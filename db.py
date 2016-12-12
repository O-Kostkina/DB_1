import pickle
class DataBase:

    def __init__(self):
        file = open("db.txt", 'r')
        components = pickle.load(file)
        self.album = components['album']
        self.photo = components['photo']
        file.close()

    def __del__(self):
        file = open("db.txt", 'wb')
        components = {}
        components['album'] = self.album
        components['photo'] = self.photo
        pickle.dump()
        file.close()

db = DataBase()
