"""Implements List ADT using arrays."""

__author__ = "Maria Garcia de la Banda, modified by Brendon Taylor, Graeme Gange, and Alexey Ignatiev"
__docformat__ = "reStructuredText"

from data_structures.abstract_list import *
from data_structures.referential_array import ArrayR


class ArrayList(List[T]):
    """Implementation of a generic list with arrays.

    Attributes:
         length (int): number of elements in the list (inherited)
         array (ArrayR[T]): array storing the elements of the list

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """

    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 1) -> None:
        """Initialises self.length by calling its parent and
        self.array as an ArrayList of appropriate capacity
        :complexity: O(len(self)) always due to the ArrarR call
        """
        List.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, capacity))

    def __getitem__(self, index: int) -> T:
        """Returns the value of the element at position index
        :pre: index is 0 <= index < len(self) checked by ArrayR's method
        :complexity: O(1)
        """
        if index < 0 or len(self) <= index:
            raise IndexError("Out of bounds access in array.")
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """Sets the value of the element at position index to be item
        :pre: index is 0 <= index < len(self) checked by ArrayR's method
        :complexity: O(1)
        """
        if index < 0 or len(self) <= index:
            raise IndexError("Out of bounds access in array.")
        self.array[index] = value

    def __shuffle_right(self, index: int) -> None:
        """Shuffles all the items to the right from index
        :complexity best: O(1) shuffle from the end of the list
        :complexity worst: O(N) shuffle from the start of the list
        where N is the number of items in the list
        """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def __shuffle_left(self, index: int) -> None:
        """Shuffles all the items to the left from index
        :complexity best: O(1) shuffle from the end of the list
        :complexity worst: O(N) shuffle from the start of the list
        where N is the number of items in the list
        """
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def __resize(self) -> None:
        """
        If the list is full, doubles the internal capacity of the list,
        copying all existing elements. Does nothing if the list is not full.

        :post:       Capacity is strictly greater than the list length.
        :complexity: Worst case O(N), for list of length N.
        """

        if len(self) == len(self.array):
            new_cap = int(2 * len(self.array))
            new_array = ArrayR(new_cap)
            for i in range(len(self)):
                new_array[i] = self.array[i]
            self.array = new_array
        assert len(self) < len(
            self.array
        ), "Capacity not greater than length after __resize."

    def is_full(self):
        """Returns true if the list is full
        :complexity: O(1)
        """
        return len(self) >= len(self.array)

    def index(self, item: T) -> int:
        """Returns the position of the first occurrence of item
        :raises ValueError: if item not in the list
        :complexity: O(Comp==) if item is first; Comp== is the BigO of ==
                     O(len(self)*Comp==) if item is last
        """
        for i in range(len(self)):
            if item == self[i]:
                return i

        raise ValueError(f"{item} not in the list")

    def delete_at_index(self, index: int) -> T:
        """Moves self[j+1] to self[j] if j>index, returns old self[index].
        Do shuffling by means of self.__shuffle_left().
        :pre: index is 0 <= index < len(self) - this is checked by __getitem__() !
        :complexity: O(len(self) - index)
        """
        item = self[index]
        self.length -= 1
        self.__shuffle_left(index)
        return item

    def insert(self, index: int, item: T) -> None:
        """Moves self[j] to self[j+1] if j>=index & sets self[index]=item.
        Do shuffling by means of self.__shuffle_right().
        If the list is full, it should be extended with the use of self.__resize().
        :complexity: O(len(self)-index) if no resizing needed, O(len(self)) otherwise
        """
        # Ensure index is valid
        if index < 0 or index > len(self):
            raise IndexError("Index out of bounds")

        # Resizes array if it's full
        if self.is_full():
            self.__resize()

        self.__shuffle_right(index)
        self.length += 1
        self[index] = item
