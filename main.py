from random import randint
from dis import dis


# 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет
# аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
#
#                 Python example:
#
#                 def isEven(value):return value%2==0
# Ответ:
# Реализация через isEven использует операцию взятия остатка от деления, а is_even_bitwise проверяет младший бит числа.
# Если младший бит при логическом умножении на 1 не поменялся, то число четное, если поменялся, то число нечетное.

# Применение функции dis из модуля dis к функциям is_even и is_even_bitwise, которая позволяет дизассемблировать
# объект питона, выдает следующие результаты:

#  37           0 LOAD_FAST                0 (value)
#               2 LOAD_CONST               1 (2)
#               4 BINARY_MODULO
#               6 LOAD_CONST               2 (0)
#               8 COMPARE_OP               2 (==)
#              10 RETURN_VALUE
# None
#  41           0 LOAD_FAST                0 (value)
#               2 LOAD_CONST               1 (1)
#               4 BINARY_AND
#               6 LOAD_CONST               2 (0)
#               8 COMPARE_OP               2 (==)
#              10 RETURN_VALUE
# None

# По количеству операций функции равны, значит можно сделать вывод, ни одна реализация не выигрывает у другой


def is_even(value):
    return value % 2 == 0


def is_even_bitwise(value):
    return value & 1 == 0


# 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и
# минусы каждой реализации.

# Python 2.7 syntax:
# Реализация циклического буфера с возможностью записи новых данных в буфер без возникновения исключения OverflowError
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


# Реализация циклического буфера с возможностью записи новых данных в буфер. Главный минус относительно реализации
# RingBuffer - нам нужно контролировать заполнение буфера
class RingBufferOverflow(RingBuffer):
    """
    A class that implements a circular buffer with buffer overflow
    """

    def put_element(self, value):
        if self.is_full:
            raise OverflowError('Buffer is full. Can\'t put element')
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.buffer_size
        if self.head == self.tail:
            self.is_full = True

# 3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив
# чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить
# почему вы считаете, что функция соответствует заданным критериям.


if __name__ == '__main__':
    buffer = RingBufferOverflow(buffer_size=4)
    # for i in range(9):
    #     buffer.put_element(randint(0, 100))
    #     print(buffer)

    # for i in range(10):
    #     buffer.put_element(randint(0, 100))
    #     print(buffer)
    print(dis(is_even))
    print(dis(is_even_bitwise))
    # print(is_even_bitwise(20))
