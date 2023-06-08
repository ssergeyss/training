
import random


def create_list():
    first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
    second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
    win_list = [first_team[index] if first_team[index] >= second_team[index]
                else second_team[index] for index in range(20)]
    print(f'Первая команда: {first_team}')
    print(f'Вторая команда: {second_team}')
    print(f'Победители тура: {win_list}')


def main():
    create_list()


if __name__ == "__main__":
    main()





















