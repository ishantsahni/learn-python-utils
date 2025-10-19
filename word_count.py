def count_words(filename):
    with open(filename, 'r') as file:
        file = file.read()
        words = file.split()
        return len(words)
    
if __name__ == "__main__":
    total = count_words("sample.txt")
    print(f"Total words in file: {total}")





# Basic test for count_words function

def test_count_words():
    result = count_words('sample.txt')
    assert isinstance(result, int), 'Result should be an integer'
    assert result > 0, 'Word count should be greater than zero'
    print('Test passed!')


test_count_words()