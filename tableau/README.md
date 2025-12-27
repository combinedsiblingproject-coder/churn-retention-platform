## EDA Methodology

EDA was conducted with a pragmatic, PM-oriented mindset focused on decision readiness rather than exhaustive statistical analysis.

### Tableau was used for:
- Distribution analysis
- Segment comparisons
- Time-based trend exploration
- Visual outlier 

## Limitations & Assumptions
- Tableau analysis was performed on sampled or aggregated data for performance reasons
- Exact metrics for large-scale logs were computed using Python chunking
- EDA focused on decision readiness, not full statistical validation


### Python was used for:
- Missing value quantification
- Cardinality checks
- Scale-sensitive log analysis (chunking)
- Leakage risk detection

For large event-level datasets (user_logs), a mixed strategy was applied:
- 2–5% sampling for visual pattern discovery
- Chunk-based scans for exact metrics where required
