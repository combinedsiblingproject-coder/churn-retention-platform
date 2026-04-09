import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/recommend_by_user"
TOP_USERS_URL = "http://127.0.0.1:8000/top_users"

st.set_page_config(layout="wide")

# -----------------------------
# SESSION STATE
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if "selected_user" not in st.session_state:
    st.session_state.selected_user = None

# -----------------------------
# HEADER
# -----------------------------
st.title("🎯 Churn Retention Engine")
st.caption("Simulate retention strategies and explore churn risk across user lifecycle")

# -----------------------------
# NAVIGATION
# -----------------------------
col1, col2 = st.columns(2)

def nav_button(label, page_key, col):
    is_active = st.session_state.page == page_key
    btn_type = "primary" if is_active else "secondary"

    if col.button(label, type=btn_type, use_container_width=True):
        st.session_state.page = page_key

nav_button("📊 Top Users", "dashboard", col1)
nav_button("🎛️ Simulation", "simulation", col2)

# ============================================
# 📊 DASHBOARD
# ============================================
if st.session_state.page == "dashboard":

    st.header("📊 High Risk Users")

    try:
        if "top_users" not in st.session_state:
            response = requests.get(TOP_USERS_URL)
            df = pd.DataFrame(response.json())

            df["risk_level"] = df["risk"].apply(
                lambda x: "High" if x > 0.7 else "Medium" if x > 0.3 else "Low"
            )

            st.session_state.top_users = df

        df = st.session_state.top_users

        # -------- Pagination --------
        page = st.number_input("Page", min_value=1, max_value=4, value=1)
        start = (page - 1) * 5
        end = start + 5
        subset = df.iloc[start:end]

        # -------- User List --------
        for _, row in subset.iterrows():

            col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])

            col1.write(f"👤 {row['user_id']}")
            col2.write(f"Risk: {row['risk_level']}")
            col3.write(f"Score: {round(row['risk'],2)}")

            if col4.button("View", key="view_" + row["user_id"]):
                st.session_state.selected_user = row["user_id"]
                st.session_state.page = "detail"

            if col5.button("Simulate", key="sim_" + row["user_id"]):
                st.session_state.selected_user = row["user_id"]
                st.session_state.page = "simulation"

    except:
        st.error("Failed to load users")

    # -------- Better Risk Chart --------
    st.subheader("📈 Risk Segmentation")

    if "top_users" in st.session_state:

        df["bucket"] = df["risk"].apply(
            lambda x: "High" if x > 0.7 else "Medium" if x > 0.3 else "Low"
        )

        st.bar_chart(df["bucket"].value_counts())

        with st.expander("ℹ️ What does this mean?"):
            st.write("""
            High → Immediate intervention needed  
            Medium → Monitor & engage  
            Low → Stable users  
            """)

# ============================================
# 👤 DETAIL PAGE
# ============================================
elif st.session_state.page == "detail":

    user_id = st.session_state.selected_user

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"

    response = requests.post(API_URL, json={"user_id": user_id})

    if response.status_code == 200:

        data = response.json()

        st.header(f"👤 User: {user_id}")

        col1, col2, col3 = st.columns(3)

        col1.metric("Persona", data["persona"])
        col2.metric("Risk", data["risk"])
        col3.metric("Time Bucket", data["time_bucket"])

        # -------- Behavioral Profile --------
        st.subheader("🧬 Behavioral Profile")

        context = data.get("context", {})

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("💳 Payment", context.get("payment", "-"))
        c2.metric("📆 Lifecycle", context.get("lifecycle", "-"))
        c3.metric("🎧 Engagement", context.get("engagement", "-"))
        c4.metric("📊 Volatility", context.get("volatility", "-"))

        # -------- Actions --------
        st.subheader("🎯 Recommended Actions")

        for action in data["actions"]:
            st.success(action)

        # -------- Explanation --------
        st.subheader("🧠 Why this?")

        st.info(data["explanation"])

    else:
        st.error(response.text)

# ============================================
# 🎛️ SIMULATION PAGE
# ============================================
elif st.session_state.page == "simulation":

    st.header("🎛️ User Simulation")

    default_user = st.session_state.selected_user or ""
    user_id = st.text_input("Enter User ID", value=default_user)

    time_options = {
        "More than 7 days": 10,
        "3 to 7 days": 5,
        "2 to 0 days": 2,
        "Expired": -1
    }

    selected = st.radio("Time to Expiry", list(time_options.keys()))
    days_override = time_options[selected]

    if user_id:

        with st.spinner("Simulating..."):

            payload = {
                "user_id": user_id,
                "override_days_to_expiry": days_override
            }

            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:

                data = response.json()

                col1, col2, col3 = st.columns(3)

                col1.metric("Persona", data["persona"])
                col2.metric("Risk", data["risk"])
                col3.metric("Time Bucket", data["time_bucket"])

                # -------- Behavioral Profile --------
                st.subheader("🧬 Behavioral Profile")

                context = data.get("context", {})

                c1, c2, c3, c4 = st.columns(4)

                c1.metric("💳 Payment", context.get("payment", "-"))
                c2.metric("📆 Lifecycle", context.get("lifecycle", "-"))
                c3.metric("🎧 Engagement", context.get("engagement", "-"))
                c4.metric("📊 Volatility", context.get("volatility", "-"))

                # -------- Actions --------
                st.subheader("Actions")

                for a in data["actions"]:
                    st.success(a)

                # -------- Explanation --------
                st.subheader("Why")

                st.info(data["explanation"])

            else:
                st.error(response.text)

# ============================================
# FOOTER
# ============================================
st.divider()

st.markdown("### 🔗 Project Links")

col1, col2, col3 = st.columns(3)

col1.markdown("[📂 GitHub Repo](https://github.com/Big4SiRaz/churn-retention-platform)")
col2.markdown("[📊 Dataset](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data)")
col3.markdown("[🚀 Live Demo](Please-Wait)")
