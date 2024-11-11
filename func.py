def main():
    try:
        print('Words is the text:', _write())
    except Exception as e:
        print(f'Error: {e}')

def _write() -> int:
    with open('assets/original_file.txt', 'r') as read_:
        read_ = read_.readlines()

        counter = 0

        for number_of_line in range(0, len(read_)):
            line = (read_[number_of_line].replace('\n', ''))
            pattern = '!@#$%^&*()_+,./<>?;:[]{}|1234567890'

            for char in pattern:
                line = line.replace(char, '')

            for temp in line.split(' '):
                if temp:
                    counter += 1
    return counter