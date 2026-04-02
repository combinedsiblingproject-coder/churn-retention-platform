import joblib

model=joblib.load("model/churn_model_week5.pkl")

print(model.feature_name_)