import os
import pandas as pd
from sklearn.datasets import load_breast_cancer

def download_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, 'breast_cancer_raw')
    os.makedirs(output_dir, exist_ok=True)
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    out_path = os.path.join(output_dir, "raw.csv")
    df.to_csv(out_path, index=False)
    print(f"Breast Cancer dataset downloaded and saved to {out_path}")

if __name__ == "__main__":
    download_data()
