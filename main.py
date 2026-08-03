from config import RAW_DATA,JSON_DIR,TABLE_DIR,FIGURE_DIR,PROCESSED_DATA
from config import MODEL_PATH

from src.loader import load_data
from src.eda import (
    dataset_summary,
    descriptive_statistics,
    missing_value_report
)
from src.reporting import (save_csv,save_json,save_dataframe)
from src.visualization import (plot_cnt_distribution,
                               plot_distribution_with_kde,
                               plot_outlier_subplots,
                               plot_categorical_boxplots,
                               plot_correlation_heatmap,
                               plot_feature_rel_scatterplot,
                               plot_actual_vs_predicted_residual,
                               plot_residuals,
                               plot_residual_distribution,
                               plot_actual_vs_predicted,
                               plot_model_comparison,
                               plot_categorical_distributions

)
from src.features import split_data,split_features_target,build_preprocessor,get_feature_count
from src.preprocessing import preprocess_data
from src.modeling import get_models,train_model
from src.persistence import save_model
from src.evaluation import evaluate_model
import pandas as pd

def main():
    df = load_data(RAW_DATA)

    summary = dataset_summary(df)

    stats = descriptive_statistics(df)

    missing = missing_value_report(df)


    cnt_plot = plot_cnt_distribution(df,FIGURE_DIR)
    all_distributions = plot_distribution_with_kde(df,FIGURE_DIR)
    outlier_subplots = plot_outlier_subplots(df,FIGURE_DIR)
    catagorical_boxplots = plot_categorical_boxplots(df,FIGURE_DIR)
    heatmap_plot = plot_correlation_heatmap(df,FIGURE_DIR)
    scatter_plots = plot_feature_rel_scatterplot(df,FIGURE_DIR)
    save_json(summary, JSON_DIR / "dataset_summary.json")
    plot_categorical_distributions(df, FIGURE_DIR)

    save_csv(stats, TABLE_DIR / "descriptive_statistics.csv")

    processed_df, quality = preprocess_data(df)

    save_json(
    quality,
    JSON_DIR / "data_quality.json",)

    
    save_dataframe(
    processed_df,
    PROCESSED_DATA,
)




    print(summary)
    print(stats)
    print(missing)



   

    X, y = split_features_target(processed_df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    preprocessor = build_preprocessor()

    models = get_models()

    results = []

    trained_models = {}

    p = get_feature_count(preprocessor,X_train)

    for name, model in models.items():

        pipeline, elapsed = train_model(
            model,
            preprocessor,
            X_train,
            y_train,
        )
        trained_models[name] = pipeline

        metrics,actual, predicted = evaluate_model(
            pipeline,
            X_train,
            X_test,
            y_train,
            y_test,
            elapsed,
            name,
        )

        # metrics["Model"] = name
        print(metrics)

        results.append(metrics)

    sorted_data = sorted(
        results,
        key=lambda x: (-x["R2"], x["RMSE"])
)
    best_model_name = sorted_data[0]["Model"]
    best_pipeline = trained_models[best_model_name]

    results_df = pd.DataFrame(results)

    residual_df = pd.DataFrame(
        {
            "actual": actual,
            "predicted": predicted,
            "residual": actual - predicted
        }
    )


    save_csv(
        residual_df,
        TABLE_DIR / "residual_analysis.csv"
    )

    
    plot_actual_vs_predicted_residual(
        residual_df,
        FIGURE_DIR
    )

    plot_residuals(
        residual_df,
        FIGURE_DIR
    )

    plot_residual_distribution(
        residual_df,
        FIGURE_DIR
    )
        

    save_json(
        sorted_data,
        JSON_DIR / "evalutaion_score.json",)
    save_model(best_pipeline, MODEL_PATH)

    print(f"Best model saved to {MODEL_PATH}")

    best_model_info = {
        "Model": sorted_data[0]["Model"],
        "R2": sorted_data[0]["R2"],
        "RMSE": sorted_data[0]["RMSE"],
        "MAE": sorted_data[0]["MAE"],
        "Training Time": sorted_data[0]["Training Time (s)"]
}

    save_json(
        best_model_info,
        JSON_DIR / "best_model.json"
    )
    plot_model_comparison(
        results_df,
        FIGURE_DIR,
    )

    plot_actual_vs_predicted(
        trained_models,
        results_df,
        X_test,
        y_test,
        FIGURE_DIR,
    )



if __name__ == "__main__":
    main()
