from dataclasses import dataclass


@dataclass
class ServiceException(Exception):
    @property
    def message() -> str:
        return "App exception occurred"
