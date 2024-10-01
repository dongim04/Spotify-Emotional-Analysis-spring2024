"""
Check the correctness of the translated lyrics from the Google Translate API
"""

# Import all required libraries.
import pytest

# Import the functions
from google_translate import get_translate


@pytest.mark.parametrize(
    "untranslated,english",
    [
        # Test Spanish Translation
        (
            {
                "user1": [
                    "El sol brilla en un cielo azul despejado.",
                    "La vida es un viaje lleno de aventuras y desafíos.",
                ]
            },
            {
                "user1": [
                    "The sun shines in a clear blue sky.",
                    "Life is a journey full of adventures and challenges.",
                ]
            },
        ),
        # Test Chinese Translation
        (
            {
                "user2": [
                    "春天来了，万物复苏，大地充满了生机。",
                    "家人是我们生命中最珍贵的财富。",
                ]
            },
            {
                "user2": [
                    (
                        "Spring is here, everything revives, and the earth is"
                        " full of life."
                    ),
                    "Family is the most precious treasure in our lives.",
                ]
            },
        ),
    ],
)
def test_get_translate(untranslated, english):
    """
    Check that the translation from any language is able
    to translate to English.

    Args:
        untranslated: A  dictionary of a list of lyrics in other languages
            mapped to users.
        english: A dictionary of a list of english lyrics mapped to users.

    """
    get_translate(untranslated)

    assert untranslated == english
