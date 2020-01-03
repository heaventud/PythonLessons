
def test_function(x):
    
    if type(x) == str:
        return 'Строка'
    elif type(x) in [int, float, complex, bytes]:  #почему не могу тип long?
                                                   # long нет такого типа
        return 'Число'
    # Такое сравнение не пойдет
    # Вот пример коллекции которая здесь не сработает collections.OrderedDict(), хотя это тоже коллекция
    elif type(x) in [dict, list, tuple, set, frozenset]:
        return 'Коллекция'
    elif type(x) == bool:
        return 'Булевый тип'
    # да, по сути такая обработака и имелась в виду 
    else:
        return 'undefined'
# вызов здесь не надо делать
x = test_function(True)
print(x)