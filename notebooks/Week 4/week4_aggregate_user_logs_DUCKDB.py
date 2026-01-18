import duckdb

FINAL_T = "2016-08-23"  # replace with your actual FINAL_T

con = duckdb.connect()

query = f"""
CREATE TABLE user_log_agg AS
SELECT
    msno,

    CASE
        WHEN date >= '{FINAL_T}'::DATE - INTERVAL 30 DAY
             AND date <  '{FINAL_T}'::DATE
            THEN 'recent'

        WHEN date >= '{FINAL_T}'::DATE - INTERVAL 90 DAY
             AND date <  '{FINAL_T}'::DATE - INTERVAL 60 DAY
            THEN 'mid'

        WHEN date >= '{FINAL_T}'::DATE - INTERVAL 180 DAY
             AND date <  '{FINAL_T}'::DATE - INTERVAL 150 DAY
            THEN 'long'

        ELSE NULL
    END AS win_bucket,

    SUM(num_25)      AS num_25,
    SUM(num_50)      AS num_50,
    SUM(num_75)      AS num_75,
    SUM(num_985)     AS num_985,
    SUM(num_100)     AS num_100,
    SUM(num_unq)     AS num_unq,
    SUM(total_secs)  AS total_secs

FROM read_csv_auto(
    'F:/AI Project/churn-retention-platform/data/raw/user_logs.csv',
    dateformat='%Y%m%d'
)

WHERE win_bucket IS NOT NULL

GROUP BY msno, win_bucket
"""

con.execute(query)

con.execute("""
COPY user_log_agg
TO 'F:/AI Project/churn-retention-platform/data/processed/user_log_aggregated_week4.csv'
WITH (HEADER, DELIMITER ',')
""")
