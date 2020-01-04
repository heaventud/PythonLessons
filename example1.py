
def function(x):
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
if __name__ == '__main__':
    x = function(True)
    print(x)
