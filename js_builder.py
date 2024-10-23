"""
Filename: js_builder.py
Description: This file contains a function that will write
             a JavaScript file containing all the information of the
             processed German lists. This is for developer-use
             to update the JavaScript version of long-s.

Author: TravisGK
Version: 1.0

License: MIT License
"""

from long_s._german_lists import *


def get_json_contents(path: str):
    result = ""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line[0] in "{}[]":
                continue
            result += line
    return result


def build_js(version_str: str = "1.0"):
    paths = get_processed_file_paths()
    result = ""
    result += f"""/**
Filename: germanlists.js
Description: This contains spelling patterns of the long S 
             in the German language. These are used to fill in uncertainties.

Author: TravisGK
Version: {version_str}

License: MIT License
*/

/**
Step 1)
---
The program has the conversions of some commonly-used
words and names explicitly written in memory, 
so if the word is one of those,
the function will return that conversion immediately.

*/
const EXACT_MATCHES = {{
{get_json_contents(paths[0])}}}

// all of these names will take a long S in the middle.
const LONG_S_NAMES = {{
{get_json_contents(paths[1])}}}


/**
Step 2 includes some few exceptional spellings.
*/
const FORCED_OVERWRITES = [
{get_json_contents(paths[2])}]


/**
Step 3) 
---
This step uses the blueprint replace function to try to solve
any ambiguous S, but only for patterns
that occur at the end of words.

*/
const END_PATTERNS = {{
{get_json_contents(paths[3])}}}


/**
Step 4)
---
This step uses the crossword replace function to try to solve
any ambiguous S. A dictionary of spelling patterns that can occur
anywhere in the word are used to try to further solve the spelling.

*/
const OMNIPRESENT_PATTERNS = {{
{get_json_contents(paths[4])}}}


/**
Step 5)
---
This step uses the crossword replace function to try to solve
any ambiguous S, but only for patterns
that occur at the beginning of words.

*/
const START_PATTERNS = {{
{get_json_contents(paths[5])}}}


/**
Step 6)
---
This step runs postprocess replacements with the crossword search.

*/
const POSTPROCESS_PATTERNS = [
{get_json_contents(paths[6])}]
"""
    with open("germanlists.js", "w", encoding="utf-8") as file:
        file.write(result)
    print("done! the results were saved to germanlists.js\n")


if __name__ == "__main__":
    build_js(version_str="1.0.5")
