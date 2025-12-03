# HW_7.1 Получить инициалы из ФИО

fullname = "Иванов Иван Иванович"
parts = fullname.split()

initials = f"{parts[0]} {parts[1][0]}.{parts[2][0]}."
print(initials)

# 2 Подсчёт количества слов в предложении

text = input('Enter a sentence: ')
words = text.split()
count = len(words)

print("Number of words:", count)