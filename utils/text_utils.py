from collections import Counter

def get_words_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().split()
            
def get_word_stats(words):
    total = len(words)
    freq = Counter(words)
    top3 = freq.most_common(3)
    return total, top3