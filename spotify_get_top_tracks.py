"""
Get top tracks for each username using Spotify API.
"""

import spotipy
from spotipy import util
from api_keys import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_REDIRECT_URI,
)


def get_top_tracks(usernames, number):
    """
    Get the top n tracks for each specified username.

    Args:
        usernames (list of str): List of Spotify usernames for which to obtain
            top tracks.
        n (int): Number of top tracks to obtain.

    Returns:
        top_tracks (list): A list containing tuples of artist and track name
            pairs for each user.
            [((user1_artist1, user1_song1), (user1_artist2, user1_song2), ...),
             ((user2_artist1, user2_song1), (user2_artist2, user2_song2), ...),
             ...]
    """

    def show_tracks(tracks, number):
        """
        Extract artist and track names from Spotify API response.

        Args:
            tracks (dict): Response containing track information.
            n (int): Number of top tracks to extract.

        Returns:
            artist_track (tuple): A tuple containing artist and track name
                pairs.
                   Format: ((artist1, song1), (artist2, song2), ...)
        """
        artist_track = ()
        for i in range(number):
            item = tracks["items"][i]
            track = item["track"]
            artist_track = artist_track + (
                (track["artists"][0]["name"], track["name"]),
            )
        return artist_track

    top_tracks = []
    for username in usernames:
        token = util.prompt_for_user_token(
            username,
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
        )
        if token:
            spotify_response = spotipy.Spotify(auth=token)
            playlists = spotify_response.user_playlists(username)
            for playlist in playlists["items"]:
                name = playlist["name"]
                if (playlist["owner"]["id"] == username) & (
                    name[0:20] == "Replay Top-50 Tracks"
                ):
                    results = spotify_response.playlist(
                        playlist["id"], fields="tracks,next"
                    )
                    tracks = results["tracks"]
                    top_tracks.append(show_tracks(tracks, number))
                    break
        else:
            print("Can't get token for", username)
    return top_tracks
