from utils.text_utils import get_word_stats, get_words_from_file

def main():
    filename = 'sample.txt'
    words = get_words_from_file(filename)
    total, top3 = get_word_stats(words)

    print(f'Total words: {total}')
    print('Top 3 words:')
    for word, count in top3:
        print(f'{word}: {count}')


if __name__ == '__main__':
    main()