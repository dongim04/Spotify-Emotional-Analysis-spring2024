"""
Get emotion analysis results for each user based on the lyrics of their top
tracks using IBM Watson NLP API.
"""

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import (
    EmotionOptions,
    Features,
)
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from api_keys import IBM_API_KEY, IBM_URL

authenticator = IAMAuthenticator(IBM_API_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version="2022-04-07", authenticator=authenticator
)


# would run four times for each class year
def emotion_analysis(dictionary):
    """
    Run emotional analysis on a dictionary of users' top songs' lyrics.

    Each user will have an overall score for each of the five emotions
    (sadness, joy, fear, disgust, and anger). Assumes the lyrics are in
    English or have been translated into English.

    Args:
        dictionary (dict): A dictionary of strings that represents a user with
            a list storing their top songs' lyrics in English.

    Returns:
        user_scores (dict): A dictionary of users and their aggregated song
            emotion scores. The key is a string of the username, and the value
            is a dictionary of emotions to the aggregated scores.

    """
    natural_language_understanding.set_service_url(IBM_URL)

    user_scores = {}

    for user, songs in dictionary.items():
        overall_emotions = {
            "sadness": 0,
            "joy": 0,
            "fear": 0,
            "disgust": 0,
            "anger": 0,
        }

        for song in songs:
            if song is None:
                continue
            lyrics_to_analyze = song

            # analyze emotion in text
            response = natural_language_understanding.analyze(
                text=lyrics_to_analyze,
                features=Features(emotion=EmotionOptions()),
            ).get_result()

            # extract emotion scores
            emotions = response["emotion"]["document"]["emotion"]

            # adding up emotion for each song
            for emotion, score in overall_emotions.items():
                overall_emotions[emotion] = score + emotions[emotion]

        # assigning their overall emotion score to each user
        user_scores[user] = overall_emotions

    return user_scores
