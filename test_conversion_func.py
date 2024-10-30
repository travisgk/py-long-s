"""
Filename: test_conversion_func.py
Description: This file contains a function to verify that
             the conversion functions for each language are working properly.

Author: TravisGK
Version: 1.0.2

License: MIT License
"""

import json
import os
import long_s

_LANG_NAMES = {
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
}


def _get_local_file_dir():
    file_path = os.path.abspath(__file__)
    return os.path.dirname(file_path)


def test_conversion_func(lang: str = None):
    """
    Tests the conversion function and outputs to the user
    if any words fail to convert correctly.

    Parameters:
    lang (string): the language code. if None, then all languages are tested.
    """

    if lang is None:
        # runs tests for every language if a language isn't specified.
        for lang in ["en", "fr", "de", "es", "it"]:
            test_conversion_func(lang)
        return

    # tests each case in the list of spellings.
    if lang == "de":
        name = "test-spellings-de.json"
        path = os.path.join(_get_local_file_dir(), name)
        with open(path, "r", encoding="utf-8") as file:
            spellings = json.load(file)

        if long_s.using_developer_mode():
            long_s._german_lists.save_flattened_json(spellings, path)
            with open(path, "r", encoding="utf-8") as file:
                spellings = json.load(file)
    else:
        name = "test-spellings.json"
        path = os.path.join(_get_local_file_dir(), name)
        with open(path, "r", encoding="utf-8") as file:
            contents = json.load(file)
        spellings = contents[lang]

    # loads the test spellings into a single string split by spaces.
    # this allows for multiprocessing with the conversion.
    expected_str = "\n".join(spellings)
    test_str = expected_str.replace("ſ", "s")
    actual_str = long_s.convert(test_str, lang=lang)

    # splits the strings into lists of results.
    expected_list = expected_str.split("\n")
    test_list = test_str.split("\n")
    actual_list = actual_str.split("\n")

    # finds any mismatches.
    mismatches = []
    for expected, test, actual in zip(expected_list, test_list, actual_list):
        if expected != actual:
            # outputs to the user any mismatch.
            mismatches.append((test, actual, expected))

    # prints the results to the user.
    num_tests = len(spellings)
    lang_name = _LANG_NAMES[lang]

    num_mismatches = len(mismatches)
    if num_mismatches == 0:
        # notifies user of success if no errors arose.
        print(f"All {num_tests} tests were successful for {lang_name}.")
    else:
        # notifies the user of each failed test case.
        print("\n")
        print("-" * 79)
        print(
            f"{lang_name}:\n({num_mismatches}/{num_tests}) tests failed.\n"
            f"{'Input':<16}     {'Actual Output':>16}\t"
            f"|\t{'Expected Output':<16}"
        )
        print("-" * 79)
        for input_text, actual_output, expected_output in mismatches:
            print(
                f"{input_text:<16} --> {actual_output:>16}"
                f"\t|\t{expected_output:<16}"
            )
        print("-" * 79)
