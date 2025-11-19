#1

name = input('Введите ваше имя: ')

if name.strip().isalnum():
    name = name.lower()
    print('Имя корректно')
else:
    print('Ошибка')


#2
password = input('Введите пароль: ')

has_digit = False
has_upper = False

for sym in password:
    if sym.isdigit():
        has_digit = True
    if sym.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print('Пароль надёжен')
else:
    print('Пароль слаб')


#3

log = "ACCESS DENIED"

print(f'{log.capitalize() - вход запрещён}')


#4

data = "ERROR connection ERROR failed access"

data = data.replace("ERROR", "ALERT")
alert_count = data.count("ALERT")

print(f'Количесвто предупреждений: {alert_count}')


#5

email = input("Введите email: ")

if email.find("@") != -1:
    domain = email.split("@")[1]
    
    if domain.endswith(".com"):
        print("Домен:", domain)
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")


#6
text = input()

text = text.strip().lower().replace(" ", "_")
print(text)


#7
message = input()
if message.find("SECRET") != -1:
    message = message.replace("SECRET", "******")
    print('Опасно')
else:
    print('Безопасно')


#8

word = input()

codes = ""
for ch in word:
    codes += str(ord(ch)) + " " 
print(codes.strip())

decoded = ""
for ch in word:
    decoded += chr(ord(ch)) 

print(f'Расшифрованное сообщение: {decoded}')


#9
text = "login attempt failed access denied unauthorized access"

has_failed = text.count('failed')
has_denied = text.count('denied')

print(f'Denied: {has_denied}')
print(f'Failed: {has_failed}')

if 'failed' in text or 'denied' in text:
    print('Попытка несанкционированного доступа')


#10
report = input("Введите отчёт: ")

sentences = report.split(".")
sentence_count = 0
for s in sentences:
    if s.strip() != "":
        sentence_count += 1
print(f'Количество предложений: {sentence_count}')

report_no_spaces = report.replace(' ', '')
chars_count = len(report_no_spaces)
print(f'Количество символов без пробелов:{chars_count}')

report_lower = report.lower()
if report_lower.startswith("report"):
    print('Текст начинается с 'Report'')
else:
    print('Текст не начинается с 'Report'')


error_count = report_lower.count('error')
if error_count >= 2:
    print('Ошибки найдены')


'''
    ответы на контрольные вопросы:
    1)строка это последовательность символов которая заключена в кавычки(кавычки могут быть как одинарными так и двойными)
    является неизменяем типом данных в пайтоне

    2)юникод это стандарт кодирования символов, который позволяет использовать любые буквы, цифры, символы и тд всех языков мира
    иными словами он используется в пайтоне для того чтобы интерпретатор мог корректно работать с текстом на разных языках мира

    3)strip() - убирает пробелы  с начала и конца строки.
    replace() -заменяет все старые вхождения на новые, первым параметром указываем старое вхождение вторым новое(на которое хотим заменить)
    find()- возвращает индекс первого вхождения подстроки(параметра) или -1, если подстрока не найдена

    4)с помощью метода count()

    5)upper() делает все буквы строки заглавными
    capitalize() делает только первую букву строки заглавной, остальные  маленькими

    6)ord(char) - возвращает числовой код символа юникод
    chr(code) - возвращает символ по его числовому коду

    7)с помощью метода startswith()

    8)это помогает прежде всего отформатировать данные чтобы в дальнейшем с ними работать правильно
    еще это немаловажно для защиты от ошибок, сбоев в программе, а также атак типа SQL Injection
'''