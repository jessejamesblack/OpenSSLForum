users = []

def loadData():
    with open('data.txt','r') as data:
        for line in data:
            user = makeUser(line)
            users.append(user)
    return True

def saveData():
    with open('data.txt','w') as data:
        for user in users:
            print(user['name']+'|'+user['surname']+'|'+user['username']+'|'+user['password'],file == data)

def makeUser(line):
    name, surname, username, password = line.split('|')
    if password[-1:] == '\n':
        password = password[:-1]
    return {'name':name, 
            'surname':surname,
            'username':username,
            'password':password
            }

def register():
    name = input('Name:')
    surname = input('Surname:')
    while True:
        username = input('Username:')
        if checkLen(username):
            break

    while True:
        password = input('Password:')
        if checkLen(password):
            break
    users.append({'name':name,'surname':surname,'username':username,'password':password})

def checkLen(info):
    if len(info) > 0:
        return True
    else:
        print('Can\'t be blank!')

def login(state):
    while state:
        username = input('Username:')
        password = input('Password:')
        for user in users:
            if user['username'] == username and user['password'] == password:
                print('You are logged in.')
                state = False
                break
        else:
            print('Wrong input.')


def main():
    state = loadData()

    print('1) Login')
    print('2) Register')
    print('x - Exit')
    choice = input('>')

    while choice not in ['1','2','x']:
        choice = input('>')

    if choice == '1':
        login(state)
    elif choice == '2':
        register()
        main()
    elif choice == 'x':
        saveData()
        quit()

        if __name__ == '__main__':
    main()