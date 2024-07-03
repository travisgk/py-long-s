import itertools
import re
from unidecode import unidecode
from ._german_dicts import *

def english_conversion(text):
    ROUND_S_BEFORE_BK = False # True in 17th and early 18th century
    
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
        text = text[:i] + "ſ" + text[i + 1: ]

    # replaces any occurrence of "ſſſ" with "ſsſ".
    pattern = r"ſſſ"
    indices = [m.start() for m in re.finditer(pattern, text)]
    for i in indices:
        text = text[:i] + "ſsſ" + text[i + 3: ]

    return text

_SHOW_DEBUG = False
_debug_str = ""

def print_debug_str():
    print(_debug_str)

def german_conversion(text):
    global _debug_str
    _debug_str = ""
    SHORT_S_ALWAYS_BEFORE_Z = False # False after 1901.
    process_dicts()
    
    clean_text = text.lower()
    if "s" not in clean_text:
        return clean_text

    clean_text = clean_text.replace("s", UNKNOWN_S)
    
    # if "s" if the first letter of the word, it will be long.
    if clean_text[0] == UNKNOWN_S:
        clean_text = "ſ" + clean_text[1:]

    # any unknown S that comes before many consonants becomes a short S.
    if SHORT_S_ALWAYS_BEFORE_Z:
        pattern = f"{UNKNOWN_S}(?=[aäceikoöp{UNKNOWN_S}tuüyAÄCEIKOÖPTUÜY])"
    else:
        pattern = f"{UNKNOWN_S}(?=[aäceikoöp{UNKNOWN_S}tuüyzAÄCEIKOÖPTUÜYZ])"

    uncertain_indices = [m.start() for m in re.finditer(pattern, clean_text)]
    short_s_indices = [
        i for i, char in enumerate(clean_text)
        if char == UNKNOWN_S and i not in uncertain_indices
    ]
    for i in short_s_indices:
        clean_text = clean_text[:i] + "s" + clean_text[i + 1: ]

    clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
    clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # runs through the primary replacements.
    if _SHOW_DEBUG:
        _debug_str += f"\n\n\ndoing main replacements: {clean_text}\n"
    for key, replacement in get_main_replacements().items():
        if UNKNOWN_S not in clean_text:
            break
        clean_text, made_replacement = smart_replace(clean_text, key, replacement)
        if made_replacement:
            clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
            clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # handles particular end replacements.
    if clean_text[-1] in [UNKNOWN_S, "ſ"]:
        clean_text = clean_text[:-1] + "s"

    if text.endswith("sses"):
        clean_text, _ = smart_replace( # differs for noun
            clean_text,
            "sses",
            "ſſes",
            #"ſses" if text[0].isupper() else "ſſes",
            restrict_to_end=True,
        )
    elif text.endswith("ses"):
        clean_text, _ = smart_replace( # differs for noun
            clean_text,
            "ses",
            "ſes",
            #"ses" if text[0].isupper() else "ſes",
            restrict_to_end=True,
        )
    elif clean_text[:-1].endswith(f"{UNKNOWN_S}ch"):
        clean_text = clean_text[:-4] + "ſch" + clean_text[-1]
    elif clean_text[:-1].endswith(f"{UNKNOWN_S}{UNKNOWN_S}"):
        clean_text = clean_text[:-3] + "ſſ" + clean_text[-1]

    clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
    clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # runs through the end replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing end replacements: {clean_text}\n"

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

    if replacements_dict is not None:
        for key, replacement in replacements_dict.items():
            clean_text, made_replacement = smart_replace(
                clean_text, key,
                replacement,
                restrict_to_end=True,
                forces_replacement=True,
            )
            if made_replacement:
                break

    clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
    clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # runs through the start replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing start replacements: {clean_text}\n"
    indexing_letter = clean_text[0]
    start_pattern_dict = get_start_replacements().get(indexing_letter)
    if start_pattern_dict is not None:
        for key, replacement in start_pattern_dict.items():
            if UNKNOWN_S not in clean_text:
                break # i think this is okay
            clean_text, made_replacement = smart_replace(
                clean_text, key, replacement, restrict_to_start=True
            )
            if made_replacement:
                break
        clean_text = clean_text.replace(f"{UNKNOWN_S}s", "ſs")
        clean_text = clean_text.replace(f"s{UNKNOWN_S}", "sſ")

    # runs through the post-process replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing post-process replacements: {clean_text}\n"
    for key, replacement in get_post_process_replacements().items():
        clean_text, made_replacement = smart_replace(
            clean_text, key, replacement, forces_replacement=True
        )
        if made_replacement:
            break

    # runs through the final replacements.
    if _SHOW_DEBUG:
        _debug_str += f"doing final replacements: {clean_text}"
    for key, replacement in get_final_replacements().items():
        clean_text, made_replacement = smart_replace(
            clean_text, key, replacement,
        )

    return clean_text


def smart_replace(
    text,
    search_term,
    replacement,
    restrict_to_start=False,
    restrict_to_end=False,
    forces_replacement=False
):
    global _debug_str
    made_replacement = False

    if len(search_term) > len(text):
        return text, made_replacement

    # locates the position of every letter S in the <replacement> term.
    search_chars = "sſ" if not forces_replacement else f"sſ{UNKNOWN_S}"
    s_indices = [
        i for i, char
        in enumerate(replacement)
        if char in search_chars
    ]
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
                text = replacement + text[len(key):]
                made_replacement = True
                break
    else:
        for key in keys:
            if text.endswith(key):
                show_debug = _SHOW_DEBUG and key in text
                if show_debug:
                    _debug_str += f"{text} -> {key} -> {replacement}\n"
                text = text[:-len(key)] + replacement
                made_replacement = True
                break

    return text, made_replacement