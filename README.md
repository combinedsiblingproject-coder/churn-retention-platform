# Churn Prediction & Retention Platform

## Overview
This project is an API-first but GUI visualized churn prediction and marketing retention platform designed to help marketing and product teams identify at-risk users, understand churn drivers, and trigger targeted retention actions.

The goal is not just to train a machine learning model, but to design a
practical system that can be used by product, operations, and customer success teams
to identify at-risk users and take retention actions.

## Problem Statement
Marketing teams often lack actionable insights on which users are likely to churn and why, resulting in ineffective blanket campaigns and revenue loss.

## Solution
This platform predicts churn risk, explains the drivers behind churn, and recommends targeted retention actions via documented APIs. A Streamlit UI consumes these APIs for visualization and demo purposes.

## Target Users
- Marketing & Growth Teams
- CRM Systems
- Product Managers

## Key Features (Planned)
- Churn prediction (real-time and batch)
- Explainable churn drivers
- Retention action recommendations
- API-first architecture (FastAPI)
- Streamlit UI as API consumer

## Dataset (In 2 Phases)
- KKBox's Churn Dataset (https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data)
- eCommerce behavior data from multi category store (https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store

## Tools & Technologies
- Python (pandas, numpy, seaborn, matplotlib)
- Tableau (visual exploratory analysis)
- Jupyter Notebook

## Status

### Week 1: 
- Project setup and 
- Data exploration

### Week 2:
- Churn labels isolated and frozen
- Transaction-based behavioral features created
- Leakage and sanity checks completed
- Modeling dataset v1 finalized
- Backfill algorithm: used for transactions but not being utlized right now since we are creating baseline as of now & we can't do that if there are inferred data present along with real data - may give rise to synthetic signals: We will use backfill to investigae whether this improves our prediction or not & then decide to do this. ALternatively, the data may be some kind of marker which we don't have explanation for now & may be relvealed later as maybe - loyalities rewards or refunds. So, better to keep the data at this stage. So the process for cleaning: Model with raw data --> Measure impact --> Introduce corrections --> Validate gains
- 


