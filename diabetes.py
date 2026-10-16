from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

DATASET_CANDIDATES = (
    Path(__file__).resolve().parent / "diabetes.csv",
    Path.cwd() / "diabetes.csv",
    Path("/content/diabetes.csv"),  # Google Colab compatibility
)


def load_dataset() -> pd.DataFrame:
    """Load diabetes.csv from the project folder, current folder, or Colab."""
    for path in DATASET_CANDIDATES:
        if path.is_file():
            return pd.read_csv(path)

    searched = "\n".join(f"- {path}" for path in DATASET_CANDIDATES)
    raise FileNotFoundError(
        "Could not find diabetes.csv. Put the dataset next to diabetes.py.\n"
        f"Locations checked:\n{searched}"
    )


def main() -> None:
    diabetes_dataset = load_dataset()
    if "Outcome" not in diabetes_dataset.columns:
        raise ValueError("Dataset must contain an 'Outcome' target column.")

    X = diabetes_dataset.drop(columns=["Outcome"])
    y = diabetes_dataset["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=2
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    classifier = SVC(kernel="linear")
    classifier.fit(X_train_scaled, y_train)

    train_accuracy = accuracy_score(y_train, classifier.predict(X_train_scaled))
    test_accuracy = accuracy_score(y_test, classifier.predict(X_test_scaled))
    print(f"Training accuracy: {train_accuracy:.3f}")
    print(f"Test accuracy: {test_accuracy:.3f}")

    # Illustrative example only; not a medical diagnosis.
    sample = pd.DataFrame(
        [(5, 166, 72, 19, 175, 25.8, 0.587, 51)],
        columns=X.columns,
    )
    sample_scaled = scaler.transform(sample)
    prediction = int(classifier.predict(sample_scaled)[0])
    if prediction == 0:
        print("Model prediction: lower likelihood class (Outcome = 0).")
    else:
        print("Model prediction: higher likelihood class (Outcome = 1).")
    print("This educational model is not a substitute for medical advice.")


if __name__ == "__main__":
    main()
