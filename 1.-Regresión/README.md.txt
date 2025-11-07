## Introduction

Compensation in data roles varies widely across countries, job titles, seniority, and company size. This project builds a reproducible pipeline to profile a public salary dataset, control outliers, encode high-cardinality categories, and train regularized regression models to predict salary.

## Project Goal

- Predict salary (recommended target: **`salary_in_usd`**) from structured attributes (year, experience level, job title, company location, company size).
- Build a baseline, then improve it with **Ridge** (and leave room for tree-based models).

## Dataset & Methodology (bullet overview)

- **Dataset:** ~3,761 rows × 9 columns (original file `salary.xls` but CSV-formatted).
- **Key fields:** `work_year`, `experience_level`, `employment_type`, `job_title`, `company_location`, `company_size`, `salary`, `salary_currency`, `salary_in_usd`.
- **Data audit:** 0 nulls; ~1,351 exact duplicates removed.
- **Target choice:** Prefer **`salary_in_usd`** for currency comparability.
- **Preprocessing:**
    - Ordinal maps: `experience_level` (EN<MI<SE<EX), `company_size` (S<M<L).
    - One-hot for `job_title` and `company_location` with long-tail control (group rare categories).
    - Outlier policy: scenario with raw data; scenario capped (e.g., salaries < 1,000,000 USD).
- **Modeling:**
    - **Baseline:** mean predictor.
    - **Ridge Regression (α≈10)** with train/test split (80/20).
    - Metrics: **RMSE** and **R²** (plus MAE recommended for exec reporting).
- **Reproducibility:** documented pipeline steps, clear assumptions, and seeds.

## Results (quick glance)

- **Raw dataset scenario**
    - Baseline RMSE ≈ **248k USD**
    - Ridge RMSE ≈ **190k USD** | R² ≈ **0.404**
- **Filtered scenario (salary < 1,000,000 USD)**
    - Baseline RMSE ≈ **65.4k USD**
    - Ridge RMSE ≈ **51.6k USD** | R² ≈ **0.379**

**Interpretation:** Regularization stabilizes coefficients in a high-dimensional dummy space; controlling extreme outliers reduces absolute error.

## Visual Highlights

- Distribution of `salary_in_usd` (raw vs. filtered).
- Top 10 job titles & top countries by count.
- RMSE comparison: Baseline vs Ridge (bar plot).
- Coefficient magnitudes (Ridge) grouped by feature family (country, job title, experience).

## Conclusions & Ideas for Improvement

**What works:**

- Ridge handles multicollinearity and high-cardinality one-hots reliably.
- Outlier control materially improves error.