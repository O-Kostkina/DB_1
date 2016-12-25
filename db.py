import pickle
from album import Album
from photo import Photo


class DataBase:

    def __init__(self):
        try:
            file = open("db.txt", 'rb')
            components = pickle.load(file)
            self.albums = components['album']
            self.photos = components['photo']
            file.close()
        except EOFError:
            self.albums = []
            self.photos = []

    def __del__(self):
        try:
            file = open("db.txt", 'wb')
            components = {'album': self.albums, 'photo': self.photos}
            print(components)
            pickle.dump(components, file)
            file.close()
        except Exception as e:
            print(e)

    def add_album(self, name, author, subject):
        i = self.albums[-1].id + 1 if self.albums else 1
        album = Album(i, name, author, subject)
        self.albums += [album]

    def add_photo(self, name, format, size, album):
        al = self.get_album_by_id(album)
        if al:
            i = self.photos[-1].id + 1 if self.photos else 1
            photo = Photo(i, name, format, size, al)
            self.photos += [photo]
        else:
            print("Альбому з таким id не знайдено")

    def get_albums(self):
        return self.albums

    def get_photos(self):
        return self.photos

    def del_album(self, album):
        for i in self.photos:
            if str(i.album.id) == str(album.id):
                print("deleting " + str(i) + " by cascade")
                self.photos.remove(i)
        self.albums.remove(album)

    def del_photo(self, photo):
        self.photos.remove(photo)

    def get_album_by_id(self, _id):
        for i in self.albums:
            if str(i.id) == _id:
                return i
        return None

    def get_photo_by_id(self, _id):
        for i in self.photos:
            if str(i.id) == _id:
                return i
        return None

    def find_by_filter(self):
        s = set()
        for i in self.photos:
            if i.format == "bmp":
                s.add(i.album.id)
        for i in list(s):
            print(self.get_album_by_id(str(i)))



    #def update_value(self, album):

    #def update_value(self, photo):

    #def filter_item(self, album):

    #def filter_item(self, photo):
