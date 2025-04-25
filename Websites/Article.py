

class Article:
    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.date}\nContent: {self.content}"