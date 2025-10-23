import pandas as pd

def load_csv(filename):
    df = pd.read_csv(filename)
    print(f'Loaded {filename} ({df.shape[0]} rows, {df.shape[1]} cols)')
    return df

def analyze_csv(df):
    print('\n--- Columns ---')
    print(list(df.columns))

    print('\n--- Missing Values ---')
    print(df.isnull().sum)

    print('\n--- Basic Statistics ---')
    print(df.describe(include='all'))

    numeric_cols = df.select_dtypes('number').columns
    summary = {}

    for col in numeric_cols:
        summary[col] = {
            'mean': round(df[col].mean(), 2),
            'median': round(df[col].median(), 2),
            'std': round(df[col].std(), 2)
        }

    print('\n--- Numeric Summary ---')
    for k, v in summary.items():
        print(f'{k}: {v}')

    return summary


def save_report(filename, summary):
    with open('analysis_report.txt', 'w') as f:
        f.write(f'Analysis report for {filename}\n\n')
        for col, stats in summary.items():
            f.write(f'{col}:\n')
            for k, v in stats.items():
                f.write(f'    {k}: {v}\n')
            f.write('\n')
    print('Report saved -> analysis_report.txt')


def test_analyzer():
    df = load_csv('titanic_cleansed.csv')
    summary = analyze_csv(df)
    save_report('titanic_cleansed.csv', summary)
    assert 'Age' in summary
    print('Analyze CSV Analyzer test passed!')


if __name__ == '__main__':
    df = load_csv('titanic_cleansed.csv')
    summary = analyze_csv(df)
    save_report('titanic_cleansed.csv', summary)
    test_analyzer()



