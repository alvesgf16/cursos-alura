from media_playlist.film import Film
from media_playlist.playlist import Playlist
from media_playlist.series import Series

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

print(f'Playlist size: {len(weekend_playlist)}')

for medium in weekend_playlist:
    print(medium)

print(daredevil in weekend_playlist)
