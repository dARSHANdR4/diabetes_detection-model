<p align="center"><img src="https://raw.githubusercontent.com/dARSHANdR4/dARSHANdR4/main/assets/minecraft-emerald-divider.svg?v=4" width="100%" alt="Animated emerald pixel divider"></p>

<div align="center">

# ❤️ Diabetes Detection · SVM

**Standalone educational ML example using the Pima diabetes dataset.**

[![Python](https://img.shields.io/badge/Python-245b32?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Model](https://img.shields.io/badge/Model-SVM-245b32?style=for-the-badge)](https://scikit-learn.org/)
[![Live dashboard](https://img.shields.io/badge/Combined_Screening-Live_Dashboard-245b32?style=for-the-badge&logo=cloudflarepages&logoColor=white)](https://ai-prediction-studio.pages.dev/)

</div>

<p align="center"><img src="https://raw.githubusercontent.com/dARSHANdR4/dARSHANdR4/main/assets/minecraft-emerald-divider.svg?v=4" width="100%" alt="Animated emerald pixel divider"></p>

## 🌐 Live combined dashboard

The standalone model repository is separate from the combined hosted screening module.

- **[Open AI Prediction Studio ↗](https://ai-prediction-studio.pages.dev/)** — crop, fertilizer, and educational diabetes screening.
- [Backend health](https://ai-prediction-studio-api.onrender.com/health)
- [Interactive API documentation](https://ai-prediction-studio-api.onrender.com/docs)
- [Combined dashboard source](https://github.com/dARSHANdR4/EDUNET_WEEK3_FINALWEEK)

## 🧪 Run the standalone example

Python 3.10+ is recommended.

```bash
git clone https://github.com/dARSHANdR4/diabetes_detection-model.git
cd diabetes_detection-model
python -m venv .venv
```

Activate the environment:

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python diabetes.py
```

If `diabetes.csv` is not available locally, the script attempts to download the public educational dataset from [npradaschnor/Pima-Indians-Diabetes-Dataset](https://github.com/npradaschnor/Pima-Indians-Diabetes-Dataset). If download fails, place `diabetes.csv` alongside `diabetes.py`.

Expected columns: `Pregnancies`, `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`, `DiabetesPedigreeFunction`, `Age`, and `Outcome`.

## ⚠️ Important limitations

- This is an educational benchmark and may not generalize to different populations.
- The standalone model and combined dashboard should not be treated as medical devices or diagnostic tools.
- A lower-risk output does **not** rule out diabetes. Do not use this result to make healthcare decisions or to delay appropriate clinical testing.

<p align="center"><img src="https://raw.githubusercontent.com/dARSHANdR4/dARSHANdR4/main/assets/minecraft-emerald-divider.svg?v=4" width="100%" alt="Animated emerald pixel divider"></p>

<div align="center">

**Built by [dARSHANdR4](https://github.com/dARSHANdR4) · Voxel Builder / Developer / Automation**

</div>


## Copyright and permissions

Copyright © 2026 dARSHANdR4. All rights reserved.

Unless otherwise stated, original project code and assets are reserved and no open-source licence is granted. Third-party materials remain subject to their respective licences. Public repositories may still be viewed and forked through GitHub's platform functionality. See [COPYRIGHT](./COPYRIGHT) for the full notice.
