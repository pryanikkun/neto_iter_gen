import types


def gen_lists(some_list):
    for el in some_list:
        if type(el) == list:
            yield from gen_lists(el)
        else:
            yield el


def flat_generator(list_of_lists):

    for list_ in list_of_lists:
        list_ = [('None' if x is None else x) for x in list_]
        for element in list_:
            if type(element) == list:
                element = gen_lists(element)
                yield from element
            elif element == 'None':
                yield None
            else:
                yield element


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
