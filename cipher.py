import string


def solution(word: str, cipher):
    try:
        translator = str.maketrans(string.ascii_lowercase, cipher)
    except:
        return ""
    for char in word:
        if char not in string.ascii_lowercase:
            return ""
    return word.translate(translator)


def test_solution():
    assert solution("helloword", "bjosxcqukmrhgeynazlwfpvti") == 0

