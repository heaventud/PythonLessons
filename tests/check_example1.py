import pytest
import collections
from example1 import function


class MyType:
    def __init__(self):
        my_var = 50


my_type = MyType()
ordered_dict = collections.OrderedDict()


@pytest.mark.parametrize('data, expected', [
    ('Katya', 'строка'),
    (3809999232344, 'число'),
    (-9, 'число'),
    (list('hello'), 'коллекция'),
    (my_type, 'undefined'),
    (ordered_dict, 'коллекция'),
    ({1, 3, 'kiss', (None, None)}, 'коллекция'),

])
def test_example1(data, expected):
    res = function(data)
    assert res.lower() == expected.lower()
