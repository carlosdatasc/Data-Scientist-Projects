**Business Problem**
In the construction industry, budget accuracy is the difference between profitability and bankruptcy. Historically, this task falls on Cost Analysts; however, current market volatility (material inflation, geopolitical factors, uncertainty) makes traditional methods prone to human error.
**The Risk:**
• **Underestimating costs:** Leads to direct financial losses during execution.
• **Overestimating costs:** Results in losing bids against more accurate competitors.
Project Objective:
To create a data-driven decision support tool, evaluated under two critical metrics:
1. **R2 (Coefficient of Determination):** To measure how well the model explains cost variance.
2. **MAPE (Mean Absolute Percentage Error):** The primary business metric, chosen to ensure low percentage error in both small works (e.g., Drainage) and large projects (e.g., Bridges).
**The Dataset: Engineering & Cleaning**
Given the confidentiality of real financial data in the sector, an **Advanced Synthetic Dataset** was designed to simulate the physics and economics of 2,000 civil construction projects.
Generation Methodology:
The dataset was created using AI-assisted Python scripts (LLMs) to replicate real construction logic, for example:
• Correlation between *Soil Type* and *Machinery Performance*.
• Relationship between *Materials (Concrete/Steel)* and *Project Typology*.
Data Hygiene:
To simulate a "Real-world noise" environment, intentional errors were injected and subsequently treated:
• **Text Audit:** Standardization of categories.
• **Feature Engineering:** Date transformation and One-Hot Encoding.
• **Multicollinearity Detection:** Elimination of redundant variables using **VIF (Variance Inflation Factor)** analysis to avoid mathematical bias.
• **Outlier Handling:** Validation based on physical data (e.g., machinery hours vs. earth volume) rather than blind statistical removal.
**Analysis and Modeling (The Journey)**
The modeling process followed an iterative trial-and-error approach to find the optimal architecture.
**1. The Linear Failure (Baseline)**
Started with **Linear Regression**, assuming a direct relationship between material quantity and price.
• **Result:** Deceptively high R2 (99%) but an **unacceptable MAPE of 30.7%**.
• **Diagnosis:** The model suffered from **Magnitude Bias**. It minimized error in expensive works (Bridges) but failed drastically in small works.
**2. The Logarithmic Attempt**
A **Logarithmic Transformation (`Log-Lin`)** was applied to correct scale and heteroscedasticity.
• **Result:** Performance worsened (**MAPE 44.79%**).
• **Finding:** This revealed the problem wasn't just scale, but that the relationship between variables is **non-linear**. A simple straight line cannot model the complexity of different project types simultaneously.
**3. The Solution: Random Forest** 
An ensemble model (**Random Forest Regressor**) was implemented, capable of capturing non-linear relationships and segmenting decisions via trees.**MetricLinear RegressionRandom Forest (Final)R2 Score**0.9934-**0.9906MAPE (Error)**30.70%-**5.13%** 

**Insight:** The Random Forest model managed to "democratize" precision, reducing error in small works to competitive levels.
Feature Importance:
Contrary to the initial intuition that material would be the only important factor, the model discovered that time and difficulty factors are crucial:
1. `Estimated_Duration_Months` (Indirect costs).
2. `Excavation_Volume_m3` (Earthworks).
3. `Rocky_Soil_Type` (Difficulty factor).
**Conclusions and Next Steps**
This project serves as a solid **Proof of Concept (PoC)** on how Data Science can modernize construction management.
• **Validity:** Although the data is synthetic, the cleaning workflow and model selection demonstrate that budget uncertainty can be reduced using ensemble algorithms.
• **Future:** For production implementation, it is recommended to:
    1. Recalibrate the model with the company's real historical data.
    2. Integrate exogenous variables (Inflation indices, Exchange rates, Weather).
    3. Explore **Gradient Boosting (XGBoost)** models to further refine accuracy.