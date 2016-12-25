class Album:
    def __init__(self, _id, name, author, subject):
        self.id = _id
        self.name = name
        self.author = author
        self.subject = subject

    def __str__(self):
        return "Альбом #" + str(self.id) + " - " + self.name + ", автор - " + self.author +\
               ", тематика - " + str(self.subject)
