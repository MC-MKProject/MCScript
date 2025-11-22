from enum import Enum, auto


class OpCode(Enum):
    LOAD_CONST = auto()      # push number
    LOAD_NAME = auto()       # push variable
    STORE_NAME = auto()      # assign variable
    CALL = auto()            # function call
    BINARY_ADD = auto()
    BINARY_SUB = auto()
    BINARY_MUL = auto()
    BINARY_DIV = auto()
    RETURN_VALUE = auto()
    POP = auto()
