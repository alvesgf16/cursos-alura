class Media:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self.name} - {self.year}: {self.likes} likes'


class Film(Media):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'{self.name} - {self.year} - {self.length} min: {avengers.likes} likes'


class Series(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons} seasons: {self.likes} likes'


avengers = Film('avengers: infinity war', 2018, 149)
avengers.like()

atlanta = Series('atlanta', 2016, 4)
atlanta.like()
atlanta.like()

films_and_series = [avengers, atlanta]

for media in films_and_series:
    print(media)
