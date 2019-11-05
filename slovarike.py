import re

words = dict({'вы':1})
def searchword(string):
    """
    Функция ищет слова и ведет их учёт в словаре
    :param string: str
     upadate dict(words)
    :return: none
    """
    listword = re.findall(r'\w+',string.lower())
    i = 0
    for i in listword:
        #print(i)
        if i.isdigit():
            continue
        elif words.get(f'{i}', False):
           words[f'{i}'] += 1
        else:
            d = {f"{i}":1}
            words.update(d)

a = "Вы посещали эту страницу несколько раз. Дата последнего посещения: 01.09.19"
searchword(a)
print(words)

