
import random


def create_required_list():
    nice_list = nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
    # list_len = len(nice_list)
    # sub_list_len = len(nice_list[0])
    # sec_sub_len = len(nice_list[0][0])
    # total_len = list_len * sub_list_len * sec_sub_len
    # required_list = [nice_list[index // (sec_sub_len * sub_list_len)][index // sec_sub_len % sub_list_len]
    #                  [index % sec_sub_len] for index in range(total_len)]
    required_list = [symbol for sub_list in nice_list for sec_sub_list in sub_list
                     for symbol in sec_sub_list]
    print(f'Сгенерированный двумерный список: {required_list}')


def main():
    create_required_list()


if __name__ == "__main__":
    main()





















