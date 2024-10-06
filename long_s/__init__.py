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

import multiprocessing
import os
import re
from functools import partial
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


def _process_chunk(chunk, convert_func, lang: str = "de"):
    """
    Returns a dict of every word contained in the given chunk after being converted.
    """
    return {key: convert_func(value) for key, value in chunk.items()}


def convert_text_file(
    in_file_path: str,
    out_file_path: str = None,
    lang: str = "en",
    keep_unknown_s: bool = False,
):
    """
    Loads a text file, converts all the text to use the long S,
    then saves it to an output text file.

    Parameters:
    in_file_path (string): path of the source text file.
    out_file_path (string): path of the destination text file.
    lang (string): the language code for the text.
    keep_unknown_s (bool): if True, ambiguous cases of S
                           will remain explicitly marked.
    """
    if not os.path.isfile(in_file_path):
        return

    with open(in_file_path, "r", encoding="utf-8") as input_file:
        content = input_file.read()
        results = convert(content, lang, keep_unknown_s)

    if out_file_path is None:
        out_file_path = in_file_path[:-4] + "-long-s.txt"
    with open(out_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(results)


def convert(text: str, lang: str = "en", keep_unknown_s: bool = False):
    """
    Places the long s (ſ) in a sentence and returns it.

    Parameters:
    text (str): the string to convert into archaeic spelling.
    lang (str): the language code for <text>. "en", "es", "fr", "it", or "de".
    keep_unknown_s (bool): if True, ambiguous cases of S
                           will remain explicitly marked.

    Returns:
    str: text with the long s (ſ) placed.
    """
    CHUNK_SIZE = 30
    MULTIPROCESS_THRESHOLD = 100  # wordcount that triggers multiprocessing.

    convert_func = get_conversion_func(lang)

    if convert_func is None:
        print(f'language "{lang}" not found.' "the options are: en, fr, de, es, it.")
        return text

    words_with_indices = split_words_with_indices(text, lang)

    if len(words_with_indices) > MULTIPROCESS_THRESHOLD:
        # uses multiprocessing to convert massive amounts of words.
        non_words = {}
        next_new_index = 0
        for old_word, start_index in words_with_indices:
            if next_new_index != start_index:
                non_words[next_new_index] = text[next_new_index:start_index]
                next_new_index = start_index
            next_new_index = start_index + len(old_word)

        if next_new_index < len(text):
            non_words[next_new_index] = text[next_new_index:]

        # breaks all the words to be converted into dictionary chunks.
        chunks = []
        for i in range(0, len(words_with_indices), CHUNK_SIZE):
            chunks.append({})
            for j in range(i, min(len(words_with_indices), i + CHUNK_SIZE)):
                old_word, start_index = words_with_indices[j]
                chunks[-1][start_index] = old_word
        last_used_index = (len(words_with_indices) // CHUNK_SIZE) * CHUNK_SIZE

        # converts every chunk using multiprocessing.
        process_func = partial(_process_chunk, convert_func=convert_func, lang=lang)
        with multiprocessing.Pool() as pool:
            results = pool.map(process_func, chunks)

        # combines all the results.
        combined_result = {k: v for r in results for k, v in r.items()}
        for key, value in non_words.items():
            combined_result[key] = value

        mapped_list = sorted(combined_result.items())
        text = "".join(substr for _, substr in mapped_list)

        return text

    else:
        # uses one thread to directly convert some words.
        # converts each word individually.
        words = split_words_with_indices(text, lang)
        for old_word, start_index in words:
            new_word = convert_func(old_word)

            if old_word == new_word:
                continue  # no replacements were made.

            # overwrite the original occurrences of S.
            for j in range(len(new_word)):
                clip = start_index + j
                if text[clip] == "s":
                    text = text[:clip] + new_word[j] + text[clip + 1 :]

        return text
