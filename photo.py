class Photo:
    def __init__(self, _id, name, _format, size, album_id):

        self.id = _id
        self.name = name
        self.format = _format
        self.size = size
        self.album = album_id

    def __str__(self):
        return "Фото #" + str(self.id) + " -" + self.name + ", Формат -" + self.format + ", Розмір -" \
               + self.size + ", " + str(self.album)
