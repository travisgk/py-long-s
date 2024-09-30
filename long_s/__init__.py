"""
long-s
# pip install unidecode

Filename: __init__.py
Description: long-s is a tool that takes modern text and 
             inserts the archaic letter of the long S (ſ) where it fits.

Author: TravisGK
Version: 1.0

License: MIT License
"""

import re
from ._split_words import *
from ._simple_conversions import *
from ._german_conversion import convert_german_word

def get_conversion_func(lang: str):
    """Returns the conversion function used for a particular language."""
    if lang == "en":
        return convert_english_word
    elif lang == "fr":
        return convert_french_word
    elif lang == "de":
        return convert_german_word
    elif lang == "es":
        return convert_spanish_word
    elif lang == "it":
        return convert_italian_word
    return None


def convert(text: str, lang: str="en", keep_unknown_s: bool=False):
    """
    Places the long s (ſ) in a sentence and returns it.

    Parameters:
    text (str): the string to convert into archaeic spelling.
    lang (str): the language code for <text>. "en", "es", "fr", "it", or "de".
    keep_unknown_s (bool): if True, ambiguous cases of S will be shown as X.

    Returns:
    str: text with the long s (ſ) placed.
    """
    convert_func = get_conversion_func(lang)

    if convert_func is None:
        print(
            f"language \"{lang}\" not found."
            "the options are: en, es, fr, it, de."
        )
        return text

    # converts each word individually.
    words = split_words_with_indices(text, lang)
    for old_word, start_index in words:
        new_word = convert_func(old_word)
        
        if old_word == new_word:
            continue # no replacements were made.

        # overwrite the original occurrences of S.
        for j in range(len(new_word)):
            clip = start_index + j
            if text[clip] == "s":
                text = text[: clip] + new_word[j] + text[clip + 1 :]

    return text
