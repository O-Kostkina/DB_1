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
        file = open("db.txt", 'wb')
        components = {}
        components['album'] = self.albums
        components['photo'] = self.photos
        pickle.dump()
        file.close()

    def add_album(self, album):
        self.albums += [album]

    def add_photo(self, photo):
        self.photos += [photo]

    def get_albums(self):
        return self.albums

    def get_photos(self):
        return self.photos
