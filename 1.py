name = input("введите имя: ")
surname = input("введите фамилию: ")
year = int(input("введите год рождения: "))
print(name, surname, year, sep = "_")
name, surname = surname, name
print(name, surname, year + 60)
