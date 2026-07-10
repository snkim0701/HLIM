from abc import ABC, abstractmethod

class BaseCollector(ABC):

    def __init__(self, ticker, start, end=None):
        self.ticker = ticker
        self.start = start
        self.end = end

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def save(self):
        pass