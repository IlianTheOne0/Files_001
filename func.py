def main():
    word_to_replace = str(input('Enter a word to replace: '))
    word_to_replace_with = str(input('Enter the word to replace with: '))

    replacer(word_to_replace, word_to_replace_with)

    print('Task is completed!')

def replacer(word, replace_with):
    with open('assets/original_file.txt', 'r') as read_:
        with open('assets/processed_file.txt', 'w') as write_:
            read_ = read_.readlines()

            for line in read_:
                words = line.split()

                for index_of_word in range(len(words)):
                    if words[index_of_word] == word:
                        words[index_of_word] = replace_with

                write_.write(' '.join(words) + '\n')