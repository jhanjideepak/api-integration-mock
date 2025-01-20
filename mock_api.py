from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)


@app.route("/api/fitness_data", methods=["GET"])
def get_fitness_data():
    """
    Simulate fitness data for n users.
    Returns JSON with a list of user data records.
    """

    # Generate synthetic data for 5 users
    data = []
    num_users = 5

    for user_id in range(1, num_users + 1):
        steps = np.random.randint(3000, 15000)
        heart_rate = np.random.randint(60, 100)
        active_minutes = np.random.randint(0, 181)
        calories_consumed = np.random.randint(1200, 4000)
        systolic_bp = np.random.randint(90, 181)
        diastolic_bp = np.random.randint(60, 121)

        data.append({
            "user_id": user_id,
            "steps": steps,
            "heart_rate": heart_rate,
            "active_minutes": active_minutes,
            "calories_consumed": calories_consumed,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp
        })

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
