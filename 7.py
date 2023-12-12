# ex - higher order printing

# 1. What does this code do?
# 2. How can we make this more readable?
# 3. What other functions

def noice(style):
    def pad(num):
        padding = []
        for _ in range(0, num):
            padding.append(' ')
        return ''.join(padding)

    noIce = ['n', 'o', 'i', 'c', 'e']

    for i in range(0, len(noIce)):
        print(pad(i), style(noIce[i]))


noice(lambda char: char.lower())
noice(lambda char: char.capitalize())
noice(lambda char: char.upper())