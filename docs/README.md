# EDA Insights

## Overview
The goal is to discover 
- Outliers/Impossible Values
- Missing Values
- Identifying Categorical Variables 
- Aggregate Snapshot & Skewness (Normalization/Scaling Requirements)
- Variance 
- Time Gaps/Impossible Ranges/Format


## Members Data
- City (21 Unique counts --> Can be categorical Data) --> Very Heavy Skewness --> City=1 has 7 Lac out of 10.5, next  has between 0.5 to 0.75
- bd (205 Unique counts --> Can be categorical Data) --> Large Invalid Data -->  38% of data where Age<10 or Age>100. Practically uselss
- gender -->  61% times no data for this column. Useless
- registered_via (16 Unique counts --> Can be categorical Data) --> Reasonable Box Plot = Maybe route to registration can be impactful & upon churn, may again be used to retarget --> But 3-4 values each contribute 3 lac each (Total-10.5) --> so very big-3/4 like
- registration_init_time --> From 20040326 to 20170429 --> Maybe we can use to see stickiness of old customers


## Transactions Data
- Payment Method --> Cases where listPrice!=actualPaid & all times listPrice=0 along with paymentPlanDay=0 --> Need to insert both of them using actualPaid standard observed values
- Need to remove instances where days & planPrice & actualPaid are all 0 with isCancel=1
- REFUND --> Can it be refund when listPrice!=0 & actualPaid=0 and is_cancel=1 --> Can we model it somehow?
- Effect of paymentMethod/planDay on planPrice>Actual --> LoyaltyRewards? --> All these cases account for, so NO.

- txnDate<expiryDate --> (for is_cancel=0:expiry= txndata+30) & (for is_cancel=1: expiry=txndata)
- transaction_date = (20150101 to 20170228)	&& membership_expire_date = (19700101 to  20170331)--> Clean txnDate<expiryDate
- isCancel=0 & txndata+planDay>ExpiryDate --> Probe & what to do?
- isCancel=0 & txndata+planDay<ExpiryDate --> Probe & what to do?
- Context for 3339 Duplicate rows - Probe & What to do?


## Users Data
- num_25 to num_100 is not unique song but total including repeated
- Total Seconds are negative for some --> Need cleaning
