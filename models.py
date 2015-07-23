


class Series(object):

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return self.name


class Episode(object):

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return self.name


class Organization(object):

    def __init__(self, name=None):
        self.name = name


    def __str__(self):
        return self.name


class Actor(object):

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return self.name
