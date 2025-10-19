from utils.text_utils import get_word_stats


def test_word_stats():
    sample_words = ['python', 'is', 'fun', 'python']
    total, top3 = get_word_stats(sample_words)
    assert total == 4
    assert top3[0][0] == 'python'
    print('Utils import and function test passed!')


if(__name__ == '__main__'):
    test_word_stats()