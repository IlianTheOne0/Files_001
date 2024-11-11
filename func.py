def main():
    try:
        symbol = str(input('Enter a character to start counting words: '))
        print(f'{_write(symbol)} words were found after {symbol} in the file')
    except Exception as e:
        print(f'Error: {e}')

def _write(symbol: str) -> int:
    with open('assets/original_file.txt', 'r') as read_:
        read_ = read_.readlines()

        counter = 0

        for line in read_:
            line = line.split()

            for word in line:
                if symbol in word:
                    counter += 1

    return counter