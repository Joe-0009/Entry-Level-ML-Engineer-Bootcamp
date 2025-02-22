import string
import sys


def non_punctuation(word):
    count = 0
    for c in word:
        if c not in string.punctuation:
            count += 1
    return count


def make_list(input, N):
    lists = input.split()
    filtered = [word for word in lists if non_punctuation(word) > N]
    print(filtered)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    elif not sys.argv[2].isdigit():
        print("ERROR")
    else:
        make_list(sys.argv[1], int(sys.argv[2]))
