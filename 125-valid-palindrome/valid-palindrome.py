class Solution:
    def isPalindrome(self, s: str) -> bool:
        word =""

        for char in s:
            if char.isalnum():
                word += char

        word = word.lower()
        print(word)

    # word[::-1] to read it from backward. :: to include all letters, : would remove the last letter in the string
        return word == word[::-1]


