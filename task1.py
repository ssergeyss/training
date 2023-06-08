
vowels_list = ["а", "е", "ё", "и", "й", "о", "у", "ы", "э", "ю", "я"]


def input_text():
    text = input('\nВведите текст: ')
    return text.lower()


def vowels_check(latter):
    for vowel_latter in vowels_list:
        if vowel_latter == latter:
            return True
    return False


def vowels_count_text(text):
    vowels_in_text = [text[index] for index in range(len(text))
                      if vowels_check(text[index])]
    print(f'Список гласных букв: {vowels_in_text}')
    print(f'Длина списка: {len(vowels_in_text)} ')


def main():
    text = input_text()
    vowels_count_text(text)


if __name__ == "__main__":
    main()





















