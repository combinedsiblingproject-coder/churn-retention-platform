# User Risk Segmentation & Action Engine

A lightweight decision system that classifies users into risk personas and recommends targeted actions using behavioral signals and rule-based + model-driven logic.

---

## Problem & User

Subscription-based platforms struggle to identify *which users are at risk* and *what action should be taken* before churn actually happens.

Due to nature of the dataset, the churn rentention systems either:

* Rely on delayed signals (post-churn analysis) - so leakge
* And produce scores without actionable insights
* No way to tell if actions are actually useful or not

### Target User

* Product Managers / Growth Teams
* CRM / Retention teams

### Core Problem

There is no simple, interpretable system that:

1. Converts raw behavioral signals into meaningful user states
2. Maps those states to clear, actionable interventions

---

## What This Project Does

This project builds a simplified **user intelligence layer** that:

* Transforms raw user attributes into 4 derived behavioral signals:

  * Payment Health
  * Lifecycle Stage
  * Engagement Level
  * Volatility

* Maps users into personas based on these signals

* Assigns recommended actions for each persona

* Computes a risk score (baseline model)

👉 The focus is not just prediction, but **decision enablement**

---

## Demo

![Demo](demo.gif)

---

## Key Features

* Rule-based persona classification using derived behavioral signals
* ML driven Risk scoring layer for prioritization
* Action mapping engine for targeted interventions
* Time-window based analysis (user state can evolve)
* Lightweight and interpretable (no black-box dependency)

---

## Sample Output

Example user classification:

```
{
  "payment": "Critical",
  "lifecycle": "Late",
  "engagement": "Very Low",
  "volatility": "Ultra Low",
  "persona": "At-Risk Passive",
  "risk_score": 0.82,
  "recommended_action": "Winback Campaign"
}
```

---

## How It Works (User Flow)

1. User data is ingested (subset / simulated dataset)
2. Derived metrics are computed
3. User is mapped to a persona
4. Risk score is assigned
5. Recommended action is generated

---

## System Architecture

The system is divided into 4 layers:

1. Data Layer

   * Input: User attributes (subset / simulated)
   * Note: Full dataset (320M logs) not used in Phase-1

2. Feature Engineering Layer

   * Derived metrics computed from raw inputs

3. Decision Layer

   * Persona mapping rules
   * Risk scoring model (ML)

4. Action Layer

   * Persona → Action mapping

---

## Key Decisions & Trade-offs

### 1. Used Derived Signals Instead of Raw Data

* Improves interpretability
* Trade-off: Loss of granularity

### 2. Rule-Based Personas (Phase-1)

* Faster iteration and explainability
* Trade-off: Limited coverage of edge combinations

### 3. Subset / Simulated Data

* Enabled rapid prototyping
* Trade-off: Reduced real-world fidelity

### 4. Ignored Payments Table

* Simplified initial modeling
* Trade-off: Missing critical financial signals

### 5. No Real-time Pipeline

* Batch-style processing used
* Trade-off: Not production-ready

---

## How I’d Measure Success

If deployed, success would be measured by:

* Reduction in churn rate
* Increase in action conversion rate
* Accuracy of risk classification
* Time taken to identify at-risk users
* Coverage of users with actionable recommendations

---

## Edge Cases & Failure Handling

* Missing inputs → default values assigned (fallback logic)
* Negative tenure_days → assigned neutral risk (0.5)
* Unknown persona combinations → no action assigned
* Time-window shifts → persona may change dynamically

These are partially handled and will be improved in future phases.

---

## Current Limitations (Phase-1)

### Data & Modeling

* Full dataset (~320M logs) not used; only subset/simulated data
* Payments table completely ignored (critical signal gap)
* Derived metrics are approximations, not statistically validated
* Users enrolled after cutoff time included during training

### System Design

* Not all combinations of derived features map to a persona
  → Some users receive no recommended action
* Actions are rule-based and brittle
* No handling for metric computation failures

### Data Integrity

* Missing inputs default to zero values
* Use of customer name instead of unique user_id (risk of duplication)

### Analytical Gaps

* Certain anomalies unexplained (e.g., high remaining_days for non-auto-renew users)
* Cashback / incentive-driven behavioral patterns not explored

### Performance Constraints

* Development done on limited compute → constrained experimentation

---

## Phase-2 Roadmap

### 1. Data & Identity Improvements

* Replace customer name with unique user_id
* Integrate payments table into feature set

### 2. Model Evolution

* Simulated A/B testing framework:

  * Compare intervention strategies
  * Optimize actions based on outcomes
* Automated model improvement using synthetic feedback loops

### 3. Decision Intelligence

* CLTV-based prioritization
* Budget-aware intervention allocation

### 4. Dynamic Risk Updating

* Update risk scores based on actions taken
* Avoid full retraining via incremental updates

### 5. Persona Coverage Expansion

* Ensure all feature combinations map to actions
* Reduce “no-action” states

### 6. Robustness

* Handle missing/invalid metric scenarios
* Improve stability of action recommendations

---

## Setup

1. Clone repo
2. Install dependencies
3. Run app script for both backend and frontend

```
Step 1:
0. Go to the directory - churn-retention-platform\backend
A. Activate backend venv
B. Run command - uvicorn app:app --reload   

Step 2:
0. Go to the directory - churn-retention-platform\frontend
A. Activate front venv
B. Run command - streamlit run app.py 
```

Supplementary data Link:https://drive.google.com/file/d/12T-Yj-D8YwZua-OraIc2B_pywrGC2grQ/view?usp=sharing
The data as-is must be unzipped and placed inside: 'data\processed'

---

## Project Positioning

This is a **Phase-1 prototype / MVP** focused on:

* Decision logic design
* Interpretability
* Fast iteration

It is not production-ready and intentionally prioritizes speed over completeness.

---

## Learnings

* Translating raw data into meaningful signals is non-trivial
* Covering all user states is harder than building initial rules
* Actionability is more important than prediction accuracy
* Trade-offs between speed and rigor are unavoidable in early stages
