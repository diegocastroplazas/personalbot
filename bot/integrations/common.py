from abc import ABC, abstractmethod


class CommonIntegration(ABC):
    connection_params = dict()

    @abstractmethod
    def connect(self):
        pass


    @abstractmethod
    def perform_task(self):
        pass