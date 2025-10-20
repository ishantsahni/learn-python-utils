import pandas as pd



def read_csv_file(filename):
    df = pd.read_csv(filename)
    return df


def show_basic_info(df):
    print('File loaded successfully!\n')
    print('First 3 rows\n', df.head(3))
    print('\nColumns: ', [df.columns])
    print('\nTotal rows: ', len(df))

def analyze_data(df):
    print('\n--- Basic Statistics ---')
    print(df.describe())
    avg_age = df['age'].mean()
    print(f'\nAverage age: {avg_age:.1f}')

def test_analyze_data():
    df = read_csv_file('sample_data.csv')
    assert "age" in df.columns
    print('CSV test passed!')


if __name__ == '__main__':
    df = read_csv_file('sample_data.csv')
    show_basic_info(df)
    analyze_data(df)
    test_analyze_data()





