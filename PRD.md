# Product Requirements Document (PRD)

## 1. Problem Statement

Subscription platforms lack a simple and interpretable system to identify at-risk users and take proactive actions.

Simple approaches for dataset are either:

* Focus only on prediction without actionability
* Depend on delayed or incomplete signals

---

## 2. Goals

* Build a system that converts raw user data into actionable insights
* Classify users into meaningful personas
* Assign clear, interpretable actions
* Enable prioritization via risk scoring

---

## 3. Non-Goals (Phase-1)

* Full-scale production deployment
* Real-time processing pipeline
* Deep learning or complex modeling
* Full dataset utilization (320M logs)

---

## 4. User Stories

1. As a Product Manager, I want to identify at-risk users early so that I can reduce churn
2. As a CRM Manager, I want recommended actions for each user segment so that campaigns are targeted
3. As a Growth Analyst, I want interpretable user segments so that I can understand behavior patterns

---

## 5. Functional Requirements

### Input

* User attributes (subset or simulated dataset)

### Processing

* Compute derived metrics:

  * Payment
  * Lifecycle
  * Engagement
  * Volatility

### Decisioning

* Map users to personas
* Assign risk score

### Output

* Persona classification
* Risk score
* Recommended action

---

## 6. Success Metrics

* % of users classified into personas
* % of users with assigned actions
* Accuracy of risk prioritization (relative ranking)
* Reduction in churn (future validation)

---

## 7. Constraints

* Limited compute resources
* Partial dataset usage
* Manual rule definitions

---

## 8. Assumptions

* Derived metrics approximate real behavioral signals
* Personas can represent meaningful user states
* Rule-based actions are sufficient for initial iteration

---

## 9. Risks

* Incomplete persona coverage
* Data quality issues
* Over-simplification of user behavior

---

## 10. Future Scope (Phase-2)

* A/B testing for intervention strategies
* Integration of payments data
* CLTV-based prioritization
* Dynamic risk updating
* Improved persona coverage
