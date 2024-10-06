"""
Filename: test_conversion_func.py
Description: This file contains a function to verify that
             the conversion functions for each language are working properly.

Author: TravisGK
Version: 1.0

License: MIT License
"""

import long_s

from test_spellings import TEST_SPELLINGS

_LANG_NAMES = {
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
}


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
    spellings = TEST_SPELLINGS[lang]
    conversion_func = long_s.get_conversion_func(lang)
    mismatches = []
    for expected_output in spellings:
        input_text = expected_output.replace("ſ", "s")
        actual_output = conversion_func(input_text)
        if expected_output != actual_output:
            # outputs to the user any mismatch.
            mismatches.append((input_text, actual_output, expected_output))

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
