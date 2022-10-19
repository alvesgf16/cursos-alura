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


class Playlist:
    def __init__(self, name, media):
        self._name = name
        self._media = media

    @property
    def listing(self):
        return  self._media

    @property
    def size(self):
        return len(self._media)

avengers = Film('avengers: infinity war', 2018, 149)
atlanta = Series('atlanta', 2016, 4)
scary_movie = Film('scary movie', 2000, 88)
daredevil = Series('Daredevil', 2015, 3)

avengers.like()
scary_movie.like()
scary_movie.like()
scary_movie.like()
scary_movie.like()
daredevil.like()
daredevil.like()
atlanta.like()
atlanta.like()
atlanta.like()

films_and_series = [avengers, atlanta, daredevil, scary_movie]
weekend_playlist = Playlist('weekend', films_and_series)

print(f'Playlist size: {len(weekend_playlist.listing)}')

for medium in weekend_playlist.listing:
    print(medium)
