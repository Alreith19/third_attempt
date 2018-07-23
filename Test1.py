vowels = "AEIOUaeiou"


x = [1, 2, 3, 4, 5]

def anti_vowel(text):
    word = ""
    for letter in text:
        if letter not in vowels:
            word += letter
    return word

#print (anti_vowel("Whatupphomie"))




















score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    tot_score = 0
    for letter in word.lower():
        tot_score += score[letter]
    return tot_score






def count(sequence, item):
  count = 0
  for i in sequence:
    if i == item:
      count += 1
  return count





















