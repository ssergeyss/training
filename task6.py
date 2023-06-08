
import random


def create_2dimensional_list():
    two_dem_list = [[random.randint(0, 20) for _ in range(3)] for _ in range(4)]
    print(f'Сгенерированный двумерный список: {two_dem_list }')


def main():
    create_2dimensional_list()


if __name__ == "__main__":
    main()





















