class Album:
    def __init__(self, name, author, subject):
        self.name = name
        self.author = author
        self.subject = subject

    def __str__(self):
        return "Альбом -" + self.name + ", автор -" + self.author + ", тематика -" + self.subject
