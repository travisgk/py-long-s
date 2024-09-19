import itertools
import re
from unidecode import unidecode
from ._german_dicts import *


def english_conversion(text: str):
    """
    returns english text with the short S placed.

    returns:
        string: the converted <text>.
        bool: if any replacement is made.
        bool: if any fancy in-place replacements are needed.
    """
    ROUND_S_BEFORE_BK = False  # True in 17th and early 18th century
    if ROUND_S_BEFORE_BK:
        # selects every S that has a letter after it,
        # so long as that letter is not B nor K.
        pattern = r"s(?=[a-ac-jm-zA-AC-JM-Z])"
    else:
        # selects every S that has any letter after it.
        pattern = r"s(?=[a-zA-Z])"

    indices = [m.start() for m in re.finditer(pattern, text)]

    # excludes any S that comes before or after the letter F.
    pattern = r"s(?=f|F)|(?<=f|F)s"
    excluded_indices = [m.start() for m in re.finditer(pattern, text)]
    indices = [i for i in indices if i not in excluded_indices]
    for i in indices:
        text = text[:i] + "ſ" + text[i + 1 :]

    # replaces any occurrence of "ſſſ" with "ſsſ".
    pattern = r"ſſſ"
    indices = [m.start() for m in re.finditer(pattern, text)]
    for i in indices:
        text = text[:i] + "ſsſ" + text[i + 3 :]

    return text, True, True


_SHOW_DEBUG = False
_debug_str = ""


def print_debug_str():
    print(_debug_str)


def german_conversion(text: str):
    """
    returns german text with the short S placed.

    returns:
    - string: the converted <text>.
    - bool: if any replacement is made.
    - bool: if any fancy in-place replacements are needed 
            (to preserve punctuation in original text).
    """
    global _debug_str
    _debug_str = ""
    DEFAULT_UNKNOWNS_TO_LONG_S = False # if False, UNKNOWN_S char may appear.
    SHORT_S_ALWAYS_BEFORE_Z = False  # False after 1901.
    process_dicts()

    if "s" not in text[1:-2]:
        # if there are no occurrences of S besides 
        # the very start and the last two letters,
        # then the program doesn't need to do complicated searching and replacing.
        replacement_made = False
        if text.startswith("s"):
            # an S at the start is always long.
            text = "ſ" + text[1:]
            replacement_made = True
        if text[-2] == "s":
            # an S that's the penultimate letter is always long (uncertain).
            text = text[:-2] + "ſ" + text[-1]
            replacement_made = True
        
        return text, replacement_made, False # no fancy in-place replacements are needed.

    clean_text = text.lower()
    clean_text = clean_text.replace("s", UNKNOWN_S)

    # if "s" if the first letter of the word, it will be long.
    if clean_text[0] == UNKNOWN_S:
        clean_text = "ſ" + clean_text[1:]

    # 1) any unknown S that comes before many certain consonants becomes a short S.
    if SHORT_S_ALWAYS_BEFORE_Z:
        pattern = f"{UNKNOWN_S}(?=[aäceikoöp{UNKNOWN_S}tuüyAÄCEIKOÖPTUÜY])"
    else:
        pattern = f"{UNKNOWN_S}(?=[aäceikoöp{UNKNOWN_S}tuüyzAÄCEIKOÖPTUÜYZ])"

    # determines which indices of the string contain a letter S 
    # whose long/short status remains unknown.
    uncertain_indices = [m.start() for m in re.finditer(pattern, clean_text)]
    short_s_indices = [
        i
        for i, char in enumerate(clean_text)
        if char == UNKNOWN_S and i not in uncertain_indices
    ]
    for i in short_s_indices:
        clean_text = clean_text[:i] + "s" + clean_text[i + 1 :]

    # particular patterns with double S can now be filled in.
    clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
    clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # 2) runs through the primary replacements.
    if _SHOW_DEBUG:
        _debug_str += f"\n\n\ndoing main replacements: {clean_text}\n"
    for key, replacement in get_main_replacements().items():
        if UNKNOWN_S not in clean_text: # no more unknowns; for loop is broken.
            break
        clean_text, made_replacement = _smart_replace(clean_text, key, replacement)
        if made_replacement: # patterns with double S can now be filled in.
            clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
            clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # 3) handles particular end replacements.
    if clean_text[-1] in [UNKNOWN_S, "ſ"]: # an S at the end is always short.
        clean_text = clean_text[:-1] + "s"

    if text.endswith("sses"):
        clean_text, _ = _smart_replace(
            clean_text,
            "sses",
            "ſſes",
            restrict_to_end=True,
        )
    elif text.endswith("ses"):
        clean_text, _ = _smart_replace(
            clean_text,
            "ses",
            "ſes",
            restrict_to_end=True,
        )
    elif clean_text[:-1].endswith(f"{UNKNOWN_S}ch"):
        clean_text = clean_text[:-4] + "ſch" + clean_text[-1]
    elif clean_text[:-1].endswith(f"{UNKNOWN_S}{UNKNOWN_S}"):
        clean_text = clean_text[:-3] + "ſſ" + clean_text[-1]

    # particular patterns with double S can now be filled in.
    clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
    clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # 4) runs through the end replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing end replacements: {clean_text}\n"

    # since the end replacements are broken into subdictionaries,
    # the program must select which of these subdictionaries to use.
    # the last three letters of the word are used to index these dictionaries,
    # so the program now finds the dictionary of end replacements to use.
    replacements_dict = None
    if len(clean_text) >= 3:
        end_snippet = clean_text[-3:]
        end_snippet = end_snippet.replace("s", UNKNOWN_S)
        end_snippet = end_snippet.replace("ſ", UNKNOWN_S)
        replacements_dict = get_end_replacements()[0].get(end_snippet)

    if replacements_dict is None and len(clean_text) >= 2:
        end_snippet = clean_text[-2:]
        end_snippet = end_snippet.replace("s", UNKNOWN_S)
        end_snippet = end_snippet.replace("ſ", UNKNOWN_S)
        replacements_dict = get_end_replacements()[1].get(end_snippet)

    if replacements_dict is None:
        end_snippet = clean_text[-1]
        end_snippet = end_snippet.replace("s", UNKNOWN_S)
        end_snippet = end_snippet.replace("ſ", UNKNOWN_S)
        replacements_dict = get_end_replacements()[2].get(end_snippet)

    # an indexed subdictionary was found,
    # so its used to apply replacements to the text.
    if replacements_dict is not None:
        for key, replacement in replacements_dict.items():
            clean_text, made_replacement = _smart_replace(
                clean_text,
                key,
                replacement,
                restrict_to_end=True,
                forces_replacement=True,
            )
            if made_replacement:
                break

    # particular patterns with double S can now be filled in.
    clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
    clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # 5) runs through the start replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing start replacements: {clean_text}\n"
    
    # the subdictionaries for start replacements 
    # are indexed by the word's first letter, so that dictionary is found.
    indexing_letter = clean_text[0]
    start_pattern_dict = get_start_replacements().get(indexing_letter)
    
    # an indexed subdictionary was found,
    # so its used to apply replacements to the text.
    if start_pattern_dict is not None:
        for key, replacement in start_pattern_dict.items():
            if UNKNOWN_S not in clean_text:
                break  # i think this is okay
            clean_text, made_replacement = _smart_replace(
                clean_text, key, replacement, restrict_to_start=True
            )
            if made_replacement:
                break
        
        # particular patterns with double S can now be filled in.
        clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
        clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # 6) runs through the post-process replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing post-process replacements: {clean_text}\n"
    for key, replacement in get_post_process_replacements().items():
        clean_text, made_replacement = _smart_replace(
            clean_text, key, replacement, forces_replacement=True
        )
        if made_replacement:
            break

    # 7) runs through the final replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing final replacements: {clean_text}"
    for key, replacement in get_final_replacements().items():
        clean_text, made_replacement = _smart_replace(clean_text, key, replacement)

    # 8) cleans up ambiguous cases.
    if DEFAULT_UNKNOWNS_TO_LONG_S:
        clean_text = clean_text.replace(UNKNOWN_S, "ſ")

    return clean_text, True, True # fancy in-place replacements are needed.


def _smart_replace(
    text: str,
    search_term: str,
    replacement: str,
    restrict_to_start: bool=False,
    restrict_to_end: bool=False,
    forces_replacement: bool=False,
):
    """
    searches the given <text> for the <search_term> 
    and replaces it with <replacement>. this function, however,
    can take the <search_term> and generate all combinations of
    the letter S being changed out with "s" or "ſ".

    params:

    """
    global _debug_str
    made_replacement = False

    if len(search_term) > len(text):
        return text, made_replacement

    # locates the position of every letter S in the <replacement> term.
    search_chars = "sſ" if not forces_replacement else f"sſ{UNKNOWN_S}"
    s_indices = [i for i, char in enumerate(replacement) if char in search_chars]
    n_unknowns = len(s_indices)
    if n_unknowns == 0:
        return text, made_replacement

    # the replacement term is taken
    # and every possible combination of
    # switching out every possible letter S is generated.
    # each combination will be a list of values
    # that each correspond to the <s_indices>.
    if not forces_replacement:
        # only combos with at least one UNKNOWN_S are used.
        combinations = itertools.product([True, False], repeat=n_unknowns)
        combinations = [c for c in combinations if any(c)]
    else:
        combinations = itertools.product(f"sſ{UNKNOWN_S}", repeat=n_unknowns)

    # a search term is generated to correspond to every resulting combination list.
    keys = []
    for combo in combinations:
        new_string = list(replacement)
        for i, make_unknown in zip(s_indices, combo):
            if forces_replacement:
                new_string[i] = make_unknown
            elif make_unknown:
                new_string[i] = UNKNOWN_S
        keys.append("".join(new_string))

    if not restrict_to_start and not restrict_to_end:
        for key in keys:
            show_debug = _SHOW_DEBUG and key in text
            if show_debug:
                _debug_str += f"{text} -> {key} -> {replacement}\n"
            text = text.replace(key, replacement)

    elif restrict_to_start:
        for key in keys:
            if text.startswith(key):
                show_debug = _SHOW_DEBUG and key in text
                if show_debug:
                    _debug_str += f"{text} -> {key} -> {replacement}\n"
                text = replacement + text[len(key) :]
                made_replacement = True
                break
    else:
        for key in keys:
            if text.endswith(key):
                show_debug = _SHOW_DEBUG and key in text
                if show_debug:
                    _debug_str += f"{text} -> {key} -> {replacement}\n"
                text = text[: -len(key)] + replacement
                made_replacement = True
                break

    return text, made_replacement
