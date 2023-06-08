

def input_parameter():
    while True:
        list_lenght = input('\nВведите длину списка: ')
        if input_parameter_check(list_lenght):
            return int(list_lenght)
        else:
            print('Введите целое положительное число!!!')


def input_parameter_check(list_lenght):
    if list_lenght.isdigit() and int(list_lenght) > 0:
        return True
    else:
        return False


def create_list(list_lenght):
    required_list = [1 if index % 2 == 0 else index % 5 for index in range(list_lenght)]
    print(f'Результат:: {required_list}')


def main():
    list_lenght = input_parameter()
    create_list(list_lenght)


if __name__ == "__main__":
    main()





















