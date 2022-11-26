# Linked list stack

You can easily build a stack from singly-linked lists. Recall that a link can be defined this way:

```python
@dataclass
class Link(Generic[T]):
    head: T
    tail: List[T]

# A List is either None or a Link[T]
List = Optional[Link[T]]
```

**Exercise:** Implement a stack by filling in the blanks in the code below (and in `src/stack.py`):

```python
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
```

I have not written tests for you, so you have to write those yourself if you want minimal certainty that your implementation is correct.
