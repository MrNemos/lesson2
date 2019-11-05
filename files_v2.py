


def search(index,dictionary):
    if dictionary.get(index):
        return True
    return False


def reg_user(forma = ['name','login','password']):
    form1 = []
    for i in forma:
        print('Введите ', end='')
        if i == 'name':
            form1.append(input("имя"))
        elif i == 'login':
            check = True
            while check:
                login = input("логин:")
                check = search(login,users_data)
                if check:
                    print('Логин уже используется!')
            else:
                form1.append(login)
        elif i == 'password':
            form1.append(input('пароль: '))
        else:
            form1.append(input(f'{i}: '))
    return check_corect(form1,forma)


def check_corect(list1,form = ['name','login','password']):
    dict1 = dict()
    if len(list1) != len(form):
        print(f'Ошибка чтения даных пользевателя {list1[0:1]}')
        return False , None, form
    for i in range(0,len(form)):
        d = {f'{form[i]}':f'{list1[i]}'}
        dict1.update(d)
    return True, {f"{dict1.get('login')}":dict1},form


def read_data(name_file,users_data):
    with open(f'{name_file}',"r") as data:
        form = ''
        list1 = data.readline()
        if ',' in list1:
            form = list1
            form = form.strip().split(',')
            #print(form)
            list1 = data.readline()
        for list1 in data:
            list1 = list1.strip().split(';')
            check, user_data, form = check_corect(list1,form)
            if check:
                users_data.update(user_data)

    return users_data, form

def save_all_data(name_file,users_data,form = ['name','login','password']):
    with open(f'{name_file}', "w+") as data:
        string = ''
        for i in form:
            string = string + f'{i},'
        data.write(string[:-1] + '\n')
        string = ''
        for user in users_data:
            check = 0
            for items,user_item in users_data.get(user).items():
                if form[check] == items:
                    string = string + f'{user_item};'
                else:
                    print('что-то пошло не так')
                check += 1
            data.write(string[:-1] + '\n')

def save_new_data(name_file,new_user_data,form):
    with open(f'{name_file}', "a+") as data:
        string = ''
        for i in new_user_data:
            for check, user_items in new_user_data.get(i).items():
                if check in form:
                    string = string + '{new_user_item};'.format(new_user_item = user_items)
                else:
                    print('Что-то пошло не так')
            data.write(string[:-1] + '\n')




if '__main__' == __name__:
    vod = input("Введите логин чтобы авторизироватся, reg для регистрации либо q чтобы выйти")
    if vod in 'qQйЙ':
        exit(0)
    users_data = dict()
    users_data, form = read_data("data.txt", users_data)
    if vod == 'reg':
        new_user_data = reg_user(form)
        save_new_data('data.txt',new_user_data[1],new_user_data[2])
        users_data.update(new_user_data[1])
        login =str(list(new_user_data[1].keys())).strip("['']")
    else:
        check = True
        while check:
            check = search(vod,users_data)
            if vod in 'qQйЙ':
                exit(0)
            if not check:
                print('Login not found')
                vod = input('Login: ')
        else:
            login = vod

        i = 3
        while i>0:
            pas = input('Введите пароль: ')
            check = search(pas,users_data.get(login))
            if check:

                break
            else:
                print('wrong password')
                i-=1
        else:
            exit(0)

    print(f'Здраствуйте {users_data.get(login).get("name")}')

