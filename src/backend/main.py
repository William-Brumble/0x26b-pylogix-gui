import time
import signal
import argparse
from logging import getLogger, Formatter, StreamHandler, DEBUG, NullHandler
from logging.handlers import QueueListener, QueueHandler
from multiprocessing import freeze_support, Queue

from process_broker.factory import Factory as BrokerFactory
from process_pywebview.factory import Factory as PywebviewFactory
from process_pylogix.factory import Factory as PylogixFactory

parser = argparse.ArgumentParser(description="Pylogix GUI")
parser.add_argument(
    "-p", "--port", default=65535, help="Port for the server to listen on"
)
parser.add_argument("-t", "--token", default=None, help="The pywebview token")
parser.add_argument(
    "--simulate", action="store_true", help="Simulate a connection to a PLC"
)
parser.add_argument(
    "--logging", action="store_true", help="Enable debug logging to console"
)
parser.add_argument(
    "--debug", action="store_true", help="Enable pywebview debug window"
)
args = parser.parse_args()


def time_to_bail(signal=None, frame=None):
    for process in processes:
        if process.is_alive():
            process.terminate()
            process.join()
    queue_listener.stop()
    quit(-1)


if __name__ == "__main__":
    freeze_support()
    signal.signal(signal.SIGINT, time_to_bail)

    root_logger = getLogger()
    root_logger.addHandler(NullHandler())
    formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    if args.logging:
        root_stream_handler = StreamHandler()
        root_stream_handler.setLevel(DEBUG)
        root_stream_handler.setFormatter(formatter)
        root_logger.addHandler(root_stream_handler)
    logging_queue = Queue(-1)
    queue_listener = QueueListener(logging_queue, root_logger)
    queue_listener.start()

    processes = [
        BrokerFactory.create_broker(
            pywebview_url="tcp://*:5559",
            pylogix_url="tcp://*:5560",
            queue=logging_queue,
        ),
        PylogixFactory.create_pylogix(
            pylogix_url="tcp://localhost:5560",
            queue=logging_queue,
            simulate=args.simulate,
        ),
        PywebviewFactory.create_pywebview(
            pywebview_url="tcp://localhost:5559",
            queue=logging_queue,
            window_name="0x26b-pylogix-gui",
            port=args.port,
            token=args.token,
            debug=args.debug,
        ),
    ]

    for process in processes:
        process.start()
        time.sleep(0.1)

    while True:
        for process in processes:
            if not process.is_alive():
                time_to_bail()
        time.sleep(1)
