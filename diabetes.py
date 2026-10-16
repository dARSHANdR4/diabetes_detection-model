from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

PROJECT_DIR = Path(__file__).resolve().parent
DATASET_PATH = PROJECT_DIR / "diabetes.csv"
DATASET_URL = (
    "https://raw.githubusercontent.com/"
    "npradaschnor/Pima-Indians-Diabetes-Dataset/master/diabetes.csv"
)


def load_dataset() -> pd.DataFrame:
    """Load local diabetes.csv, downloading the public educational dataset if absent."""
    if not DATASET_PATH.is_file():
        print("diabetes.csv not found; attempting to download the public Pima dataset...")
        try:
            urlretrieve(DATASET_URL, DATASET_PATH)
        except Exception as exc:
            if DATASET_PATH.exists():
                DATASET_PATH.unlink()
            raise RuntimeError(
                "Could not download diabetes.csv. Download it manually from "
                f"{DATASET_URL} and place it beside diabetes.py."
            ) from exc

    dataset = pd.read_csv(DATASET_PATH)
    expected = [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome",
    ]
    if not set(expected).issubset(dataset.columns):
        raise ValueError(
            "diabetes.csv does not have the expected Pima dataset columns. "
            f"Expected: {expected}; found: {list(dataset.columns)}"
        )
    return dataset


def main() -> None:
    diabetes_dataset = load_dataset()
    feature_columns = [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age",
    ]
    X = diabetes_dataset[feature_columns]
    y = diabetes_dataset["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=2
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    classifier = SVC(kernel="linear")
    classifier.fit(X_train_scaled, y_train)

    print(f"Training accuracy: {accuracy_score(y_train, classifier.predict(X_train_scaled)):.3f}")
    print(f"Test accuracy: {accuracy_score(y_test, classifier.predict(X_test_scaled)):.3f}")

    # Illustrative sample only; this model is not a medical diagnostic tool.
    sample = pd.DataFrame(
        [(5, 166, 72, 19, 175, 25.8, 0.587, 51)],
        columns=feature_columns,
    )
    prediction = int(classifier.predict(scaler.transform(sample))[0])
    label = "lower likelihood class (Outcome = 0)" if prediction == 0 else "higher likelihood class (Outcome = 1)"
    print(f"Model prediction for illustrative sample: {label}")
    print("Educational demonstration only—not medical advice or a diagnosis.")


if __name__ == "__main__":
    main()
