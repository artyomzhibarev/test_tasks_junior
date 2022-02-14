from random import randint


def is_even(value):
    return value % 2 == 0


def is_even_bitwise(value):
    print(value, bin(value))
    return value & 1 == 0


def is_even_shift(value):
    return value >> 5
    # while True:
    #     value >> 1
    # else:
    #     ...


# TODO реализовать класс буфера с возможностью добавления элемента, когда он заполнен
class RingBuffer:
    """
    A class that implements a circular buffer without buffer overflow
    """
    def __init__(self, buffer_size=10):
        self.buffer_size = buffer_size
        self.buffer = [None for _ in range(buffer_size)]
        self.head = 0
        self.tail = 0
        self.is_full = False

        if not isinstance(buffer_size, int) or buffer_size < 1:
            raise ValueError

    def __str__(self):
        return '[' + ', '.join([str(element) for element in self.buffer]) + ']'

    def is_buffer_empty(self):
        return self.tail == self.head

    def put_element(self, value):
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.buffer_size

    def read_element(self):
        if self.is_buffer_empty():
            raise Exception('Buffer is empty. Can\'t read element')
        element = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.buffer_size
        return element


class RingBufferOverflow(RingBuffer):
    """
    A class that implements a circular buffer with buffer overflow
    """
    def put_element(self, value):
        if self.is_full:
            raise Exception('Buffer is full. Can\'t put element')
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.buffer_size
        if self.head == self.tail:
            self.is_full = True


if __name__ == '__main__':
    buffer = RingBufferOverflow(buffer_size=4)
    # for i in range(9):
    #     buffer.put_element(randint(0, 100))
    #     print(buffer)

    for i in range(10):
        buffer.put_element(randint(0, 100))
        print(buffer)
