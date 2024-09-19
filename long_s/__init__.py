import re
import unicodedata
from ._romance import french_conversion, italian_conversion, spanish_conversion
from ._germanic import english_conversion, german_conversion
from ._german_dicts import UNKNOWN_S


def convert(text: str, lang: str="en", keep_unknown_s: bool=False):
    """
    places the long s (ſ) in a sentence.

    params:
        text: the string to convert into archaeic spelling.
        lang: the language code for <text>. "en", "es", "fr", "it", or "de".
        keep_unknown_s: if True, ambiguous cases of S will be shown as X.

    returns:
        string: the given <text> with the long s (ſ) placed.
    """
    convert_func = None
    if lang == "en":
        convert_func = english_conversion
    elif lang == "es":
        convert_func = spanish_conversion
    elif lang == "fr":
        convert_func = french_conversion
    elif lang == "it":
        convert_func = italian_conversion
    elif lang == "de":
        convert_func = german_conversion

    if convert_func is None:
        print("language not found. the options are: en, es, fr, it, de.")
        return text

    results = _split_string_with_indices(text, lang)
    for i, old_word in results:
        new_word, replacement_made, use_fancy_replace = convert_func(old_word)

        if not replacement_made:
            continue

        if not use_fancy_replace:
            text = text[:i] + new_word + text[i + len(new_word):]
        else:
            if not keep_unknown_s:
                new_word = new_word.replace(UNKNOWN_S, "ſ") # defaults to long s

            for j in range(len(new_word)):
                if text[i + j] == "s":
                    text = text[: i + j] + new_word[j] + text[i + j + 1 :]

    return text


def _split_string_with_indices(input_string: str, lang: str):
    """
    splits the input string into words and returns their starting indices. 
    the function also considers language-specific rules for word splitting.
    
    params:
    - input_string: the string to be split.
    - lang: the language code (e.g., "de" for German) to handle specific rules.

    returns:
    - a list of tuples where each tuple contains the start index
      and the word itself.
    """
    APOSTROPHES = "'"
    matches = re.finditer(r"\S+", input_string)
    results = []
    for match in matches:
        index = match.start()
        word = match.group()

        local_start_index = 0
        for i in range(len(word)):
            if _is_letter(word[i]):
                local_start_index = i
                break
        else:
            continue

        local_end_index = len(word) - 1
        if lang == "de":
            for i in range(len(word) - 1, -1, -1):
                if _is_letter(word[i]) or word[i] in APOSTROPHES:
                    local_end_index = i
                    break
            else:
                continue
        else:
            for i in range(len(word) - 1, -1, -1):
                if _is_letter(word[i]):
                    local_end_index = i
                    break
            else:
                continue

        index += local_start_index
        word = word[local_start_index : local_end_index + 1]
        results.append((index, word))

    return results


def _is_letter(char: str):
    """returns True if the given <char> is some letter."""
    category = unicodedata.category(char)
    return category.startswith("L")
