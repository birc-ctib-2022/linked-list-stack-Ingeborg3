"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        # FIXME: code here

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        # FIXME: code here

    def top(self) -> T:
        """Return the top of the stack."""
        # FIXME: code here

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        # FIXME: code here

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        # FIXME: code here
