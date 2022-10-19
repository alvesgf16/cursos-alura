from media_playlist.media import Media


class Film(Media):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'{self.name} - {self.year} - {self.length} min: {self.likes} likes'
