# Backfilling payment_plan_days & plan_list_price

## Overview
- The goal is to backfill data where is_cancel=0 & (payment_plan_days=0 & plan_list_price=0 & actual_amount_paid>0)
- The approach is to use confidence to decide this and this should be high in order to have good quality data
- >90% --> autofill data, 85-90 --> indicate confidence level, Rest --> don't fill data
- There are 3 parameters for calculating confidence:
- confidence = 0.45 × price_alignment+ 0.35 × expiry_alignment+ 0.20 × frequency_score

## Signal 1: Price alignment (strongest signal)
- How close the plan’s list price is to actual_amount_paid.
- Perfect match → score close to 1 & Increasing deviation → score decreases
- Tolerance of 5%
- price_alignment = 1 − (candidate_price − actual_amount_paid) / candidate_price

## Signal 2: Expiry alignment (2nd strongest signal)
- How close the plan’s list price is to actual_amount_paid.
- Whether adding the candidate plan duration to the correct baseline (previous expiry or transaction date) lands near the recorded expiry.
- Tolerance of 2 days in mismatch
- Close alignment → plan duration is plausible & Large mismatch → plan duration is wrong
- expiry_alignment =  1 − (expected_expiry − actual_expiry) / tolerance_days

## Signal 3: Historical frequency (weakest signal)
- How often this exact (payment_plan_days, plan_list_price) combination has appeared historically. Rare plans are more likely to be noise or edge cases: penalized but not eliminated
- Normalized frequency (0 to 1)
- frequency_score = frequency_of_plan / max_frequency_across_plans

## Rejection before even calculating confidence
- Expiry mismatch exceeds tolerance
- Price difference exceeds tolerance

## Why we did NOT use ML here
- ML would require: Labeled “correct” backfills & Ground truth for corrupted rows: Neither exists - Strong indication of hallucination.

## Q --> how has the calculation/arriving at 'candidate_price' & 'expected_expiry' happened? algo for it?
- 
