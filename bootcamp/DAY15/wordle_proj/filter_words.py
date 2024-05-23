red = 'R'
green = 'G'
yellow = 'Y'
def filter_Rwords(words: list, red_guess: list):
    eliminate_red = []
    for letter in red_guess:
        for word in words:
            if letter in word:
                eliminate_red.append(word)
    return eliminate_red

def filter_Ywords(words: list, yellow_guess: list):
    eliminate_yellow = []
    for letter in yellow_guess:
        for word in words:
            if letter not in word:
                eliminate_yellow.append(word)
    return eliminate_yellow

filer_Ywords(["SPEAR", "GEARY", "WEARY", "BRAIN"], ['S', 'R', 'A'] )



