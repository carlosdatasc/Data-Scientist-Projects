🏠 Housing Price Prediction with Regression Models

Part of the *Ciencia de Datos Jr.* portfolio

## 📌 Introduction

Housing prices depend on multiple factors: surface area, property age, number of rooms, and, especially, the socioeconomic characteristics of the surrounding area.

In this project, I built a regression model capable of **estimating a home's price** using structural and contextual numerical features.

## 🎯 Project Objective

Develop a supervised machine learning model to predict housing prices while exploring:

- Exploratory Data Analysis (EDA)
- Data quality and preprocessing
- Comparison of multiple regression algorithms
- Model evaluation using **RMSE**

## 🗂️ Dataset Summary

- **Rows:** 5000
- **Columns:** 7
- **Target variable:** `precio`
- **Predictors:** `m2`, `antiguedad`, `salas`, `dormitorios`, `renta_zona`, `poblacion_zona`

The dataset contains no missing values, no duplicates, and all features are numerical.

---

## 🔍 Methodology

### **1. Preprocessing**

- Converted `salas` and `dormitorios` to integer types.
- Correlation and low-variance checks (implemented but not executed in this version).
- Train-test split (80/20).
- Prepared structure for feature scaling.

### **2. EDA**

- Distribution plots and histograms.
- Pairplots for bivariate inspection.
- Correlation heatmap:
    - `renta_zona` is the strongest predictor.
    - `m2` and `salas` show very high collinearity (~0.96).

### **3. Modeling**

Regression models tested:

- **Linear models:** Linear Regression, Ridge, Lasso, ElasticNet
- **Tree-based models:** DecisionTree, RandomForest, AdaBoost
- **Distance-based:** KNeighbors

Evaluation metrics:

- **Train RMSE**
- **Cross-Validation RMSE**

### 🥇 **Best-performing Models**

The **linear and regularized models** produced the most stable and consistent results:

| Model | CV RMSE |
| --- | --- |
| Linear Regression | ~30,063 |
| Ridge | ~30,063 |
| Lasso | ~30,063 |
| ElasticNet | ~34,371 |

Tree-based models severely overfitted; KNN underperformed without proper scaling.

---

## 📊 Key Results

- Housing prices are most influenced by:
    - socioeconomic context (`renta_zona`)
    - property age
    - surface area (m2)
- The relationship between features and price is **mostly linear**.
- A simple Linear Regression performs competitively and consistently.

---

## 📌 Conclusions & Next Steps

- Linear models are the best fit for this dataset.
- Multicollinearity affects interpretability more than performance.
- Still pending:
    - applying feature selection
    - scaling features for KNN and regularized models
    - hyperparameter tuning
    - final evaluation on the test set
    - exporting the final model