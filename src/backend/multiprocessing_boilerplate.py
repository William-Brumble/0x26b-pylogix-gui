from logging import NullHandler, getLogger, DEBUG, StreamHandler, Formatter, LogRecord, FileHandler
from logging.handlers import QueueHandler, QueueListener
import time
import multiprocessing
import zmq

root_logger = getLogger()
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

root_stream_handler = StreamHandler()
root_stream_handler.setLevel(DEBUG)
root_stream_handler.setFormatter(formatter)
root_logger.addHandler(root_stream_handler)

def pylogix_worker_process(queue, pUrl="tcp://127.0.0.1:5555", pTopic="pylogix"):
    # logging
    pylogix_logger = getLogger("pylogix-process")
    pylogix_logger.setLevel(DEBUG)
    pylogix_logger.addHandler(NullHandler())
    if queue:
        handler = QueueHandler(queue)
        pylogix_logger.addHandler(handler)

    # subscribing
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(pUrl)
    socket.setsockopt(zmq.SUBSCRIBE, pTopic.encode("utf-8"))

    # listening
    try:
        while True:
            topic, msg = socket.recv_multipart()
            decoded_topic = topic.decode("utf-8")
            decoded_message = msg.decode("utf-8")
            if decoded_message == "stop": # sentinel
                break
            pylogix_logger.info(
                f"topic: {decoded_topic}, got message: {decoded_message}"
            )
    except KeyboardInterrupt:
        pass

    # closing
    socket.close(linger=5)
    context.term()


if __name__ == "__main__":
    logging_queue = multiprocessing.Queue(-1)
    queue_listener = QueueListener(logging_queue, root_logger)

    main_logger = getLogger("main-process")
    main_logger.setLevel(DEBUG)
    handler = QueueHandler(logging_queue)
    main_logger.addHandler(handler)

    # main zeromq publisher
    pub_sub_url = "tcp://127.0.0.1:5555"
    pub_sub_topic = "pylogix"
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(pub_sub_url)

    # Create a worker process
    pylogix_worker = multiprocessing.Process(
        target=pylogix_worker_process,
        args=(logging_queue,),
        kwargs={"pUrl": pub_sub_url, "pTopic": pub_sub_topic},
    )

    pylogix_worker.start()
    time.sleep(0.1) # give subscriber some time to start

    for iteration in range(10):
        main_logger.info(f"sending message: {iteration}")
        socket.send_multipart([pub_sub_topic.encode("utf-8"), f"{iteration}".encode("utf-8")])
        time.sleep(1)


    socket.send_multipart([pub_sub_topic.encode("utf-8"), f"stop".encode("utf-8")])
    pylogix_worker.join()

    main_logger.info("main is finished")