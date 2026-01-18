# Week 3 — Churn Prediction Baseline (Transactions Only)

## Objective

The objective of **Week 3** was to build a **baseline** using transaction-level data only, before introducing richer behavioral logs.

The focus was deliberately **not** on maximizing model accuracy, but on:

- Correct problem formulation  
- Validition and causality with rudimentary feature selection
- Establishing a defensible baseline suitable for extension  

---

## Dataset Scope

This phase uses the following KKBox datasets:

- **`transactions.csv`** — subscription transactions and cancellations  
- **`train.csv`** — pre-defined churn labels provided by the dataset authors  

---

## Key Design Decision: Prediction Timing

A central risk in churn modeling is **post-churn leakage**, where features capture inactivity or cancellation behavior that has already effectively realized churn.

To mitigate this, the modeling problem was explicitly framed as:

> **At a given time T, can we predict which users will churn (as defined in `train.csv`) using only historical transaction behavior prior to T?**

This required a careful and explicit choice of the **feature cutoff timestamp (T)**.

---

## Feature Window Definition

For any chosen timestamp `T`, features were constructed using a fixed historical window:

- **Feature window:** `[T − 60 days, T)`  
- **No gap window** was used  
- No data after `T` was included in feature construction  

This guarantees:

- Strict temporal causality  
- No overlap between feature data and churn outcomes  

---

## Systematic Selection of T

Rather than selecting `T` arbitrarily, multiple candidate cutoffs were evaluated:
T - {50%, 55%, 60%, 65%, 70% quantiles of transaction_date}


For each candidate `T`, **behavioral diagnostics** were computed *before* any model training.

### Diagnostics Used

- Median number of transactions:
  - churned users vs non-churned users  
- Percentage of churned users with **zero transactions** in the feature window  

These diagnostics were chosen specifically to detect **post-churn inactivity collapse**, which would make the task artificially easy and non-actionable.

---

## Diagnostic Results Summary

The diagnostics showed that:

- Several mid-range cutoffs (≈ 55–65%) resulted in:
  - median churned activity = 0  
  - more than 50% of churned users having zero transactions  
- These cutoffs were rejected as they primarily captured **already-inactive users**

The cutoff at:

> **T = 70th percentile of `transaction_date`**

was selected because it satisfied all of the following:

- Churned users still showed non-zero median activity  
- Inactivity collapse was materially reduced  
- Non-churn behavior remained stable  

This represented the best balance between **early warning** and **learnability** for this dataset.

---

## Feature Engineering (Week 3 Scope)

Features were intentionally kept simple and interpretable:

- `total_amount_paid` — total spend in the feature window  
- `num_transactions` — number of transactions  
- `num_cancellations` — count of cancellations  
- `total_plan_days` — total subscribed days  

All features were:

- Aggregated at the user (`msno`) level  
- Computed strictly within the feature window  
- Derived using memory-efficient Pandas operations suitable for large datasets  

---

## Model Choice

A **logistic regression** model was used as the baseline:

- Chosen for transparency and interpretability  
- Class imbalance handled via `class_weight="balanced"`

---

## Evaluation Philosophy

Evaluation emphasized **sanity and realism over raw score**:

- ROC–AUC was monitored but not aggressively optimized  
- Behavioral separation was inspected to ensure:
  - Gradual risk gradients  
  - Absence of near-deterministic inactivity signals  

Observed performance (ROC ≈ **0.6925**) was considered appropriate for an **early-warning baseline**.

---

## Artifact Freezing

Once `T` was finalized:

- A single, frozen dataset was generated

---

## What This Phase Achieved

By the end of Week 3:

- A leakage-aware churn prediction baseline was established  
- Feature construction was acceptable 
- A clean handoff point was created for richer behavioral modeling  

---

## Known Limitations (Intentional)

- Transaction data alone provides limited early behavioral signal  
- Churn definition is externally fixed by the dataset  
- Sequence-level patterns are not yet modeled  

These limitations are addressed explicitly in **Week 4**.

---

## Next Phase

**Week 4** will focus on:

- Integrating `user_logs.csv`  
- Measuring incremental lift over the Week-3 baseline  
- Validating whether fine-grained behavioral signals improve early churn detection  

---

## Summary

> **Week 3 established a disciplined, leakage-aware churn baseline using transaction data, prioritizing correctness and actionability over inflated accuracy.**






