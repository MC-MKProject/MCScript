from dataclasses import dataclass
from typing import List, Any


@dataclass
class Node:
    pass


@dataclass
class Number(Node):
    value: float


@dataclass
class Identifier(Node):
    name: str


@dataclass
class Let(Node):
    name: str
    value: Node


@dataclass
class BinaryOp(Node):
    left: Node
    op: str
    right: Node


@dataclass
class Call(Node):
    name: str
    args: List[Node]


@dataclass
class Program(Node):
    body: List[Node]
