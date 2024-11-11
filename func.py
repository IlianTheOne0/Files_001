def main():
    try:
        function()
        print('Task is completed!')
    except Exception as e:
        print(f'Error: {e}')

def function():
    with open('assets/original_file.txt', 'r') as read_:
        with open('assets/processed_file.txt', 'w') as write_:
            lines = read_.readlines()

            index = []

            for number_of_line in range(len(lines)):
                line = lines[number_of_line]
                if ',' not in line:
                    index.append(number_of_line)

            for number_of_line in range(len(lines)):
                line = lines[number_of_line].replace('\n', '')
                write_.write(line + '\n')

                if number_of_line in index and (number_of_line == index[-1] or number_of_line + 1 != index[index.index(number_of_line) + 1]):
                    '''
                    Чи є номер строки в списку індексів
                    і
                        Чи це останній елемент
                        або
                        Наступний елемент не дорівнює наступному елементу в списку індексів
                    '''
                    write_.write('*' * 12 + '\n')

            print(index)