# Tasks 7 & 8 are the same

from assets.array import text

def main():
    try:
        _write()
        print('Task is completed!')
    except Exception as e:
        print(f'Error: {e}')

def _write():
    with open('assets/processed_file.txt', 'w') as write_:
        for line in text:
            write_.write(line + '\n')