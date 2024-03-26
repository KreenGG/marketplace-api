from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass
class CodeException(ServiceException):
    @property
    def message() -> str:
        return "Auth code exception occurred"


@dataclass
class CodeNotFoundException(CodeException):
    code: str

    @property
    def message() -> str:
        return "Code not found"


@dataclass
class CodesNotEqualException(CodeException):
    code: str
    cached_code: str
    customer_phone: str

    @property
    def message() -> str:
        return "Codes are not equal"
