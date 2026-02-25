import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

def load_data(filepath):
    print(f"Loading data from {filepath}...")
    return pd.read_csv(filepath)

def preprocess_data(df):
    print("Preprocessing data...")
    # Pisahkan fitur dan target (target: species)
    X = df.drop('species', axis=1)
    y = df['species']
    
    # Menangani missing values (jika ada)
    X = X.fillna(X.median())
    
    # Standarisasi
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    # Gabungkan kembali
    df_processed = X_scaled.copy()
    df_processed['species'] = y
    
    return df_processed

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_data_path = os.path.join(base_dir, 'iris_raw', 'raw.csv')
    
    if not os.path.exists(raw_data_path):
        print(f"File {raw_data_path} not found. Please ensure it exists.")
        return

    df = load_data(raw_data_path)
    df_processed = preprocess_data(df)
    
    # Split
    print("Splitting data into train and test sets...")
    train_df, test_df = train_test_split(df_processed, test_size=0.2, random_state=42, stratify=df_processed['species'])
    
    # Save
    output_dir = os.path.join(base_dir, 'preprocessing', 'iris_preprocessing')
    os.makedirs(output_dir, exist_ok=True)
    train_path = os.path.join(output_dir, 'train.csv')
    test_path = os.path.join(output_dir, 'test.csv')
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    print(f"Data successfully preprocessed and saved to {train_path} and {test_path}")

if __name__ == "__main__":
    main()
