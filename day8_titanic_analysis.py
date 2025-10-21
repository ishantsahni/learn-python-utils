import pandas as pd

def load_titanic():
    df = pd.read_csv('titanic.csv')
    print('Titanic dataset loaded!\n')
    print(df.head())
    print('\nShape: ', df.shape)
    print('Columns: ', list(df.columns))
    return df

def explore_titanic(df):
    print('\n--- Passengers older than 50 ---')
    print(df[df['Age'] > 50][['Name', 'Age', 'Sex', 'Survived']])

    print('\n--- Average age by class ---')
    print(df.groupby('Pclass')['Age'].mean())

    print('\n--- Survival rate by gender ---')
    print(df.groupby('Sex')['Survived'].mean())

def analyze_titanic(df):
    print('\n--- Summary Statistics ---')
    print(df.describe())
    
    rate = df['Survived'].mean() * 100
    print(f'\nOverall Survival Rate: {rate:.2f}%')
    print(df.isnull().sum())

def test_titanic():
    df = pd.read_csv('titanic.csv')
    assert 'Survived' in df.columns
    assert len(df) > 500
    print('Titanic data set passed!')

if __name__ == '__main__':
    df = load_titanic()
    explore_titanic(df)
    analyze_titanic(df)
    test_titanic()