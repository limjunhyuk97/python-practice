class Post:
    """
    param id
    param title
    param content
    param view_count
    """
    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def set_post(self, id, title, content, view_content):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_content

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_view_count(self):
        return self.view_count

    def view_count_increment(self):
        self.view_count += 1

    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def set_view_count(self, view_count):
        self.view_count = view_count

    def __str__(self):
        return f"{self.id}. {self.title}\n{self.content}\nview : {self.view_count}\n"





