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


class Film(Media):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length


class Series(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Film('avengers: infinity war', 2018, 149)
avengers.like()
print(f'{avengers.name} - {avengers.year} - {avengers.length}: {avengers.likes}')

atlanta = Series('atlanta', 2016, 4)
atlanta.like()
atlanta.like()
print(f'{atlanta.name} - {atlanta.year} - {atlanta.seasons}: {atlanta.likes}')
