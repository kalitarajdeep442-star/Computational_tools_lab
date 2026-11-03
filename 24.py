import pandas as pd

def clean_titanic_data(csv_file):
    # Load the real-world dataset
    df = pd.read_csv(csv_file)
    
    print("Original Dataset Shape:", df.shape)
    
    # 1. Drop columns with a high percentage of missing values or irrelevant info
    # 'Cabin' usually has too many missing values in the Titanic dataset
    df.drop(columns=['Cabin', 'Ticket', 'PassengerId', 'Name'], inplace=True, errors='ignore')
    
    # 2. Handle missing values
    # Fill missing 'Age' with the median age
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())
        
    # Fill missing 'Embarked' with the mode (most common port)
    if 'Embarked' in df.columns:
        mode_embarked = df['Embarked'].mode()[0]
        df['Embarked'] = df['Embarked'].fillna(mode_embarked)
        
    # 3. Type Conversion
    # Convert 'Sex' and 'Embarked' to categorical types for better memory usage
    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].astype('category')
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].astype('category')
        
    # 4. Remove duplicates if any exist
    df.drop_duplicates(inplace=True)
    
    print("Cleaned Dataset Shape:", df.shape)
    print("Missing values after cleaning:\n", df.isnull().sum())
    
    return df

# Usage
cleaned_df = clean_titanic_data('titanic.csv')
