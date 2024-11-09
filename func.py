def main():
    try:
        processed_text = _read()
        _write(processed_text)
        print('Task is completed!')
        # print(processed_text)
    except Exception as e:
        print(f'Error: {e}')

def _read():
    with open('assets/original_file.txt', 'r') as f:
        text = f.readlines()
        result = ''

        for number_of_line in range(0, len(text)):
            line = (text[number_of_line].replace('\n', ''))
            pattern = '!@#$%^&*()_+,./<>?;:[]{}|'

            for char in pattern:
                line = line.replace(char, '')

            for word in line.split(' '):
                if len(word) >= 7:
                    result += word + ' '
            result += '\n'

    return result

def _write(processed_text):
    with open('assets/processed_file.txt', 'w') as f:
        f.write(processed_text)