#!/usr/bin/python3
"""
    5-text_indentation:
        Functions:
            text_indentation
"""


def text_indentation(text):
    """
    text_indentation: print text with indentation
        Args:
            @text: text to print
    """
    if type(text) != str:
        raise TypeError("text must be a string")
        return

    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print("")
        elif text[i] == " ":
            j = i - 1
            while j:
                if text[j] == ' ':
                    j -= 1
                    continue

                if text[j] in ['.', '?', ':']:
                    break

                print(text[i], end='')
                j = 0
        else:
            print(text[i], end='')
