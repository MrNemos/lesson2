import sys
usersdata = {}
def check_avalible(*lists):
    n = len(lists)
    if n == 3:
        return True, {'name':lists[0],'password':lists[2].split(),'login':lists[2]}
with open('users.txt', 'r') as users:
    string = users.readline()
    while string:
        ok , user = check_avalible(*string.split(';'))
        if ok:
            usersdata.setdefault(user.get('login'),user)
        print(user)
        string = users.readline()



def search_input(string,arg):
    pass
def reg_user():
    pass
    name = input()
    login = search_input(input(),"login")
    while login:
        password = input()
        break


