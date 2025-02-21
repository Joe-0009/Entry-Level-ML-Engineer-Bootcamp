import sys
import string


def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text is None:
        text = input("What is the text to analyze?\n")
    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return
    printable = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    space = text.count(" ")
    punctuation = sum(1 for c in text if c in string.punctuation)
    print(f"The text contains {printable} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space} space (s)")


if __name__ == "__main__":
    text_analyzer()
