"""
Problem: Clean and Reverse Words (process_text)
Write a Python function named process_text(text) that takes a single string parameter text and returns a modified version of the string based on the following rules:
1. Remove Digits: Any numeric character ('0' through '9') in the string must be removed entirely.
2. Reverse Each Word: Every word (sequences of non-space characters) must have its characters reversed.
3. Preserve Spaces: Words should remain separated by a single space, maintaining the original word order.
"""
text = input("Add the Text: ")

def process_text(text):
    fresh_text = ""

    for i in text:
        if not i.isdigit():
            fresh_text += i

    text_list = fresh_text.split()

    reversed_word = []
    
    for word in text_list:
        reversed_word.append(word[::-1])

    final_text = " ".join(reversed_word)

    return final_text

print(process_text(text))