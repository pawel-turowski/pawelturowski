def is_izogram(word):
    word = word.lower()
    letters = []
    for letter in word:
        if letter in letters:
            return False
        letters.append(letter)
    return True

def is_izgoram(word):
    return len(word) == len(set(word))



if __name__ == '__main__':
    word = input('Provide word: ')
    if is_izogram(word):
        print('Word is izogram')
    else:
        print('Word is not izogram')