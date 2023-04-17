from problems.string_problems import is_palindrome, is_palindrome_relaxed, \
    reverse_words_order, is_anagram


class TestPalindromes:
    def test_correct_palindromes(self):
        assert is_palindrome('ABCBA')
        assert is_palindrome('ABCBA')
        assert is_palindrome('RACACAR')
        assert is_palindrome('abababa')
        assert is_palindrome('abbababba')
        assert is_palindrome('deed')

    def test_incorrect_palindromes(self):
        assert not is_palindrome('ABSURD')
        assert not is_palindrome('abbababa')
        assert not is_palindrome('deadead')


class TestRelaxedPalindromes:
    def test_correct_relaxed_palindromes(self):
        assert is_palindrome_relaxed('ABCBA')
        assert is_palindrome_relaxed('ABCEBA')
        assert is_palindrome_relaxed('RACEACAR')
        assert is_palindrome_relaxed('abbababa')
        assert is_palindrome_relaxed('abbababba')
        assert is_palindrome_relaxed('deead')

    def test_incorrect_relaxed_palindromes(self):
        assert not is_palindrome_relaxed('ABSURD')
        assert not is_palindrome_relaxed('abbbababa')
        assert not is_palindrome_relaxed('deadead')


class TestWordReversing:
    def test_words_get_reversed(self):
        assert reverse_words_order('Hello World') == 'World Hello'
        assert reverse_words_order('The quick brown fox jumped over a lazy dog'
                                   ) == 'dog lazy a over jumped fox brown ' \
                                        'quick The'

    def test_edge_strings(self):
        assert reverse_words_order('') == ''
        assert reverse_words_order('Hello  World  ') == 'World Hello'


class TestAnagrams:
    def test_valid_anagrams(self):
        assert is_anagram('soap', 'posa')
        assert is_anagram('rca', 'car')
        assert is_anagram('anagram', 'nagaram')

    def test_invalid_anagrams(self):
        assert not is_anagram('rat', 'car')
        assert not is_anagram('xoxo', 'xoxx')
        assert not is_anagram('xoxox', 'xoxx')
