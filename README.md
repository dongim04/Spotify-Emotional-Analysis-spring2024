# Midterm Project: Oliners Spotify Emotional Insights

At Olin College, our community is uniquely united in the sense that students here move through shared classes and college experiences. For instance, a first-year agonizing over their Design Nature hopper project could approach nearly any upperclassman and be regaled with stories, accompanied with varying fondness levels, of their own experience with the project and how first years have it easier. Similarly, it seems to be widely agreed upon that sophomore year is academically the most stressful year here, due to the combination of classes and the way responsibilities tend to pile on them.

Now we take a brief turn to thinking about music, specifically the theory that the music we listen to reflects something about ourselves and our emotional states. It’s both fun and interesting to think about–Spotify, one of the most popular music streaming services, has capitalized on this through features like their “daylist”, which gives premium users a daily updating playlist with titles, based on their music taste, such as “energizing pumped wednesday morning” or “shy kitsch tuesday afternoon”.

After considering these ideas, the possible patterns of Olin years as well as music listening history reflecting emotional states, we decided to explore the combination of them to answer the question:

**How do the emotional states of the four current Olin College class years compare to each other through the lyric sentiment of their top Spotify tracks?**

Our project runs emotional sentiment analysis on the lyrics of the current top tracks of our college classmates, where we collected this data, processed it, and analyzed it to see if there were trends in the emotional states across the four class years (2027, 2026, 2025, 2024).

## Setup

The `requirements.txt` file is blank and should be filled out with any project
dependencies. There is a Python package called `pipreqs` that autogenerates the
contents of the `requirements.txt` file based on the `import` statements in your
`.py` files. To get this, run

```
pip install pipreqs
```

The README provides instructions for how to generate plots similar or identical to those shown in the project computational essay.
OR to manually install each API packages,

To get the top tracks from the [Spotify API](https://developer.spotify.com/), run

```
pip install spotipy
```

To get the lyrics from any song from the [Genius API](https://lyricsgenius.readthedocs.io/), run

```
pip install lyricsgenius
```

To run a sentiment analysis on a set of lyrics from the [IBM Watson API](https://cloud.ibm.com/docs/natural-language-understanding), run

```
pip install ibm-watson
pip install --upgrade "ibm-watson>=6.1.0"
```


## Usage

### Changes To Code
For the code to run successfully, make sure to have your own API keys in your local repo.

When getting a user's top tracks, the function `get_top_tracks` allows you to adjust the number of data points you want to include in your research. In this project, we took the 10 top tracks from each user. Additionally, change the name of the playlist you wish to search for if not using Replayify.com to generate public playlists of current top tracks. We used "Replay Top-50 Tracks" as the playlist to generate top tracks from.

### Data
To run the code with your own set of data, collect users' Spotify usernames. Download these Spotify usernames into a CSV file. The Spotify API only allows you access to their public playlist if you have the title of it. With the Genius API, the project only focused on the lyrics, however there are many other accessible data points to answer a research question. Run the `data_processing.ipynb` notebook in order to process your data, which should output in the form of a JSON file with a list of averaged emotional scores for each class year. Ideally, run this notebook first before running any unit tests, as it will give warnings about cache data that would be generated from the notebook.

### Generating Plots
To generate the visualizations of our gathered data, run the cells under Results in the `computational_essay_olin_spotify_emotional_insights.ipynb` notebook. The first cell organizes the collected data into a Python list for our 3 visualizations.

1. **Pie Chart. (4 Classes)**  Shows the percentage of emotional spread of people within a class.
2. **Stacked Bar Chart.** Compares the emotional states across all the classes.
3. **Heatmap.** Combines all the scores of users in a class and shows the percentage of each emotional state.
