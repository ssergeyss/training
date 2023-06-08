

def input_text():
    text = input('\nВведите строку: ')
    return text.lower()


def create_required_text(text):
    required_text = [text[index] for index in range(text.rindex('h') - 1, text.index('h'), -1)]
    print(f'Развёрнутая последовательность между первым и последним h:', end=' ')
    for index in range(len(required_text)):
        print(required_text[index], end='')


def main():
    text = input_text()
    create_required_text(text)


if __name__ == "__main__":
    main()





















