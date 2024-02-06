import types


# Домашняя работа. Задание №1.
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count = -1
        self.list_len = len(self.list_of_list)

    def __iter__(self):
        self.count += 1
        self.count_2 = 0
        return self

    def __next__(self):
        if self.count_2 == len(self.list_of_list[self.count]):
            iter(self)
        if self.count == self.list_len:
            raise StopIteration
        self.count_2 += 1
        return self.list_of_list[self.count][self.count_2 - 1]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Домашняя работа. Задание №2.
def flat_generator(list_of_lists):
    count = len(list_of_lists)
    for i in range(count):
        count_2 = len(list_of_lists[i])
        for z in range(count_2):
            yield list_of_lists[i][z]


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
