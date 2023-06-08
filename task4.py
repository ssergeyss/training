

def create_required_results(alphabet):
    copy_list = alphabet[:]
    print(f'1: {copy_list}\n 2: {copy_list[::-1]}\n 3: {copy_list[::2]}\n'
          f'4: {copy_list[1::2]}\n 5: {copy_list[:1]}\n 6: {copy_list[-1:]}\n' 
          f'7: {copy_list[3:4]}\n 8: {copy_list[-3:]}\n 9: {copy_list[3:5]}\n'
          f'10: {copy_list[4:2:-1]}')


def main():
    alphabet = 'abcdefg'
    create_required_results(alphabet)


if __name__ == "__main__":
    main()




















