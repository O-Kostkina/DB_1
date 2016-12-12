class Photo:
    def __init__(self, name, _format, size, _id):
        self.name = name
        self.format = _format
        self.size = size
        self.album = _id

    def __str__(self):
        return "Фото -" + self.name + ", Формат -" + self.format + ", Розмір -" + self.size + ", Альбом " + self.album