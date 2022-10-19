class Film:
    def __init__(self, name, year, length):
        self.__name = name.title()
        self.year = year
        self.length = length
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


avengers = Film('avengers: infinity war', 2018, 149)
avengers.like()
print(f'Name: {avengers.name} - Year: {avengers.year} - Length: {avengers.length} - Likes: {avengers.likes}')

atlanta = Series('atlanta', 2016, 4)
atlanta.like()
atlanta.like()
print(f'Name: {atlanta.name} - Year: {atlanta.year} - Seasons: {atlanta.seasons} - Likes: {atlanta.likes}')
