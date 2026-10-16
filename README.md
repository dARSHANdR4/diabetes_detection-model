## Live combined dashboard

Try the combined Crop, Fertilizer, and Diabetes educational screening interface:
**https://ai-prediction-studio.pages.dev/**

API health status: https://ai-prediction-studio-api.onrender.com/health  
API documentation: https://ai-prediction-studio-api.onrender.com/docs

The live Diabetes module is an educational screening demonstration, not a diagnosis or a substitute for medical testing. A low-risk output cannot rule out diabetes.

---

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
