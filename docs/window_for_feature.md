# Feature Windows
Compute features over multiple time windows to capture short-term and long-term behavior changes.

## Windows Used
- 30 days (recent behavior)
- 60 days (medium-term trend)
- 90 days (long-term engagement)

## Rationale
- Recent behavior captures immediate churn signals
- Longer windows capture habit formation and loyalty

## Feature Categories

### Transactional
- Total payments till date
- Number of renewals
- Average plan duration

### Behavioral
- Per duration/interval basis: (Each cateogy share) & (Total Seconds) --> Comparsion with progressive durations
- Total listening time
- Percentage of inactive days/total active days
- Percentage of inactive periods/total number of renewals+1
- short term/long term: Listening satisfaction OR Catalogue Research & satisfaction score

#### User-segmentation/User-modes
- 1. Easily Satisfied
- 2. Rarely satisfied
- 3. Too experimental 

### Tenure
- Account age
- Time since last renewal
