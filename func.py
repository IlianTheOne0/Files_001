def main():
    _write()
    print('Task is completed!')

def _write():
    with open('assets/original_file.txt', 'r') as read_:
        with open('assets/results.txt', 'w') as write_:
            read_ = read_.readlines()

            consonant_sounds_pattern = 'aeiouy'
            vowel_sounds_pattern = 'bcdfghjklmnpqrstvwxz'
            digit_pattern = '1234657890'

            char_counter = 0
            line_counter = len(read_)
            consonant_sounds_counter = 0
            vowel_sounds_counter = 0
            digit_counter = 0

            for number_of_line in range(0, len(read_)):
                line = (read_[number_of_line].replace('\n', ''))

                for temp in line:
                    char_counter += 1

                line = line.split()

                for word in line:
                    for char in word.lower():
                        if char in consonant_sounds_pattern:
                            consonant_sounds_counter += 1
                        if char in vowel_sounds_pattern:
                            vowel_sounds_counter += 1
                        if char in digit_pattern:
                            digit_counter += 1

            write_.write(f'Number of characters: {char_counter}\n' \
                         f'Number of lines: {line_counter}\n' \
                         f'Number of consonant sounds: {consonant_sounds_counter}\n' \
                         f'Number of vowel sounds: {vowel_sounds_counter}\n' \
                         f'Number of digits: {digit_counter}')