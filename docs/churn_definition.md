# Churn Definition

## Business Question
Which users are likely to stop renewing their subscription in the near future?

## Label Source
We use the churn label provided in train.csv.

## Churn Meaning
A user is considered churned if they do not renew their subscription
within the defined prediction window = expired subscription & 30+ days & still no active subscription

## Prediction Window
We predict churn over the next 30 & 60 days.

## Observation Window
We use user behavior and transactions from the past 30/60/90 days.

## Why this definition?
- Allows proactive intervention
- Avoids future data leakage

## What is not considered churn
- Temporary inactivity
- Reduced usage without cancellation
- Plan downgrade without exit
