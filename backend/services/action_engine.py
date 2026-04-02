from config.action_config import ACTIONS

def get_action(persona, risk, time_bucket):

    try:
        return ACTIONS[risk][persona][time_bucket]
    except:
        return ["No Action"]


# -------------------------------
# Following was simple action model and has been discarded, using above function to fetch actions instead.
# -------------------------------

'''
def get_recommended_action(risk, context):

    payment = context["payment_state"]
    lifecycle = context["lifecycle_stage"]
    engagement = context["engagement_strength"]
    volatility = context["volatility"]
    loyalty = context["loyalty"]
    fatigue = context["fatigue_flag"]

    # --- START SIMPLE (you will refine later) ---

    # HIGH RISK USERS
    if risk == "High":

        if payment == "Critical":
            return "Immediate retention call / offer discount"

        if payment == "Friction-Exposed":
            return "Send payment reminder + incentive"

        if engagement == "Weak":
            return "Re-engagement campaign (email/push)"

        if fatigue:
            return "Reduce frequency + personalized content"

        return "General retention campaign"


    # MEDIUM RISK USERS
    elif risk == "Medium":

        if engagement == "Moderate":
            return "Nudge engagement via recommendations"

        if volatility == "Volatile":
            return "Stabilize experience (curated playlists)"

        return "Monitor + soft nudges"


    # LOW RISK USERS
    else:

        if loyalty == "Loyal":
            return "Upsell premium / long-term plan"

        return "No action / maintain experience"

    # --- END SIMPLE ---'''