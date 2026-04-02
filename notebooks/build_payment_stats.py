import duckdb
import joblib

INPUT_PATH = "data/processed/membersTransactionsUserAggregated.csv"

con = duckdb.connect()

print("Computing payment stats...")

query = f"""
SELECT
    AVG(remaining_days) FILTER (WHERE is_auto_renew = 1 and remaining_days!=999) AS auto_mean,
    STDDEV(remaining_days) FILTER (WHERE is_auto_renew = 1  and remaining_days!=999) AS auto_std,

    AVG(remaining_days) FILTER (WHERE is_auto_renew = 0  and remaining_days!=999) AS no_auto_mean,
    STDDEV(remaining_days) FILTER (WHERE is_auto_renew = 0  and remaining_days!=999) AS no_auto_std

FROM '{INPUT_PATH}'
WHERE tenure_days >= 0
  AND remaining_days >= 0
"""

result = con.execute(query).fetchone()

stats = {
    "auto_mean": result[0],
    "auto_std": result[1],
    "no_auto_mean": result[2],
    "no_auto_std": result[3]
}

joblib.dump(stats, "backend/config/payment_stats.pkl")

print("✅ payment_stats.pkl created")

print(stats)
