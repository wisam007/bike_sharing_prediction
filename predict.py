import pandas as pd

from config import MODEL_PATH
from src.persistence import load_model
from src.inference import predict


def main():
    # Load the exported .pkl model
    model = load_model(MODEL_PATH)

    sample = pd.DataFrame([
    {
        "season": "spring",
        "yr": 0,
        "mnth": "mar",
        "holiday": 0,
        "weekday": "fri",
        "workingday": 1,
        "weathersit": "clear",
        "temp": 22.14,
        "hum": 52.5217,
        "windspeed": 15.478139,
    }
])

    sample2 = pd.DataFrame([
            {
                "season": "spring",
                "yr": 0,
                "mnth": "jan",
                "holiday": 0,
                "weekday": "sat",
                "workingday": 0,
                "weathersit": "mist_cloudy",
                "temp": 14.110847,
                "hum": 80.5833,
                "windspeed": 10.749882,
            }
        ])

    prediction = predict(model, sample)
    prediction2 = predict(model, sample2)


    print(f"Predicted rentals: {prediction[0]:.0f}")
    print(f"Predicted rentals2: {prediction2[0]:.0f}")



if __name__ == "__main__":
    main()