from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from core.apps.customers.entities import Customer


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, customer: Customer, code: str) -> None:
        ...


class DummySenderService(BaseSenderService):
    def send_code(self, customer: Customer, code: str) -> None:
        print(f"Code to user {customer}, sent: {code}")


class EmailSenderService(BaseSenderService):
    def send_code(self, customer: Customer, code: str) -> None:
        print(f"Code to user {customer}, sent: {code} via email")


class PushSenderService(BaseSenderService):
    def send_code(self, customer: Customer, code: str) -> None:
        print(f"Push to user {customer}, sent: {code}")


@dataclass
class ComposeSenderService(BaseSenderService):
    sender_services: Iterable[BaseSenderService]

    def send_code(self, customer: Customer, code: str) -> None:
        for service in self.sender_services:
            service.send_code(customer, code)
