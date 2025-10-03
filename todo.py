tasks = []

while True:
    print("\n1- افزودن کار")
    print("2- مشاهده کارها")
    print("3- خروج")
    choice = input("انتخاب شما: ")

    if choice == "1":
        task = input("کار جدید: ")
        tasks.append(task)
        print("کار اضافه شد!")
    elif choice == "2":
        print("لیست کارها:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        break
    else:
        print("انتخاب نامعتبر!")
