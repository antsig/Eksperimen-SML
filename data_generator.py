import urllib.request
import os

def download_data():
    os.makedirs('iris_raw', exist_ok=True)
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    urllib.request.urlretrieve(url, "iris_raw/raw.csv")
    print("Iris dataset downloaded to iris_raw/raw.csv")

if __name__ == "__main__":
    download_data()
