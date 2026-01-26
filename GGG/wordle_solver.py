from collections import Counter


def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        return [line.strip().upper() for line in f if len(line.strip()) == 5]


def is_compatible(word, guess, feedback):
    word = word.upper()
    guess = guess.upper()

    # 1) Greens
    for i in range(5):
        if feedback[i] == "G" and word[i] != guess[i]:
            return False
        if feedback[i] != "G" and word[i] == guess[i]:
            return False

    # 2) Comptage lettres
    word_count = Counter(word)

    # Retirer les greens
    for i in range(5):
        if feedback[i] == "G":
            word_count[guess[i]] -= 1

    # 3) Yellows & Blacks
    for i in range(5):
        if feedback[i] == "Y":
            if word_count[guess[i]] <= 0:
                return False
            word_count[guess[i]] -= 1

        if feedback[i] == "B":
            if word_count[guess[i]] > 0:
                return False

    return True


def filter_words(words, guess, feedback):
    return [w for w in words if is_compatible(w, guess, feedback)]


def main():
    words = load_words()
    print(f"{len(words)} mots chargés")

    guess = "CRANE"
    feedback = "BBYBG"  # exemple Wordle

    possible = filter_words(words, guess, feedback)
    print("Mots encore possibles :", possible)


if __name__ == "__main__":
    main()
