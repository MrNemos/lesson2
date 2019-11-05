import random
import Capcha
num = 0
ans = 0
numbers = list([0,])
answers = ''
nazval = {"-":'число меньше',"+":'число больше',"=":'Угадал!'}
def botcreather(n):
    return random.randint(1,n)
def searchans(answers,ans):
    b = answers[::-1]
    k = 0
    while ans == b[k]:
        k+=1
    return k
def botanswer(num, a):
    if a < num:
        ans = "-"
        #print('меньше')
    elif a > num:
        ans = "+"
        #print('больше')
    else:
        ans = "="
        #print('Угадал')
    return ans
def botqueshtion(num, ans, n,):
    '''

    :param текущее число:
    :param ответ:
    :param диапазон:
    :return:
    '''
    if num == 0:        #первое число
        num = n // 2
    else:
        if ans.find('-') == 0:
            if num == min(numbers[1:]):             #если число самое маленькое в списке
                num = num // 2
            else:
                if answers[-2] == '-':              #если предидущий ответ был меньше
                    k = searchans(answers,ans)
                    num = (num - numbers[i - k]) // 2 + numbers[i - k]
                else:
                    num = (num - numbers[i - 1]) // 2 + numbers[i - 1]
        elif ans.find('+') == 0:                    #если число самое большое в списке
            if num == max(numbers):
                num = (n - num) // 2 + num + 1
            else:
                if answers[-2] == '+':
                    k = searchans(answers,ans)
                    num = (numbers[i - k] - num) // 2 + num
                else:
                    num = (numbers[i - 1] - num) // 2 + num
    return num
n = int(input("Введите диапазон: "))
a = botcreather(n)
#print(a)
i = 0
while num != a and i < 100:
    num = botqueshtion(num, ans, n,numbers)
    ans = botanswer(num,a)
    numbers.append(num)
    answers = answers + ans
    i += 1
    #print(f'{a} {num} {numbers[i-1]} {i} {ans}')

print(f'Бот отгадал число с {i} попытки')
num = int(input('Твоя очередь: '))
while num != a:
    ans = botanswer(num,a)
    print(nazval.get(f'{ans}'))
    i -= 1
    num = int(input(f'Осталось {i} попыток: '))

if i > 1:
    print('Везунчик!')
else:
    print('Хмм...   (-_-)')
    capcha = random.randint(4096, 268435456)
    capchastr = str(hex(capcha))
    capchastr = capchastr[2:]
    Capcha.printhex(capcha)
    q = input('Вот тебе капча: ')
    if q.lower() == capchastr.lower():
        print('Ну и ладно')
    else:
        print('...')
