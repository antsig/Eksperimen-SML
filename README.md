# Eksperimen Data Preprocessing

Folder ini menyimpan script dan konfigurasi untuk otomatisasi _data preprocessing_ menggunakan GitHub Actions.

## Struktur Direktori

- `data_generator.py`: Script untuk mengunduh dataset Breast Cancer dari `sklearn` dan menyimpannya sebagai `raw.csv` di dalam folder `breast_cancer_raw`.
- `.github/workflows/preprocessing.yml`: Konfigurasi GitHub Actions ("Data Preprocessing") yang memantau perubahan pada `raw.csv` atau script preprocessing.
- `preprocessing/automate_Antonius_Sigid_Priharsanto.py`: Script preprocessing otomatis yang dipanggil oleh workflow.

## Alur Kerja (Workflow)

1. Perubahan atau penambahan data mentah (`breast_cancer_raw/raw.csv`) akan secara otomatis men-trigger GitHub Actions.
2. Runner (Ubuntu) akan menjalankan script preprocessing `automate_Antonius_Sigid_Priharsanto.py`.
3. Hasil preprocessing (`train.csv` dan `test.csv`) akan dibuat.
4. GitHub Actions secara otomatis melakukan _commit_ dan _push_ data hasil preprocessing tersebut ke repositori.
