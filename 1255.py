from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        def count_letters(letters):
            count = [0] * 26
            for letter in letters:
                count[ord(letter) - ord("a")] += 1
            return count

        def calculate_word_score(word):
            return sum(score[ord(char) - ord("a")] for char in word)

        def backtrack(index, remaining_letters):
            if index == len(words):
                return 0

            max_score = backtrack(index + 1, remaining_letters.copy())

            word = words[index]
            word_letter_count = count_letters(word)
            can_form = True

            for i in range(26):
                if word_letter_count[i] > remaining_letters[i]:
                    can_form = False
                    break

            if can_form:
                for i in range(26):
                    remaining_letters[i] -= word_letter_count[i]

                current_score = calculate_word_score(word) + backtrack(
                    index + 1, remaining_letters
                )

                max_score = max(max_score, current_score)

                for i in range(26):
                    remaining_letters[i] += word_letter_count[i]

            return max_score

        remaining_letters = count_letters(letters)

        return backtrack(0, remaining_letters)
