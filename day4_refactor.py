# traverse a list
# for x in [1, 2, 3]:
#     print(x)

# # append to a list
# nums = []

# for i in range(3):
#     nums.append(i)

# print(nums)

# # tupels
# myTupels = ('ishant', 28, 'engineer')
# print(myTupels)
# print(myTupels[1])

# # dictionaries
# scores = {"Ishant": 95, "Monika": 88}

# print(scores["Ishant"])
# for name,score in scores.items():
#     print(name, score)

from collections import Counter

def get_words_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().split()
            
# total freq top3    
def get_word_stats(words):
    total = len(words)
    freq = Counter(words)
    top3 = freq.most_common(3)
    return total, top3

def main():
    words = get_words_from_file('sample.txt')
    total, top3 = get_word_stats(words)
    print(f'Total words: {total}')
    print(f'Top 3 words')
    for word, count in top3:
        print(f'{word}: {count}')
    

if __name__ == '__main__':
    main()


# test
def test_get_word_stats():
    words = ['hello', 'world', 'hello']
    total, top3 = get_word_stats(words)
    assert total == 3
    assert top3[0][0] == 'hello'
    print('Test passed')