class Job:
    def __init__(self, title, company, location, source):
        self.title = title
        self.company = company
        self.location = location
        self.source = source

    def __repr__(self):
        return f"Job(title={self.title!r}, company={self.company!r}, location={self.location!r}, source={self.source!r})"
