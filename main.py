account1 = {'login':'ivan','password':'q1'}                                                #создаем аккаунты
account2 = {'login':'petr','password':'q2'}
account3 = {'login':'olga','password':'q3'}
account4 = {'login':'anna','password':'q4'}

user1 = {'name':'Иван','age':20,'account':account1}                                        #создаем юзеров
user2 = {'name':'Петр','age':25,'account':account2}
user3 = {'name':'Ольга','age':18,'account':account3}
user4 = {'name':'Анна','age':27,'account':account4}

user_list = [user1, user2, user3, user4]                                                   #создаем список из юзеров

key = input('Введите ключ (name  или account): ').lower()                                  #принимаем пользовательский ввод
for user in user_list:
    try:
        print(f'значение ключа {key} для юзера {user_list.index(user) + 1} = {user[key]}') #исчем значение по ключу
    except:
        print('Введенный ключ не найден')
        break

key = input('Введите порядковый номер: ')                                                  #снова принимаем пользовательский ввод
try:
    current_user = user_list[int(key) - 1]                                                 #выбираем пользователя из списка по ключу
    print(f'''Данные по юзеру № {key}:
имя: {current_user['name']}
возраст: {current_user['age']}
логин: {current_user['account']['login']}
пароль: {current_user['account']['password']}''')
except:
    print('Пользователь с указанным номером не найден')

medium_ariphmetics = 0                                                                     #считаем среднее арифметическое возраста пользователей
for i in user_list:
    medium_ariphmetics += i['age']
medium_ariphmetics = medium_ariphmetics / 4

print(f'Средний возраст пользователей: {medium_ariphmetics}')

key = input('Введите номер пользователя, которого нужно переместить в конец: ')            #пользовательский ввод
try:
    print(f'Список до изменения:\n {user_list}')                                           #перемещение пользователя в конец
    user_moving = user_list.pop(int(key) - 1)
    user_list.append(user_moving)
    print('Пользователь с именем ' + user_moving['name'] + ' перемещен в конец')
    print(f'Список после изменения:\n {user_list}')
except:
    print('Возникла ошибка при перемещении пользователя в конец')
