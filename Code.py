import pathlib
from colorama import init, Back, Fore
from os import mkdir, getenv
from random import choice, randint
from sys import exit
from string import ascii_letters, digits, punctuation
init()

# Сурсы:
# http://patorjk.com/software/taag/#p=display&w=░&f=ANSI%20Shadow&t=
# http://patorjk.com/software/taag/#p=display&w=▒&f=ANSI%20Shadow&t=
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=
print(Back.BLACK, Fore.CYAN, f'''
╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
║                                                                               ║
║      ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗       ║
║      ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗      ║
║      ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║      ║
║      ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║      ║
║      ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝      ║
║      ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝       ║
║                                                                               ║
║  ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗  ║
║ ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗ ║
║ ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝ ║
║ ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗ ║
║ ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║ ║
║  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ║
║                                                                               ║
║                    ██╗   ██╗  ██╗   ██████╗    ██╗  ██╗                       ║
║                    ██║   ██║ ███║   ╚════██╗   ██║  ██║                       ║
║                    ██║   ██║ ╚██║    █████╔╝   ███████║                       ║
║                    ╚██╗ ██╔╝  ██║   ██╔═══╝    ╚════██║                       ║
║                     ╚████╔╝   ██║██╗███████╗██╗     ██║                       ║
║                      ╚═══╝    ╚═╝╚═╝╚══════╝╚═╝     ╚═╝                       ║
║                                                                               ║
╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
''')
print( Fore.WHITE, '''Автор: DavePvZ#7911
Author: DavePvZ#7911''' )

# Проверка языка

path_lul = pathlib.Path(getenv('USERPROFILE') + '\\AppData\\Roaming\\Password Generator\\' )
file = pathlib.Path(f'{path_lul}\\settings.txt')
if file.exists() == True:
    with open(file, 'r') as language_file:
        language_lol = language_file.readline()
        if language_lol == 'Language = "RU"':
            language = 'RU'
        elif language_lol == 'Language = "EN"':
            language = 'EN'
        elif language_lol != 'Language = "EN"' and language_lol != 'Language = "RU"':
            input( '''Please, return the previous "Language" setting value (Press Enter).
Пожалуйста, верните прошлое значение настройки "Language" (Нажмите Enter). ''' )
            exit()
else:
    print('Please, choose language (EN or RU)')
    language = input('Пожалуйста, выберите язык (Напишите RU или EN): ')
    if language != 'RU' and language != 'EN':
        input('Wrong language! Такого языка пока что не существует!')
        exit()
    if path_lul.exists() != True:
        mkdir( path_lul )
    with open(file, 'w+') as language_file:
        language_file.write(f'Language = "{language}"')

# Информация насчёт символов для паролей

if language == 'RU':
    print( '''Выберите пожалуйста набор знаков для своего пароля (напишите цифру):
1. Заглавные и маленькие буквы с цифрами.
2. Заглавные и маленькие буквы с цифрами и знаками (запятые, точки, скобки и т.д.)
3. Свой набор знаков.
4. Рандомные числа''' )
    chars = input('Ваш выбор: ')
elif language == 'EN':
    print( '''Please, choose set of symbols for your password (write a digit):
1. Uppercase and lowercase letters with digits.
2. Uppercase and lowercase letters with digits and symbols (comma, point, parentheses, etc.)
3. Custom set of symbols.
4. Random numbers''' )
    chars = input('Your choice: ')
if chars.isdigit() != True:
    if language == 'RU':
        input('Напишите пожалуйста номер набора знаков. (Нажмите Enter)')
    elif language == 'EN':
        input('Please write a digit of set symbols. (Press Enter)')
    exit()
chars = int(chars)
randint_number = 0
if chars == 1:
    chars = ascii_letters + digits
elif chars == 2:
    chars = ascii_letters + digits + punctuation
elif chars == 3:
    if language == 'RU':
        chars = input( 'Напишите здесь все символы, которые вы хотите использовать в генерации пароля (БЕЗ ПРОБЕЛОВ): ' )
    elif language == 'EN':
        chars = input( 'Write here all symbols, what you would like to use in passwords (Without spaces): ' )
elif chars == 4:
    randint_number = 1

if randint_number == 0:
    if language == 'EN':
        amount = int( input( 'Amount of passwords: ' ) )
        lenght = int( input( 'Lenght of passwords: ' ) )
    elif language == 'RU':
        amount = int( input( 'Количество паролей: ' ) )
        lenght = int( input( 'Длина паролей: ' ) )
elif randint_number == 1:
    if language == 'RU':
        min_number = int( input( 'Минимальное число, которое можно будет получить при генерации числа: ' ) )
        max_number = int( input( 'Максимальное число, которое можно будет получить при генерации числа: ' ) )
        amount = int( input( 'Количество этих чисел: ' ) )
    elif language == 'EN':
        min_number = int(input('Minimal number, what you can receive: '))
        max_number = int(input('Max number, what you can receive: '))
        amount = int(input('Amount of numbers: '))

# Проверка на .txt

if randint_number == 0:
    file_RU = pathlib.Path( 'Пароли.txt' )
    file_EN = pathlib.Path( 'Passwords.txt' )
elif randint_number == 1:
    file_RU = pathlib.Path('Numbers.txt')
    file_EN = pathlib.Path('Числа.txt')
if file_RU.exists() == True or file_EN.exists() == True:
    for x in range( 1, 5000 ):
        if randint_number == 0:
            path_EN = pathlib.Path(f'Passwords_{x}.txt')
            path_RU = pathlib.Path(f'Пароли_{x}.txt')
        elif randint_number == 1:
            path_EN = pathlib.Path(f'Numbers_{x}.txt')
            path_RU = pathlib.Path(f'Числа_{x}.txt')
        if path_EN.exists() == True or path_RU.exists() == True:
            continue
        else:
            if language == 'EN':
                if randint_number == 0:
                    file_name = f'Passwords_{x}.txt'
                elif randint_number == 1:
                    file_name = f'Numbers_{x}.txt'
                break
            elif language == 'RU':
                if randint_number == 0:
                    file_name = f'Пароли_{x}.txt'
                elif randint_number == 1:
                    file_name = f'Числа_{x}.txt'
                break
else:
    if language == 'RU':
        if randint_number == 0:
            file_name = 'Пароли.txt'
        elif randint_number == 1:
            file_name = 'Числа.txt'
    elif language == 'EN':
        if randint_number == 0:
            file_name = 'Passwords.txt'
        elif randint_number == 1:
            file_name = 'Numbers.txt'

# Генерация паролей

passwords = ''
for number in range( 1, amount + 1 ):
    passwords += f'{number}. '
    if randint_number == 0:
        for x in range( lenght ):
            passwords += choice( chars )
    elif randint_number == 1:
        passwords += str( randint( min_number, max_number ) )
    if number == amount:
        break
    passwords += '\n'
print(passwords)

# Запись паролей

if language == 'RU':
    if randint_number == 0:
        file_start = 'Вот ваши сгенерированные пароли:\n'
    elif randint_number == 1:
        file_start = 'Вот ваши сгенерированные числа:\n'
elif language == 'EN':
    if randint_number == 0:
        file_start = 'Here your generated passwords:\n'
    elif randint_number == 1:
        file_start = 'Here your generated numbers:\n'
with open(file_name, 'a+') as passwords_list:
    passwords_list.write( file_start+passwords )

# Завершение

if language == 'RU':
    input( 'Нажмите Enter чтобы выйти... ' )
elif language == 'EN':
    input( 'Press Enter to close the program... ' )