#!/usr/bin/python

import sys

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
vowels = "aeiouy"

class FileNotFound(Exception):
    pass

class TypoGenerator:
    def insertedKey(self, s):
        """Produce a list of keywords using the `inserted key' method
        """
        kwds = []

        for i in range(0, len(s)):
            for char in alphabet:
                kwds.append(s[:i+1] + char + s[i+1:])

        return kwds

    def skipLetter(self, s):
        """Produce a list of keywords using the `skip letter' method
        """
        kwds = []

        for i in range(1, len(s)+1):
            kwds.append(s[:i-1] + s[i:])

        return kwds

    def doubleLetter(self, s):
        """Produce a list of keywords using the `double letter' method
        """
        kwds = []

        for i in range(0, len(s)+1):
            kwds.append(s[:i] + s[i-1] + s[i:])

        return kwds

    def reverseLetter(self, s):
        """Produce a list of keywords using the `reverse letter' method
        """
        kwds = []

        for i in range(0, len(s)):
            letters = s[i-1:i+1:1]
            if len(letters) != 2:
                continue

            reverse_letters = letters[1] + letters[0]
            kwds.append(s[:i-1] + reverse_letters + s[i+1:])

        return kwds

    def wrongVowel(self, s):
        """Produce a list of keywords using the `wrong vowel' method (for soundex)
        """
        kwds = []

        for i in range(0, len(s)):
            for letter in vowels:
                if s[i] in vowels:
                    for vowel in vowels:
                        s_list = list(s)
                        s_list[i] = vowel
                        kwd = "".join(s_list)
                        kwds.append(kwd)

        return kwds

    def wrongKey(self, s):
        """Produce a list of keywords using the `wrong key' method
        """
        kwds = []

        for i in range(0, len(s)):
            for letter in alphabet:
                kwd = s[:i] + letter + s[i+1:]
                kwds.append(kwd)

        return kwds


    def get_typos(self, s):
        """Calls all our typo generation methods on a string and return the result
        """
        kwds = []
        kwds += self.insertedKey(s)
        kwds += self.wrongKey(s)
        kwds += self.skipLetter(s)
        kwds += self.doubleLetter(s)
        kwds += self.reverseLetter(s)
        kwds += self.wrongVowel(s)

        return kwds


if __name__ == "__main__":
    generator = TypoGenerator()
    words = generator.get_typos(sys.argv[1])

    print(words)
    print(len(words))
