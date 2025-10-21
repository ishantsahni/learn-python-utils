import pandas as pd

def load_data():
    df = pd.read_csv('titanic.csv')
    print('Data loaded: ', df.shape)
    return df

def handle_missing(df):
    print('\nMissing values before:\n', df.isnull().sum())

    # fill numeric columns
    df['Age'].fillna(df['Age'].median(), inplace=True)

    # fill categorical columns
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # drop columns with too many nulls
    df.drop(columns=['Cabin'], inplace=True)

    print(f'\nMissing values after:\n', df.isnull().sum())
    return df


def clean_columns(df):
    df.rename(columns={
        'SibSp': 'SiblingsOnBoard',
        'Parch': 'ParentsChildrenOnBoard'
    }, inplace=True)
    print('\nColumns renamed:\n', list(df.columns))
    return df

def create_features(df):
    df['FamilySize'] = df['SiblingsOnBoard'] + df['ParentsChildrenOnBoard'] + 1
    df['isAlone'] = df['FamilySize'].apply(lambda x: 1 if x == 1 else 0)
    print('\nDerived features added:\n', df[['FamilySize', 'isAlone']].head())
    return df

def validate(df):
    assert df['Age'].isnull().sum() == 0
    assert 'Cabin' not in df.columns
    print('Validation passed!')

def save_cleaned(df):
    df.to_csv('titanic_cleansed.csv', index=False)
    print('\nSaved cleaned dataset: titanic_cleansed.csv')


if __name__ == '__main__':
    df = load_data()
    df = handle_missing(df)
    df = clean_columns(df)
    df = create_features(df)
    validate(df)
    save_cleaned(df)