# Diabetes Detection (SVM)

An educational Support Vector Machine (SVM) example using the Pima Indians diabetes dataset.

## Run

Python 3.10+ is recommended.

```bash
python -m pip install -r requirements.txt
python diabetes.py
```

If `diabetes.csv` is not present, the script attempts to download the public dataset from [npradaschnor/Pima-Indians-Diabetes-Dataset](https://github.com/npradaschnor/Pima-Indians-Diabetes-Dataset). If downloading fails, download its `diabetes.csv` and place it beside `diabetes.py`.

The expected columns are Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, and Outcome.

## Limitations

This dataset is an educational benchmark and does not represent every population. Model output is not a clinical diagnosis and must not be used to make healthcare decisions.
