"""
Translate lyrics to English using Google Translate API.
"""

import concurrent.futures
import os
import re
import html
import urllib.parse
import sys
import requests


class EasyGoogleTranslate:
    """
    Unofficial Google Translate API.

    This library does not need an api key or something else to use, it's free
    and simple. You can either use a string or a file to translate but the text
    must be equal to or less than 5000 character. You can split your text into
    5000 characters to translate more.

    Google Translate supports 108 different languages. You can use any of them
    as source and target language in this application. If source language is
    not specified, it will detect source language automatically. This
    application supports multi thread translation, you can use it to translate
    multiple languages at once. Detailed language list can be found here:
    https://cloud.google.com/translate/docs/languages
    """

    def __init__(self, source_language="auto", target_language="tr", timeout=5):
        """
        Initialize EasyGoogleTranslate object.

        Args:
            source_language (str): The source language to translate from.
                Defaults to "auto" (auto-detect).
            target_language (str): The target language to translate to.
                Defaults to "tr" (Turkish).
            timeout (int): Timeout for HTTP requests in seconds. Defaults to 5.

        """
        self.source_language = source_language
        self.target_language = target_language
        self.timeout = timeout
        self.pattern = r'(?s)class="(?:t0|result-container)">(.*?)<'

    def make_request(self, target_language, source_language, text, timeout):
        """
        Make a request to Google Translate API.

        Args:
            target_language (str): The target language to translate to.
            source_language (str): The source language to translate from.
            text (str): The text to be translated.
            timeout (int): Timeout for HTTP requests in seconds.

        Returns:
            str: Translated text.

        """
        escaped_text = urllib.parse.quote(text.encode("utf8"))
        url = (
            f"https://translate.google.com/m?tl={target_language}"
            f"&sl={source_language}&q={escaped_text}"
        )
        response = requests.get(url, timeout=timeout)
        result = response.text.encode("utf8").decode("utf8")
        result = re.findall(self.pattern, result)
        if not result:
            print("\nError: Unknown error.")
            with open("error.txt", encoding="utf-8") as file:
                file.write(response.text)
            sys.exit(0)
        return html.unescape(result[0])

    def translate(
        self, text, target_language="", source_language="", timeout=""
    ):
        """
        Translate text to the specified target language.

        Args:
            text (str): The text to be translated.
            target_language (str or list of str): The target language(s) to
                translate to.
            source_language (str): The source language to translate from.
            timeout (int): Timeout for HTTP requests in seconds.

        Returns:
            str or list of str: Translated text.

        """
        if not target_language:
            target_language = self.target_language
        if not source_language:
            source_language = self.source_language
        if not timeout:
            timeout = self.timeout
        # if the text is None, return None
        if text is None:
            return text
        # if the text length is over 5000, cut it down to 5000
        if len(text) > 5000:
            text = text[:5000]
        if isinstance(target_language, list):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(
                        self.make_request,
                        target,
                        source_language,
                        text,
                        timeout,
                    )
                    for target in target_language
                ]
                return_value = [f.result() for f in futures]
                return return_value
        return self.make_request(
            target_language, source_language, text, timeout
        )

    def translate_file(
        self, file_path, target_language="", source_language="", timeout=""
    ):
        """
        Translate text from a file to the specified target language.

        Args:
            file_path (str): The path to the file to be translated.
            target_language (str or list of str): The target language(s) to
                translate to.
            source_language (str): The source language to translate from.
            timeout (int): Timeout for HTTP requests in seconds.

        Returns:
            str or list of str: Translated text.

        """
        if not os.path.isfile(file_path):
            print("\nError: The file or path is incorrect.")
            sys.exit(0)
        with open(file_path, encoding="utf-8") as file:
            text = self.translate(
                file.read(), target_language, source_language, timeout
            )
        return text


def get_translate(dictionary_year):
    """
    Translate lyrics in multiple languages.

    Args:
        dictionary_year (dict): A dictionary containing usernames as keys and
            lyrics as values.

    """
    for username in dictionary_year.keys():
        for i, lyric in enumerate(dictionary_year[username]):
            result = EasyGoogleTranslate().translate(
                lyric, target_language="en"  # set target language to English
            )
            dictionary_year[username][i] = result
