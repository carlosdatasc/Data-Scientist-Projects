Customer retention is one of the most critical challenges for any service-based company. Losing a customer is often more expensive than acquiring a new one, which makes predicting churn a strategic advantage.

This project develops a **supervised classification model** to determine whether a banking customer is likely to leave the service.

---

**Project Objective**

Build a complete Machine Learning pipeline that:

- Identifies factors associated with customer churn
- Trains multiple classification models
- Evaluates performance using metrics suitable for imbalanced data
- Extracts actionable insights that could support real retention strategies

---

**Dataset & Methodology**

**Dataset**

- Banking customer dataset
- 13,000+ records
- Demographic, financial, and behavioral features
- Target variable: `Attrition_Flag`

**Methodology**

- Initial exploration and problem understanding
- Preprocessing:
    - data cleaning
    - OneHotEncoding for categorical variables
    - StandardScaler for numerical features
    - class-weight balancing for imbalance
- Exploratory Data Analysis (EDA):
    - distributions
    - correlations
    - behavioral patterns of churned vs. retained customers
- Model training:
    - Logistic Regression
    - Random Forest
- Evaluation using:
    - Confusion Matrix
    - Recall
    - F1 Score
    - ROC-AUC

---

**Results & Visualizations**

**Key Findings**

- Transaction activity is the strongest churn predictor.
- Lower-income customers show higher churn rates.
- Low credit usage is strongly tied to churn.
- Certain card types concentrate more churn cases.

**Model Results**

- **Logistic Regression** performed as a strong baseline.
- **Random Forest** captured non-linear relationships with potential for improvement via hyperparameter tuning.

*(Add your graphs here: confusion matrix, ROC curves, feature importance, etc.)*

---

**Conclusions & Improvement Ideas**

- Churn is heavily influenced by **behavioral variables** rather than demographics.
- The model could be improved by:
    - Applying SMOTE or ADASYN
    - Performing hyperparameter tuning
    - Using SHAP for interpretability
    - Feature engineering to capture deeper patterns