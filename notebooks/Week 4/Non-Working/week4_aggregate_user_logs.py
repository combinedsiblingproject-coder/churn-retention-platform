import pandas as pd
import numpy as np

# Taken from outut of previous notebook
FINAL_T = pd.to_datetime('2016-08-23')

WINDOWS = {
    "recent": (FINAL_T - pd.Timedelta(days=30), FINAL_T),
    "mid":    (FINAL_T - pd.Timedelta(days=90), FINAL_T - pd.Timedelta(days=60)),
    "long":   (FINAL_T - pd.Timedelta(days=180), FINAL_T - pd.Timedelta(days=150)),
}

# Initialize empty accumulator
aggregated = {}

def assign_window(date):
    if WINDOWS["recent"][0] <= date < WINDOWS["recent"][1]:
        return "recent"
    elif WINDOWS["mid"][0] <= date < WINDOWS["mid"][1]:
        return "mid"
    elif WINDOWS["long"][0] <= date < WINDOWS["long"][1]:
        return "long"
    else:
        return None

CHUNK_SIZE = 5_000_000  # safe for home PC

for chunk in pd.read_csv(
    "F:/AI Project/churn-retention-platform/data/raw/user_logs.csv",
    usecols=[
        "msno", "date",
        "num_25", "num_50", "num_75",
        "num_985", "num_100",
        "num_unq", "total_secs"
    ],
    chunksize=CHUNK_SIZE
):
    chunk["date"] = pd.to_datetime(chunk["date"], format="%Y%m%d")

    chunk["window"] = chunk["date"].apply(assign_window)
    chunk = chunk[chunk["window"].notna()]

    if chunk.empty:
        continue

    grouped = (
        chunk
        .groupby(["msno", "window"])
        .agg({
            "num_25": "sum",
            "num_50": "sum",
            "num_75": "sum",
            "num_985": "sum",
            "num_100": "sum",
            "num_unq": "sum",
            "total_secs": "sum"
        })
    )

    for idx, row in grouped.iterrows():
        if idx not in aggregated:
            aggregated[idx] = row
        else:
            aggregated[idx] += row

# Convert to DataFrame
final = pd.DataFrame.from_dict(aggregated, orient="index")
final.reset_index(inplace=True)
final.rename(columns={"level_0": "msno", "level_1": "window"}, inplace=True)

final.to_csv(
    "F:/AI Project/churn-retention-platform/data/processed/user_log_aggregated_week4.csv",
    index=False
)
