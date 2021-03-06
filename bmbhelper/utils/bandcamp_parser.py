import requests

from bs4 import BeautifulSoup
from typing import List


class AttrDict(dict):

    def __init__(self, *args, **kwargs):
        len_fields = len(self.fields)
        len_args = len(args)
        if len(self.fields) != len(args):
            IOError(
                f'Wrong number of arguments passed to the constructor: {len_fields}=/={len_args}')
        super().__init__()
        self._create_attributes(*args, **kwargs)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def _create_attributes(self, *initial_field_values, **optional_attributes):
        for i, attr in enumerate(self.fields):
            setattr(self, attr, initial_field_values[i])

        for key_attr in optional_attributes.keys():
            setattr(self, key_attr, optional_attributes[key_attr])

    def to_dict(self):
        return self


class AlbumMetaData(AttrDict):

    fields = ("album_artist",
              "album_name",
              "album_release_date",
              "album_cover_art",
              "album_url"
              )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return self


class AlbumTrack(AttrDict):
    fields = ("track_number", "track_title", "track_length")

    def __str__(self):
        return f'{self.track_number}\t{self.track_title}\t{self.track_length}'


class TrackList(object):
    def __init__(self) -> None:
        self._tracks: List[AlbumTrack] = list()

    def push(self, track: AlbumTrack) -> None:
        self._tracks.append(track)

    @property
    def tracks(self):
        return self._tracks

    def __getitem__(self, index):
        return self._tracks[index]

    def __str__(self):
        result = "\r"
        for t in self._tracks:
            result += f'{t}\n'
        return result

    def __len__(self):
        return len(self._tracks)


class BandcampParser(object):

    def __init__(self, url: str) -> None:
        self.url = url
        self.release_meta: AlbumMetaData = None
        self.release_tracks: TrackList = TrackList()

    def fetch_album(self) -> None:
        soup = self.fetch_url_soup(self.url)
        self.parse_meta(soup)
        self.parse_tracks(soup)

    @staticmethod
    def fetch_url_soup(album_url):
        r = requests.get(album_url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def parse_meta(self, soup: BeautifulSoup):

        artist = soup.find(itemprop="byArtist").a.text
        album = soup.find(class_="trackTitle").text.strip('\n ')

        release_date = soup.find(itemprop="datePublished")['content']
        # split to YYYY-MM-DD
        release_date = f'{release_date[:4]}-{release_date[4:6]}-{release_date[6:8]}'
        cover_art = soup.find(class_="popupImage").img['src']

        self.release_meta = AlbumMetaData(
            artist,
            album,
            release_date,
            cover_art,
            self.url)
        return self.release_meta

    def parse_tracks(self, soup: BeautifulSoup):

        def cook_text(text_list_raw):
            return list(map(lambda x: x.text, text_list_raw))

        track_table = soup.find(id="track_table")
        track_numbers_raw = track_table.find_all(
            class_="track_number secondaryText")
        track_names_raw = track_table.find_all(itemprop="name")
        track_durations_raw = track_table.find_all(class_="time secondaryText")

        track_numbers = cook_text(track_numbers_raw)
        track_names = cook_text(track_names_raw)
        track_durations = list(
            map(lambda x: x.text.strip(' \n '), track_durations_raw))

        for track in track_numbers:
            i = track_numbers.index(track)
            self.release_tracks.push(AlbumTrack(
                track, track_names[i], track_durations[i]))

    def to_dict(self):
        print(self.release_meta)
        print(self.release_meta)
        print(self.release_meta)
        print(self.release_meta)
        return {
            "meta": self.release_meta,
            "tracks": self.release_tracks,
        }
