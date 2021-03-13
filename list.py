def plus():
    nom = len(my_list)
    my_list.append(str(nom + 1) + "." + input("Какое задание добавим: "))
def popped():
    popped_list = my_list.pop(-1 + int((input("Какое задание удалим: "))))

    for task in my_list:
        print(task)
    print("\n...")
    print("Зделаные задания: ")
    print(popped_list)

def display():
    print("План на месяц: ")
    for task in my_list:
        print(task)
    print("\n...")
    print("Зделаные задания: ")

def condition():
    if what == 'p':
        plus()
        display()

    if what == "m":
        popped()



my_list = [
    '1. Выучить Django',
    '2. Выучить requests',
]

while True:
    what = input("Что делаем? ")
    condition()
    if what == 's':
        print("\nИтоговый список: ")
        print()
        for task in my_list:
            print(task)
        print("\nЗавершено.")
        break


