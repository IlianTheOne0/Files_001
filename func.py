def main():
    comparator()

def comparator():
    with open('assets/first.txt', 'r') as first:
        with open('assets/second.txt', 'r') as second:
            first_text = first.readlines()
            second_text = second.readlines()

            the_same = False

            if len(first_text) > len(second_text):
                print(f'Line {len(second_text)+1} is missing in the second file')
            elif len(second_text) > len(first_text):
                print(f'Line {len(first_text)+1} is missing in the first file')
            else:
                the_same = True

                for i in range(len(first_text)):
                    first_line = first_text[i].replace('\n', '')
                    second_line = second_text[i].replace('\n', '')
                    if first_line != second_line:
                        print(f'Line {i+1} is different:')
                        print(f'First: {first_line if first_line != "" else ("| NOTHING |")}')
                        print(f'Second: {second_line if second_line != "" else ("| NOTHING |")}\n')

                        the_same = False

            if the_same:
                print('Files are the same')