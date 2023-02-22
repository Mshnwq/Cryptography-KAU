# from abc import ABC, abstractmethod
import abc
from pydantic import BaseModel, validator
from typing import Optional


class EncModel(BaseModel):
    plainText: str
    key: str
    isEncrypt: Optional[bool] = True

    @validator('plainText')
    def check_hex(cls, value):
        if not all(c in '0123456789abcdefABCDEF' for c in value):
            raise ValueError('not a valid hex string')
        return value


class Algorithm(abc.ABC):

    @abc.abstractmethod
    def encrypt(self, args: EncModel) -> str:
        pass

    @abc.abstractmethod
    def decrypt(self, args: EncModel) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def generateKey(size: int):
        pass

    @staticmethod
    @abc.abstractmethod
    def isAsymmetric() -> bool:
        pass

    @staticmethod
    @abc.abstractmethod
    def getKeyBitSizes():
        pass
