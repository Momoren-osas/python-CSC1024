letter = input("Enter a letter: ").lower()

match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"{letter} is a vowel")
    case _:
        print(f"{letter} is a consonant")