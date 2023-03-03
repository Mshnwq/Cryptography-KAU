from abc import ABC, abstractmethod
from pydantic import BaseModel, validator
from typing import Optional


class EncModel(BaseModel):
    text: str
    key: str
    isEncrypt: Optional[bool] = True

    # @validator('key', allow_reuse=True)
    # def check_hex(cls, value):
    #     if not all(c in 'x$0123456789abcdefABCDEF' for c in value):
    #         raise ValueError('not a valid hex string for key')
    #     return value


class Algorithm(ABC):

    @abstractmethod
    def encrypt(self, args: EncModel) -> str:
        pass

    @abstractmethod
    def decrypt(self, args: EncModel) -> str:
        pass

    @staticmethod
    @abstractmethod
    def generateKey(size: int):
        pass

    @staticmethod
    @abstractmethod
    def isAsymmetric() -> bool:
        pass

    @staticmethod
    @abstractmethod
    def hasFPGA() -> bool:
        pass

    @staticmethod
    @abstractmethod
    def getKeyBitSizes():
        pass
