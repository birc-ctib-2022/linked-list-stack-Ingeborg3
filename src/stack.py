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

class EmptyStack(Exception):
    pass


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T.
        >>> x = Stack()
        >>> print(x)
        None
        >>> x.dummy
        Link(head=None, tail=None)
        >>> x.last
        Link(head=None, tail=None)
        """
        # Create empty singly linked list with dummy element at
        # beginning.
        self.dummy = Link(None, None)
        # When the singly-linked list is empty, the last link in the
        # list is the dummy element.
        self.last = self.dummy 

    def push(self, x: T) -> None:
        """Push x on the top of this stack.
        >>> x = Stack()
        >>> x.push(1)
        >>> print(x)
        Link(head=1, tail=None)
        """
        new_link = Link(x, self.dummy.tail)
        self.dummy.tail = new_link
        if self.dummy == self.last: # if x inserted into an empty
            # singly-linked list.
            self.last = self.dummy.tail


    def top(self) -> T:
        """Return the top of the stack.
        >>> x = Stack()
        >>> x.push(1)
        >>> print(x.top()) 
        1
        """
        if self.is_empty(): # if the stack is empty
            raise EmptyStack()
        top = self.dummy.tail.head
        return top

    def pop(self) -> T:
        """Pop the top element off the stack and return it.
        >>> x = Stack()
        >>> x.push(1)
        >>> print(x.pop())
        1
        >>> print(x)
        None
        >>> x.last
        Link(head=None, tail=None)
        """
        if self.is_empty(): # if the stack is empty
            raise EmptyStack()
        # get top element
        top = self.dummy.tail.head
        # delete top element
        self.dummy.tail = self.dummy.tail.tail
        # if empty stack after deletion
        if self.dummy.tail is None:
            self.last = self.dummy    
        return top

    def is_empty(self) -> bool:
        """Test if the stack is empty.
        >>> x = Stack()
        >>> x.is_empty()
        True
        >>> x.push(1)
        >>> print(x.is_empty())
        False
        """
        return self.dummy == self.last

    def __str__(self):
        return repr(self.dummy.tail)

