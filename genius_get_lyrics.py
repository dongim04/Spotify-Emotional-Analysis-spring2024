"""
Get lyrics of top tracks using Genius API.
"""

import json
import re
import shutil
from lyricsgenius import Genius
from api_keys import GENIUS_TOKEN

genius = Genius(access_token=GENIUS_TOKEN, timeout=100)


def first_number_index(string):
    """
    Given a string, return the index of the first non-alphabet.

    Args:
        string (str): A string with a number in it.
    Returns:
        int: An int representing the index of the number.

    """
    # Regular expression to find the first digit
    # Search for the pattern in the string
    match = re.search(r"\d", string)
    if match:
        return match.start()
    # Return -1 if no number found
    return -1


def getlyrics(artist, song):
    """
    Given the artist and song, use the genius API to get lyrics.

    Args:
        artist (string): A string representing artist name.
        song (string): A string representing song title.

    Returns:
        final_lyrics (string): A string of the lyrics.

    """
    # remove section headers from lyrics
    genius.remove_section_headers = True
    genius.verbose = False

    song_name = ""
    for character in song:
        if character.isalnum():
            song_name = song_name + character

    artist_name = ""
    for character in artist:
        if character.isalnum():
            artist_name = artist_name + character

    # set file name to include artist and song
    file_name = "lyrics_" + artist_name + "_" + song_name

    # get track from genius
    track = genius.search_song(song, artist)

    # Define path name to save the JSON files
    track_path = "Lyric_Files/" + file_name + ".json"

    if track:
        # save track lyrics as json file
        track.save_lyrics(filename=file_name, overwrite=True)

        # move files to Lyric Files
        shutil.move(file_name + ".json", track_path)

        # get lyrics key from json dictionary
        with open(track_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Create list of lyrics excluding non-lyrics
        lyrics = data["lyrics"].split()

        # Find the start index in text_list where
        # the lyrics start
        start_index = 0
        for i, item in enumerate(lyrics):
            if item == "Lyrics":
                start_index = i + 1

        # Append all lyrics into a single string
        final_lyrics = ""
        for i in range(start_index, len(lyrics)):
            if i == len(lyrics) - 1:
                # take out the last bit of non-lyrics, then concatnate
                final_lyrics += lyrics[i][: first_number_index(lyrics[i])]
            else:
                final_lyrics += lyrics[i] + " "
        # return string of lyrics
        return final_lyrics
    return None


def get_lyrics_dictionary(usernames, top_tracks):
    """
    Given a nested list of username's top tracks in the (artist, song)
    format and a list of usernames. Output a dictionary of a user's
    top track lyrics mapped to their username.

    Args:
        usernames (list): A list of all usernames in a year.
        top_tracks (list): A list representing a year's username's top tracks.
            eg: [(("string1", "string2"), ("string3", "string4"))]

    Returns:
        dict_data (dictionary): A dictionary of a year, mapping username to
            list of lyrics of top songs.

    """
    dict_data = {}
    # loop through users' top tracks
    for i, item in enumerate(top_tracks):
        # initialize a temp list of lyrics for a user
        lyric_list = []
        for j in item:
            # call getlyrics and get artist and song
            lyric_list.append(getlyrics(j[0], j[1]))
        # map lyric list to username
        dict_data[usernames[i]] = lyric_list
    # return dictionary
    return dict_data
