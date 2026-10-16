# Diabetes Detection (SVM)

An educational machine-learning example that trains a Support Vector Machine (SVM) classifier on the Pima Indians diabetes dataset.

## Requirements

- Python 3.10+
- The dataset file `diabetes.csv` (not included in this repository unless you add it yourself)

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Place `diabetes.csv` beside `diabetes.py`. The CSV must contain the eight feature columns expected by the sample and an `Outcome` target column.
4. Run:

   ```bash
   python diabetes.py
   ```

The script also checks the current working directory and the traditional Google Colab `/content/diabetes.csv` location.

## Notes

- The train/test split is stratified and the scaler is fitted only on the training data to avoid test-set leakage.
- The printed sample row is illustrative; it must match the dataset's feature order.
- This project is for learning only. It is not a clinical tool and must not be used to diagnose or treat anyone.
