#1

name = input("Введите имя: ").strip()

if name.isalnum():
    name = name.lower()
    print("Имя корректно:", name)
else:
    print("Ошибка")

#2
password = input("Введите пароль: ")

has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if len(password) >= 8 and has_digit and has_upper:
    print("Пароль надёжен")
else:
    print("Пароль слаб")

#3
log = "ACCESS DENIED"
result = log.capitalize() + " – вход запрещён"
print(result)


#4
data = "ERROR connection ERROR failed access"

new_data = data.replace("ERROR", "ALERT")
count_alert = new_data.count("ALERT")

print(new_data)
print("Количество предупреждений:", count_alert)


#5

email = input("Введите email: ")

if "@" in email:
    parts = email.split("@")
    if len(parts) == 2 and parts[1] != "":
        print("Домен:", parts[1])
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")


#6
text = input("Введите текст: ")

normalized = text.strip().lower().replace(" ", "_")
print(normalized)


#7
msg = input("Введите строку: ")

if msg.find("SECRET") != -1:
    safe = msg.replace("SECRET", "******")
    print("Обнаружены секретные данные!")
    print(safe)
else:
    print("Данные безопасны.")


#8
word = input("Введите слово: ")

codes = [ord(ch) for ch in word]
print("Коды символов:", codes)

decoded = ''.join(chr(code) for code in codes)
print("Восстановленное слово:", decoded)


#9
text = "login attempt failed access denied unauthorized access"

count_failed = text.count("failed")
count_denied = text.count("denied")

print("failed:", count_failed)
print("denied:", count_denied)

if count_failed > 0 or count_denied > 0:
    print("Попытка несанкционированного доступа")


#10
report = input("Введите отчёт: ")

sentences = [s for s in report.split(".") if s.strip() != ""]
num_sentences = len(sentences)

count_chars = len(report.replace(" ", ""))

starts_correct = report.lower().startswith("report")

errors = report.lower().count("error")
error_msg = "Ошибки найдены" if errors >= 2 else "Ошибок нет"

print("Предложений:", num_sentences)
print("Символов без пробелов:", count_chars)
print("Начинается с 'Report':", starts_correct)
print(error_msg)


"""
1. это неизменяемая последовательность символов, объект типа str.

2. это стандарт, который присваивает каждому символу уникальный номер.
Позволяет работать с любым языком и любыми символами.

3. strip() — удаляет пробелы по краям

replace(a, b) — заменяет подстроку a на b

find(x) — возвращает индекс первого вхождения x или -1

4. text.count("подстрока")

5. upper() — все символы в верхний регистр.

capitalize() — только первый символ строки заглавный, остальные — строчные.

6. ord('A')  код символа (число).

chr(65)  символ по коду.

7. text.startswith("слово")

8. чтобы предотвратить: ошибки ввода,некорректные данные,уязвимости (SQL-инъекции и тд),угрозы безопасности и утечки информации.
"""