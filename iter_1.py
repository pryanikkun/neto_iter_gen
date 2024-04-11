class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = iter(list_of_list)

    def _pop_element(self):
        try:
            element = next(self.current_list)
            if type(element) == list:
                self._get_current_list(element)
                element = self._pop_element()
        except StopIteration:
            element = None
        return element

    def _get_current_list(self, some_list: list = None):
        current_list = [('None' if x is None else x) for x in some_list]
        self.current_list = iter(current_list)

    def __iter__(self):
        self.current_list = iter([])
        return self

    def __next__(self):
        element = self._pop_element()

        if element is None:
            current_list = next(self.list_of_list)
            self._get_current_list(current_list)
            element = self._pop_element()
        if element == 'None':
            element = None
        return element


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


if __name__ == '__main__':
    test_1()
