# import pandas as pd

# from config import MODEL_PATH
# from src.persistence import load_model
# from src.inference import predict


# def main():
#     # Load the exported .pkl model
#     model = load_model(MODEL_PATH)

#     # Apply the UCI dataset normalizations to raw weather values
#     sample = pd.DataFrame([
#     {
#         "season": "spring",
#         "yr": 0,
#         "mnth": "mar",
#         "holiday": 0,
#         "weekday": "fri",
#         "workingday": 1,
#         "weathersit": "clear",
#         "temp": 22.14,
#         "hum": 52.5217,
#         "windspeed": 15.478139 ,
#     }
#     ])

#     sample2 = pd.DataFrame([
#             {
#                 "season": "spring",
#                 "yr": 0,
#                 "mnth": "jan",
#                 "holiday": 0,
#                 "weekday": "sat",
#                 "workingday": 0,
#                 "weathersit": "mist_cloudy",
#                 "temp": 14.110847,
#                 "hum": 80.5833 ,
#                 "windspeed": 10.749882 ,
#             }
#         ])

#     prediction = predict(model, sample)
#     prediction2 = predict(model, sample2)

#     print(f"Predicted rentals: {prediction[0]:.0f}")
#     print(f"Predicted rentals2: {prediction2[0]:.0f}")

# if __name__ == "__main__":
#     main()

import pandas as pd

from config import MODEL_PATH
from src.persistence import load_model
from src.inference import predict


def main():
    # Load the exported .pkl model
    model = load_model(MODEL_PATH)

    # Path to the processed training data
    data_path = "data/processed/bike_sharing_processed.csv"
    
    try:
        # Load the complete dataset
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: The file {data_path} was not found. Please check your path.")
        return

    # Check for target column (e.g., 'rentals' or last column)
    # Replace 'rentals' with the exact name of your target column if it differs
    target_column = "rentals" 
    
    if target_column not in df.columns:
        # Fallback to the very last column if the explicit name isn't found
        target_column = df.columns[-1]

    # Isolate features and target values
    X_features = df.drop(columns=[target_column])
    y_actual = df[target_column]

    # Generate model predictions for the entire DataFrame at once
    predictions = predict(model, X_features)

    # Print header for observation
    print(f"{'Row':<8} | {'Actual Rentals':<15} | {'Predicted Rentals':<17} | {'Difference':<10}")
    print("-" * 60)

    # Loop through data to observe individual performance
    for idx, (actual, pred) in enumerate(zip(y_actual, predictions)):
        diff = actual - pred
        print(f"{idx + 1:<8} | {actual:<15.0f} | {pred:<17.0f} | {diff:<+10.0f}")

if __name__ == "__main__":
    main()

