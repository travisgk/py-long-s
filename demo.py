import long_s


def main():
    print(long_s.convert("The discussion was surprisingly insightful.", lang="en"))
    print(long_s.convert("La discussion était étonnamment perspicace.", lang="fr"))
    print(
        long_s.convert(
            "La discussione è stata sorprendentemente perspicace.", lang="it"
        )
    )
    print(long_s.convert("La discusión fue sorprendentemente perspicaz.", lang="es"))
    print(long_s.convert("Die Diskussion war überraschend aufschlussreich.", lang="de"))


if __name__ == "__main__":
    main()
