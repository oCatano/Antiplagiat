import sys
import re


# Levitan distance
def distance(text1, text2) -> int:
    first_len, second_len = len(text1), len(text2)
    if first_len > second_len:
        text1, text2 = text2, text1
        first_len, second_len = second_len, first_len

    current_row = range(first_len + 1)
    for i in range(1, second_len + 1):
        previous_row, current_row = current_row, [i] + [0] * first_len
        for j in range(1, first_len + 1):
            # Add, delete, and change symbols
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if text1[j - 1] != text2[i - 1]:
                change += 1
            current_row[j] = min(add, change, delete)
    return current_row[first_len]


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file) as compare_src:

        for paths in compare_src:
            original_path, plagiat_path = paths.split()
            with open(original_path, encoding='utf_8') as original_file:
                original_text = re.split(r'\s', ' '.join(original_file.readlines()).lower())
                original_text = "".join(original_text)
            with open(plagiat_path, encoding='utf_8') as plagiat_file:
                plagiat_text = re.split(r'\s', ''.join(plagiat_file.readlines()).lower())
                plagiat_text = "".join(plagiat_text)

            longest_text = max(len(original_text), len(plagiat_text))
            output = (longest_text - distance(original_text, plagiat_text)) / longest_text

            with open(output_file, 'a') as scores:
                scores.write(str(output) + '\n')
