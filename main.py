from db import DataBase
from album import Album
from photo import Photo

db = DataBase()
while True:
    command = input("Введіть команду (для виведення списку команд введіть - 'help'):\n")
    if command == "q":
        break
    elif command == "help":
        print("Введіть цифру для вибору команди")
        print("1 - SELECT * FROM")
        print("2 - DELETE \"item\" FROM")
        print("3 - INSERT INTO")
        print("4 - UPDATE")
        print("4 - Filter")
        print("6 - Stop program&quot;")

    elif command == "1":
        selection = input("")
        if selection == "albums":
            for album in db.get_albums():
                print(album)
        elif selection == "photos":
            for photo in db.get_photos():
                print(photo)

    else:
        print("Невідома команда")



