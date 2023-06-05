from abc import ABC, abstractmethod


class IParser(ABC):

    @abstractmethod
    def get_requests(self):
        pass


class HHApi(IParser):
    _exemplar = None

    def __new__(cls, *args, **kwargs):
        if not cls._exemplar:
            cls._exemplar = super().__new__(cls)
        return cls._exemplar

    def get_requests(self):
        pass
