# -*-coding:utf8;-*-
# qpy:3
# qpy:console

def favourite_movie(string):
    return f'My favourite movie {string}'


print(favourite_movie(' ... '))


def make_country(country, capital):
    return {'country': f'{country}', 'capital': f'{capital}'}
dictcountry = make_country("страна", "столица")


print(dictcountry)

def make_operation(oper,*cuferki):
    operfunc = "~+-*"
    itog = cuferki[0]
    if operfunc.find(oper) == 1:
        for i in cuferki[1:]:
            itog += i
    elif operfunc.find(oper) == 2:
        for i in cuferki[1:]:
            itog -= i
    elif operfunc.find(oper) == 3:
        for i in cuferki[1:]:
            itog *= i
    else:
        print(f'Not supported operator {oper}')
        exit()
    return itog
a = make_operation('*',234,23,42,34,24,34)
print(a)
b = hex()
