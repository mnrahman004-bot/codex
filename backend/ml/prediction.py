"""ML demand prediction utilities using Linear Regression."""
from datetime import datetime

import numpy as np
from sklearn.linear_model import LinearRegression


def predict_demand(history, days_ahead=7):
    """Train a linear model on transaction demand and predict future quantity."""
    demand_points = []
    for entry in history:
        date_value = datetime.strptime(str(entry["date"])[0:10], "%Y-%m-%d").toordinal()
        signed_qty = entry["quantity"] if entry["type"] == "OUT" else -entry["quantity"]
        demand_points.append((date_value, signed_qty))

    if len(demand_points) < 2:
        return {"predicted_quantity": 0, "trend": "insufficient_data"}

    x = np.array([p[0] for p in demand_points]).reshape(-1, 1)
    y = np.array([p[1] for p in demand_points])

    model = LinearRegression()
    model.fit(x, y)

    future_x = np.array([[x[-1][0] + days_ahead]])
    prediction = max(0, float(model.predict(future_x)[0]))
    trend = "increasing" if model.coef_[0] > 0 else "decreasing"

    return {"predicted_quantity": round(prediction, 2), "trend": trend}
