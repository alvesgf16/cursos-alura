class Playlist:
    def __init__(self, name, media):
        self._name = name
        self._media = media

    def __getitem__(self, item):
        return self._media[item]

    def __len__(self):
        return len(self._media)

    @property
    def listing(self):
        return  self._media

    @property
    def size(self):
        return len(self._media)
