import time
import long_s
from test_conversion_func import *


def main():
    # prints out sample sentences for each language.
    print("\n", end="")
    sentences = [
        ("en", "The discussion was surprisingly insightful."),
        ("fr", "La discussion était étonnamment perspicace."),
        ("de", "Die Diskussion war überraschend aufschlussreich."),
        ("es", "La discusión fue sorprendentemente perspicaz."),
        ("it", "La discussione è stata sorprendentemente perspicace."),
    ]

    for lang, sentence in sentences:
        result = long_s.convert(sentence, lang=lang)
        print(result)

    # tests every supported language.
    start_time = time.time()
    print("\n", end="")
    test_conversion_func(lang=None)
    elapsed = time.time() - start_time
    print(f"\n{elapsed:.2f} seconds")

    long_s.convert_text_file("smut.txt", lang="de")


if __name__ == "__main__":
    main()
