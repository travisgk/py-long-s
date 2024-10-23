import long_s


def get_words_ending_with(ending: str):
    results = []
    with open("de_demo.txt", "r", encoding="utf-8") as file:
        for word in file:
            w = word.strip()
            contents = w.split()

            if len(contents) == 3:
                _, clean_word, _ = w.split()

                # ends with -sende... -sorte
                if clean_word.endswith(ending) and "-" not in clean_word:
                    result = long_s.strip_to_german_alphabet(clean_word)

                    if len(result) == len(clean_word):
                        results.append(result)

    return results


def main():
    long_s.enable_developer_mode()
    results = {}

    tag_a = "sorte"
    ending_list = get_words_ending_with(tag_a)
    ending_list = [r[: -len(tag_a)] for r in ending_list]
    ending_list = long_s.sort_words(ending_list)
    results[tag_a] = ending_list

    tag_b = "sort"
    ending_list = get_words_ending_with(tag_b)
    ending_list = [r[: -len(tag_b)] for r in ending_list]
    ending_list = long_s.sort_words(ending_list)
    results[tag_b] = ending_list

    list_a, list_b = results[tag_a], results[tag_b]
    matches = []
    for a in list_a:
        for b in list_b:
            if a == b:
                matches.append(a)

    list_a = long_s.sort_words([e for e in list_a if e not in matches])
    list_b = long_s.sort_words([e for e in list_b if e not in matches])

    print(
        f'Words ending with "{tag_a}" that do not have a corresponding word ending with "{tag_b}":'
    )
    with open("sorte-ambiguities.txt", "w", encoding="utf-8") as file:
        for a in list_a:
            if len(a) < 1:
                continue

            option_j = a
            if option_j[-1] == "s":
                option_j = option_j[:-1] + "ſ"
            cutoff_j = f"ſ{tag_a[1:]}"

            option_k = a
            if option_k[-2] == "s":
                option_k = option_k[:-2] + "ſ" + option_k[-1:]
            cutoff_k = tag_a

            line = f"{option_j}\t{cutoff_j}\t{option_k}s\t{cutoff_k[1:]}"
            file.write(line + "\n")

    print(
        f'\n\nWords ending with "{tag_b}" that do not have a corresponding word ending with "{tag_a}":'
    )
    for b in list_b:
        print(f"{b}s\t{tag_b[1:]}")

    print(
        f'\n\nWords ending with "{tag_a}" that has a corresponding word ending with "{tag_b}":'
    )
    for m in matches:
        print(f"{m}s\t{tag_a[1:]}\t\t{m}s\t{tag_b[1:]}")


if __name__ == "__main__":
    main()
