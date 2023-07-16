from multiprocessing import Queue

from process_broker._broker import BrokerProcess


class Factory:
    @staticmethod
    def create_broker(pylogix_url: str, pywebview_url: str, queue: Queue):
        broker = BrokerProcess.get_instance(
            pylogix_url=pylogix_url, pywebview_url=pywebview_url, queue=queue
        )
        return broker
