# Signe Kristīne Šteimaka 221RBD327

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
            if next in "([{":        
     
                opening_brackets_stack.append(Bracket(next, i + 1))
                
            elif next in ")]}":
                if len(opening_brackets_stack) == 0:
                    return i + 1

                top = opening_brackets_stack.pop()
                if not are_matching(top.char, next):
                    return i + 1
                    
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    text = input()

     # For GitHub tests
    if 'I' in text[0]:
        text = input()

    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main() 
