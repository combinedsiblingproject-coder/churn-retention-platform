import joblib
from services.utils import get_percentile_bucket

# -------------------------------
# LOAD DISTRIBUTIONS
# -------------------------------
dist = joblib.load("config/distributions.pkl")

ENG_THRESH = dist["engagement"]   # [20,40,60,80]
VOL_THRESH = dist["volatility"]
TIME_THRESH = dist["time_signal"]


# -------------------------------
# MAIN CONTEXT BUILDER
# -------------------------------

def build_user_context(user, stats):

    engagement_score = compute_engagement_score(user)
    volatility_score = compute_volatility(user)

    return {
        "payment": bucket_payment_status(
            user["is_auto_renew"],
            user["remaining_days"],
            stats
        ),
        "lifecycle": bucket_lifecycle(user["tenure_days"]),
        "engagement": bucket_engagement(engagement_score),
        "volatility": bucket_volatility(volatility_score)
    }


# -------------------------------
# ENGAGEMENT SCORE
# -------------------------------

def compute_engagement_score(user):

    total_events = (
        user["recent_num_985"] +
        user["recent_num_100"] +
        user["recent_num_75"] +
        user["recent_num_50"] +
        user["recent_num_25"]
    )

    if total_events == 0:
        return 0

    completion_ratio = (
        user["recent_num_985"] +
        user["recent_num_100"] +
        user["recent_num_75"]
    ) / total_events

    # -------------------------------
    # CASE 1 — OLD USERS
    # -------------------------------
    if user["tenure_days"] >= 120:

        time_ratio = (
            user["recent_total_secs"] /
            max(1, (90 - user["remaining_days"]))
        ) / max(1, (user["mid_total_secs"] / 60))

        return 0.5 * completion_ratio + 0.5 * time_ratio

    # -------------------------------
    # CASE 2 — NEW USERS
    # -------------------------------
    else:

        raw_time = (
            user["recent_total_secs"] /
            max(1, (90 - user["remaining_days"]))
        )

        percentile_score = get_percentile_bucket(raw_time, TIME_THRESH)

        return 0.8 * completion_ratio + 0.2 * percentile_score


# -------------------------------
# ENGAGEMENT BUCKET
# -------------------------------

def bucket_engagement(score):

    if score < ENG_THRESH[1]:
        return "Very Low"
    elif score < ENG_THRESH[2]:
        return "Low"
    elif score < ENG_THRESH[3]:
        return "Average"
    else:
        return "Strong"


# -------------------------------
# VOLATILITY SCORE
# -------------------------------

def compute_volatility(user):

    total = (
        user["recent_num_985"] +
        user["recent_num_100"] +
        user["recent_num_75"] +
        user["recent_num_50"] +
        user["recent_num_25"]
    )

    if total == 0:
        return 0

    score = (
        0.2 * (user["recent_num_25"] / total) +
        0.2 * (user["recent_num_unq"] / total) +
        0.3 * (user["recent_num_25"] / max(1, (user["recent_num_985"] + user["recent_num_100"]))) +
        0.2 * (user["recent_num_unq"] / max(1, user["recent_num_100"])) +
        0.1 * ((user["recent_num_50"] + user["recent_num_75"]) / total)
    )

    return score


# -------------------------------
# VOLATILITY BUCKET
# -------------------------------

def bucket_volatility(score):

    if score < VOL_THRESH[0]:
        return "Ultra Low"
    elif score < VOL_THRESH[1]:
        return "Low"
    elif score < VOL_THRESH[2]:
        return "Medium"
    elif score < VOL_THRESH[3]:
        return "High"
    else:
        return "Extreme"


# -------------------------------
# PAYMENT STATUS
# -------------------------------

def bucket_payment_status(auto_renew, remaining_days, stats):

    if auto_renew == 0:

        mean = stats["no_auto_mean"]
        std = stats["no_auto_std"]

        if remaining_days > 7:
            return "Stable"

        elif remaining_days <= (mean - (1.05) * std):
            return "Critical"
        
        else:
            return "Friction"

    else:

        mean = stats["auto_mean"]
        std = stats["auto_std"]

        if remaining_days > 7:
            return "Stable"

        elif remaining_days <= (mean - (1.02) * std):
            return "Critical"
        
        else:
            return "Friction"
        


# -------------------------------
# LIFECYCLE
# -------------------------------

def bucket_lifecycle(tenure_days):

    if tenure_days < 90:
        return "New"
    elif tenure_days <= 150:
        return "Activation"
    elif tenure_days <= 240:
        return "Steady"
    else:
        return "Late"


# -------------------------------
# TIME BUCKET
# -------------------------------

def get_time_bucket(days_to_expiry):

    if days_to_expiry > 7:
        return "T-7-"
    elif 3 <= days_to_expiry <= 7:
        return "T-7:3"
    elif 0 <= days_to_expiry <= 2:
        return "T-2:0"
    else:
        return "T+1"