import re
import unicodedata
from ._romance import french_conversion, italian_conversion, spanish_conversion
from ._germanic import english_conversion, german_conversion


def convert(text, lang="en"):
    convert_func = None
    if lang == "en":
        convert_func = english_conversion
    elif lang == "fr":
        convert_func = french_conversion
    elif lang == "it":
        convert_func = italian_conversion
    elif lang == "es":
        convert_func = spanish_conversion
    elif lang == "de":
        convert_func = german_conversion

    if convert_func is None:
        print("language not found. the options are: en, fr, it, es, de.")
        return text

    results = _split_string_with_indices(text, lang)
    for i, old_word in results:
        new_word = convert_func(old_word)
        for j in range(len(new_word)):
            if text[i + j] == "s":
                text = text[: i + j] + new_word[j] + text[i + j + 1 :]

    return text


_APOSTROPHES = "'"


def _split_string_with_indices(input_string, lang):
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
                if _is_letter(word[i]) or word[i] in _APOSTROPHES:
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

        # print(word)
        results.append((index, word))
    # results = [(match.start(), match.group()) for match in matches]

    return results


def _is_letter(char):
    category = unicodedata.category(char)
    return category.startswith("L")
