PERSONA_RULES = [

    {
        "name": "At-Risk Loyalist",
        "priority": 3,
        "conditions": {
            "payment": ["Critical"],
            "lifecycle": ["Steady", "Late"],
            "engagement": ["Strong"],
            "volatility": ["Ultra Low", "Low", "Medium", "High", "Extreme"]
        }
    },

    {
        "name": "Fading User",
        "priority": 3,
        "conditions": {
            "lifecycle": ["Late"],
            "engagement": ["Very Low"]
        }
    },

    {
        "name": "Payment-Friction User",
        "priority": 3,
        "conditions": {
            "payment": ["Critical","Friction"]
        }
    },

    {
        "name": "Impatient Explorer",
        "priority": 2,
        "conditions": {
            "lifecycle": ["New", "Activation"],
            "engagement": ["Low", "Very Low"],
            "volatility": ["Extreme"]
        }
    },

    {
        "name": "Bored Loyalist",
        "priority": 2,
        "conditions": {
            "lifecycle": ["Late"],
            "engagement": ["Average", "Low"],
            "volatility": ["Medium"]
        }
    },

    {
        "name": "New & Uncertain",
        "priority": 2,
        "conditions": {
            "lifecycle": ["New"],
            "engagement": ["Low"],
            "volatility": ["High"]
        }
    },

    {
        "name": "Curious Explorer",
        "priority": 1,
        "conditions": {
            "lifecycle": ["Activation", "Steady"],
            "engagement": ["Average"],
            "volatility": ["High"]
        }
    },

    {
        "name": "Loyal Enthusiast",
        "priority": 1,
        "conditions": {
            "lifecycle": ["Steady", "Late"],
            "engagement": ["Average", "Strong"],
            "volatility": ["Low", "Medium"]
        }
    },

    {
        "name": "Passive Listener",
        "priority": 1,
        "conditions": {
            "engagement": ["Strong"],
            "volatility": ["Ultra Low"]
        }
    },

    {
        "name": "Balanced Power User",
        "priority": 0,
        "conditions": {
            "lifecycle": ["Steady", "Late"],
            "engagement": ["Strong", "Average"],
            "volatility": ["Low", "Medium", "Ultra Low"]
        }
    }
]