from db import DataBase
from album import Album
from photo import Photo

db = DataBase()
while True:
    command = input("Введіть команду (для виведення списку команд введіть - 'help'):\n")

    if command == "help":
        print("Введіть цифру для вибору команди")
        print("1 - SELECT * FROM")
        print("2 - DELETE \"item\" FROM")
        print("3 - INSERT INTO")
        print("4 - UPDATE")
        print("5 - Filter")
        print("6 - Stop program")

    elif command == "1":
        selection = input("select 'albums'(1) or 'photos'(2)\n")
        if selection == "1":
            for album in db.get_albums():
                print(album)
        elif selection == "2":
            for photo in db.get_photos():
                print(photo)

    elif command == "3":
        selection = input("select 'albums'(1) or 'photos'(2) than enter all values of fields\n")
        if selection == "1":
            name = str(input("Введіть назву альбому:\n"))
            author = str(input("Введіть автора альбому:\n"))
            subject = str(input("Введіть тематику альбому:\n"))
            db.add_album(name, author, subject)

        elif selection == "2":
            name = str(input("Введіть назву фото\n"))
            format = str(input("Введіть формат фото\n"))
            size = str(input("Введіть розмір фото\n"))
            album = str(input("Введіть номер альбому до якого відноситься фото\n"))
            db.add_photo(name, format, size, album)

    elif command == "2":
        selection = input("Enter name of item that you want to delete (select 'albums'(1) or 'photos'(2)):\n")
        if selection == "1":
            sel = input("Enter number of album you want to delete\n")
            db.del_album(db.get_album_by_id(sel))

        elif selection == "2":
            sel = input("Enter number of photo you want to delete\n")
            db.del_photo(db.get_photo_by_id(sel))

    elif command == "4":
        selection = input("Enter name of item that you want to change (select 'albums'(1) or 'photos'(2)):\n")
        if selection == "1":
            i = input("Enter id of album\n")
            sel = input("Enter what field do you want to change in table: name(1), author(2) or subject(3)\n")
            val = input("Enter new value\n")
            al = db.get_album_by_id(i)
            if al:
                if sel == "1":
                    al.name = val
                if sel == "2":
                    al.author = val
                if sel == "3":
                    al.subject = val

        if selection == "2":
            i = input("Enter id of photo\n")
            sel = input("Enter what field do you want to change in table: name(1), format(2) or size(3)\n")
            val = input("Enter new value\n")
            al = db.get_photo_by_id(i)
            if al:
                if sel == "1":
                    al.name = val
                if sel == "2":
                    al.format = val
                if sel == "3":
                    al.size = val

    # elif command == "5":


    elif command == "6":
        break

    else:
        print("Невідома команда")





