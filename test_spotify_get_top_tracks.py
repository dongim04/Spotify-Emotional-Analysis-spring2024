"""
Check the correctness of the get top tracks function with Spotify API.
"""

# Import all required libraries.
import pytest

# Import the functions
from spotify_get_top_tracks import get_top_tracks


# Test Cases for first_number_index


@pytest.mark.parametrize(
    "usernames,num,tuple_list",
    [
        # Check that a list of two usernames will output
        # the correct top 10 tracks
        (
            ["1223105593", "ishaano"],
            10,
            [
                (
                    ("Twenty One Pilots", "Overcompensate"),
                    ("Hozier", "De Selby (Part 2)"),
                    ("Molchat Doma", "Судно (Борис Рижий)"),
                    ("Scizzie", "aquatic ambience"),
                    ("Jungle", "Dominoes"),
                    ("Jungle", "Candle Flame"),
                    (
                        "Twenty One Pilots",
                        "Lane Boy / Redecorate / Chlorine - Livestream Version",
                    ),
                    ("Childish Gambino", "I. Flight of the Navigator"),
                    ("The Clash", "London Calling - Remastered"),
                    ("阿保剛", "LEASE"),
                ),
                (
                    (
                        "Portugal. The Man",
                        "Summer of Luv (feat. Unknown Mortal Orchestra)",
                    ),
                    ("Portugal. The Man", "Guns and Dogs"),
                    ("Milky Chance", "Living In A Haze"),
                    ("Pink Floyd", "Pigs (Three Different Ones)"),
                    ("Metallica", "For Whom The Bell Tolls (Remastered)"),
                    ("Portugal. The Man", "Atomic Man"),
                    ("Fleetwood Mac", "You Make Loving Fun - 2004 Remaster"),
                    ("Portugal. The Man", "Feel It Still"),
                    ("Portugal. The Man", "Creep in a T-Shirt"),
                    ("Portugal. The Man", "Purple Yellow Red and Blue"),
                ),
            ],
        ),
        # Check that a list of two usernames will output
        # the correct top 2 tracks
        (
            ["1223105593", "ishaano"],
            2,
            [
                (
                    ("Twenty One Pilots", "Overcompensate"),
                    ("Hozier", "De Selby (Part 2)"),
                ),
                (
                    (
                        "Portugal. The Man",
                        "Summer of Luv (feat. Unknown Mortal Orchestra)",
                    ),
                    ("Portugal. The Man", "Guns and Dogs"),
                ),
            ],
        ),
    ],
)
def test_get_top_tracks(usernames, num, tuple_list):
    """
    Check that list of usernames and num of songs will output
    the correct list of top num tracks.

    Args:
        usernames: A list of strings representing spotify usernames.
        num: An int representing the amount of top tracks to get.
        tuple_list: A list of tuples representing a user's top tracks
            in (artist, song) format.

    """
    assert get_top_tracks(usernames, num) == tuple_list
