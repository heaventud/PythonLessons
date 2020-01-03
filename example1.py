
def test_function(x):
    if type(x) == str:
        return 'Строка'
    elif type(x) in [int, float, complex, bytes]:  #почему не могу тип long?
        return 'Число'
    elif type(x) in [dict, list, tuple, set, frozenset]:
        return 'Коллекция'
    elif type(x) == bool:
        return 'Булевый тип'
    else:
        return 'undefined'

x = test_function(True)
print(x)