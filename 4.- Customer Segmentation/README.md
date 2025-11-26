Companies collect large amounts of information about their customers — purchases, payment methods, amounts spent, frequency of visits.

But by themselves, these records don’t tell a story.

The goal of this project is to turn raw transactional data into **actionable customer segments**, enabling better understanding and evidence-based decisions.

This project is part of *Ciencia de Datos Jr.*, a portfolio designed to learn and apply real analytical techniques through hands-on projects.

---

**Project Objective**

Build a **customer segmentation model** using *unsupervised clustering techniques*, integrating multiple datasets and generating interpretable profiles such as:

- Premium customers
- Frequent buyers
- Occasional buyers
- Inactive or at-risk customers

---

** Dataset & Methodology**

**Datasets Used**

This project integrates data from 3 independent tables:

- `clientes` — demographic information
- `pagos` — payment amounts, dates, and payment method
- `pedidos` — purchase history and order dates

**Methodology (step by step)**

1. **Exploratory Data Analysis (EDA)**
    - Data types inspection
    - Missing values and duplicates
    - Outlier detection
    - Distribution analysis
2. **Preprocessing**
    - Imputation using medians and modes
    - Type corrections
    - Aggregations per customer
    - Feature engineering (RFM + additional behavioral metrics)
    - Scaling with `StandardScaler`
3. **Clustering Modeling**
    - KMeans
    - Agglomerative Clustering
    - Determination of optimal number of clusters using Elbow + Silhouette
4. **Cluster Profiling**
    - Mean, median, and IQR per cluster
    - Interpretation of customer groups
    - Construction of the *Cluster Profile Table*

---

** Results & Visualizations**

The model identified **4 consistent and business-meaningful clusters** with clear differences in:

- total amount spent
- number of purchases
- recency of last order
- preferred payment methods
- average ticket size

**Included visualizations:**

- Histograms
- Correlation matrix
- Variable distributions by cluster
- RFM comparisons
- Final customer profile table

---

** Conclusions & Future Improvements**

**Key Takeaways**

- RFM logic remains a powerful way to understand customer behavior.
- Aggregation and feature engineering were the most critical steps.
- The segmentation provides strong support for personalized business strategies.

**Future Improvements**

- Test more advanced clustering methods (DBSCAN, HDBSCAN, Gaussian Mixtures).
- Add new features (returns, customer satisfaction, purchase channel).
- Apply PCA for 2D visualization.
- Explore temporal evolution of each segment.