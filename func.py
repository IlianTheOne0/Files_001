def main():
    try:
        biggest_line, line_number = function()
        print(f'The biggest line is: {biggest_line} (line {line_number})')
    except Exception as e:
        print(f'Error: {e}')

def function():
    with open('assets/original_file.txt', 'r') as read_:
        with open('assets/processed_file.txt', 'w') as write_:
            read_ = read_.readlines()

            the_biggest, number = read_[0], 1

            for number_of_line in range(1, len(read_)):
                line = (read_[number_of_line].replace('\n', ''))

                if len(line) > len(the_biggest):
                    the_biggest, number = line, number_of_line + 1

    return the_biggest, number