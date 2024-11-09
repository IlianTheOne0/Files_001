def main():
    try:
        _write()
        print('Task is completed!')
    except Exception as e:
        print(f'Error: {e}')

def _write():
    with open('assets/original_file.txt', 'r') as read_:
        with open('assets/processed_file.txt', 'w') as write_:
            read_ = read_.readlines()

            for number_of_line in range(0, len(read_)):
                line = (read_[number_of_line].replace('\n', ''))
                write_.write(line + '\n')