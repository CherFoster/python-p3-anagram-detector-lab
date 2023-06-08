class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, letters):
        anagram = []
        for letter in letters:
            if len(letter) == len(self.word) and letter.lower() != self.word:
                if sorted(letter.lower()) == sorted(self.word):
                    anagram.append(letter)
        return anagram

                  
# class Anagram:
#     def __init__(self, word):
#         self.word = sorted(word.lower())

#     def match(self, anagrams):
#         return [anagram for anagram in anagrams if sorted(anagram.lower()) == self.word and anagram.lower() != self.word]

