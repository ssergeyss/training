alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def input_text():
    text = input('\nВведите сообщение: ')
    return text.lower()


def input_shift():
    while True:
        shift = input('\nВведите сдвиг: ')
        if input_shift_check(shift):
            return int(shift)
        else:
            print('Введите целое положительное число!!!')


def input_shift_check(shift):
    if shift.isdigit() and int(shift) > 0:
        return True
    else:
        return False


def create_encrypted_message(text, shift):
    encrypted_message = [alphabet[alphabet.index(text_symbol) + shift - len(alphabet)]
                         if text_symbol in alphabet else text_symbol for text_symbol in text]
    print('Зашифрованное сообщение:', end=' ')
    for encrypted_symbol in encrypted_message:
        print(encrypted_symbol, end='')


def main():
    text = input_text()
    shift = input_shift()
    create_encrypted_message(text, shift)


if __name__ == "__main__":
    main()
