import long_s
from test_conversion_func import *

def main():
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

    test_conversion_func(lang="de")

if __name__ == "__main__":
    main()