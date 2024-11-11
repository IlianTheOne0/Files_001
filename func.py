def main():
    try:
        word = str(input('Enter a word to find: '))
        print(f'The word {word} appears in the text {finder(word)} the number of times')
    except Exception as e:
        print(f'Error: {e}')

def finder(word):
    with open('assets/original_file.txt', 'r') as read_:
        with open('assets/processed_file.txt', 'w') as write_:
            read_ = read_.readlines()

            counter = 0

            for number_of_line in range(0, len(read_)):
                words = read_[number_of_line].split()

                for word_temp in words:
                    if word == word_temp:
                        counter += 1

    return counter