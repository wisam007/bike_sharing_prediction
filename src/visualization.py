from pathlib import Path
import seaborn as sns

import matplotlib.pylab as plt 
import pandas as pd


def plot_cnt_distribution(df:pd.DataFrame,output_dir:Path,)->Path:
    # 1. Distribution of Target Variable (cnt)
    output_dir.mkdir(parents=True,exist_ok=True)
    output_path = output_dir / "distribution_of_cnt.png"

    plt.figure(figsize=(8, 4))

    sns.histplot(df['cnt'], kde=True, color='skyblue', bins=30)

    plt.title('Distribution of Total Bike Rentals (cnt)')
    plt.xlabel('Total Rental Count')
    plt.ylabel('Frequency')

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()
    return output_path
def plot_distribution_with_kde(df:pd.DataFrame,output_dir:Path)->Path:
    # 2. Distribution Plots (Histograms with KDE)
    output_dir.mkdir(parents=True,exist_ok=True)
    output_path = output_dir / 'eda_distributions.png'

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    num_vars = ['temp', 'hum', 'windspeed', 'casual','registered', 'cnt']
    colors = ['#2b5c8f', '#3690c0', '#67a9cf', '#02818a', '#e66101', '#5e3c99']

    for i, var in enumerate(num_vars):
        row, col = divmod(i, 3)
        sns.histplot(df[var], kde=True, ax=axes[row, col], color=colors[i], bins=25)
        axes[row, col].set_title(f'Distribution of {var}')
        axes[row, col].set_xlabel(var)
        axes[row, col].set_ylabel('Frequency')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)

    plt.close()
    return output_path


def plot_categorical_distributions(df: pd.DataFrame,output_dir: Path,) -> Path:
    """
    Plot count distributions for categorical variables.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "categorical_distributions.png"

    categorical_features = [
        "season",
        "mnth",
        "weekday",
        "weathersit",
        "yr",
        "workingday",
        "holiday",
    ]

    fig, axes = plt.subplots(3, 3, figsize=(18, 14))
    axes = axes.flatten()

    for i, feature in enumerate(categorical_features):

        order = sorted(df[feature].dropna().unique())

        sns.countplot(
            data=df,
            x=feature,
            order=order,
            ax=axes[i],
            color="#4C72B0",
        )

        axes[i].set_title(f"{feature} Distribution")
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel("Count")
        axes[i].tick_params(axis="x", rotation=45)

        # Show the count above each bar
        for container in axes[i].containers:
            axes[i].bar_label(
                container,
                fontsize=8,
            )

    # Remove any unused subplot axes
    for j in range(len(categorical_features), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

    return output_path

def plot_outlier_subplots(df:pd.DataFrame,output_dir:Path)->Path:
    output_dir.mkdir(parents=True,exist_ok=True)
    output_path = output_dir / "weather_outlier_subplots.png"

    # 3. Boxplots for Outlier Analysis across Continuous Features
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=df[['temp', 'atemp', 'hum', 'windspeed']], palette='Set2', ax=ax)
    ax.set_title('Boxplots of Continuous Weather Features (Raw Data)')
    ax.set_ylabel('Normalized / Actual Scale Units')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)


    plt.close()
    return output_path

def plot_categorical_boxplots(df:pd.DataFrame,output_dir:Path)->Path:
    output_dir.mkdir(parents=True,exist_ok=True)
    output_path = output_dir / "eda_boxplots_categorical.png"
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    weather_map = {1: 'Clear/Partly Cloudy', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain'}
    df_temp = df.copy()
    df_temp['season_label'] = df_temp['season'].map(season_map)
    df_temp['weather_label'] = df_temp['weathersit'].map(weather_map)

    sns.boxplot(x='season_label', y='cnt', data=df_temp, palette='Spectral', order=['Spring', 'Summer', 'Fall', 'Winter'], ax=axes[0, 0])
    axes[0, 0].set_title('Total Demand (cnt) by Season')

    sns.boxplot(x='weather_label', y='cnt', data=df_temp, palette='Blues_r', ax=axes[0, 1])
    axes[0, 1].set_title('Total Demand (cnt) by Weather Condition')

    sns.boxplot(x='workingday', y='cnt', data=df_temp, palette='Set2', ax=axes[1, 0])
    axes[1, 0].set_title('Total Demand (cnt) by Working Day (0=No, 1=Yes)')

    sns.boxplot(x='holiday', y='cnt', data=df_temp, palette='Set1', ax=axes[1, 1])
    axes[1, 1].set_title('Total Demand (cnt) by Holiday (0=No, 1=Yes)')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)

    plt.close()
    return output_path

def plot_feature_rel_scatterplot(df:pd.DataFrame,output_dir:Path)->Path:
    output_dir.mkdir(parents=True,exist_ok=True)
    output_path = output_dir / 'eda_scatterplots.png'

    # 5. Scatter Plots for Feature Relationships
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    sns.scatterplot(x='temp', y='cnt', hue='yr', data=df, palette='coolwarm', alpha=0.7, ax=axes[0])
    axes[0].set_title('Temperature vs Rental Count (by Year)')

    sns.scatterplot(x='hum', y='cnt', hue='weathersit', data=df, palette='viridis', alpha=0.7, ax=axes[1])
    axes[1].set_title('Humidity vs Rental Count (by Weather)')

    sns.scatterplot(x='windspeed', y='cnt', hue='season', data=df, palette='Set1', alpha=0.7, ax=axes[2])
    axes[2].set_title('Windspeed vs Rental Count (by Season)')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)

    plt.close()

    return output_path
def plot_correlation_heatmap(df:pd.DataFrame,output_dir:Path)->Path:
    output_dir.mkdir(parents=True,exist_ok=True)
    output_path = output_dir / 'eda_correlation_heatmap.png'
    # Create a correlation matrix for continuous variables
    plt.figure(figsize=(11, 8))
    raw_corr = df.drop(columns=['instant','dteday']).corr()

    sns.heatmap(raw_corr, annot=True, fmt=".2f", cmap='vlag', linewidths=0.5, cbar=True)
    plt.title('Raw Dataset Correlation Heatmap (Prior to Cleaning)')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)

    plt.close()
    return output_path


def plot_actual_vs_predicted_residual(
        residual_df,
        output_dir):

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        output_dir /
        "actual_vs_predicted.png"
    )


    plt.figure(figsize=(7,5))


    sns.scatterplot(
        data=residual_df,
        x="actual",
        y="predicted"
    )


    plt.plot(
        [
            residual_df["actual"].min(),
            residual_df["actual"].max()
        ],
        [
            residual_df["actual"].min(),
            residual_df["actual"].max()
        ]
    )


    plt.title(
        "Actual vs Predicted Bike Rentals"
    )


    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()

    return output_path


def plot_residuals(
        residual_df,
        output_dir):


    output_path = (
        output_dir /
        "residual_plot.png"
    )


    plt.figure(figsize=(7,5))


    sns.scatterplot(
        data=residual_df,
        x="predicted",
        y="residual"
    )


    plt.axhline(0)


    plt.title(
        "Residuals vs Predictions"
    )


    plt.tight_layout()


    plt.savefig(
        output_path,
        dpi=300
    )


    plt.close()

    return output_path

def plot_residual_distribution(
        residual_df,
        output_dir):


    output_path = (
        output_dir /
        "residual_distribution.png"
    )


    plt.figure(figsize=(7,5))


    sns.histplot(
        residual_df["residual"],
        kde=True
    )


    plt.title(
        "Residual Distribution"
    )


    plt.tight_layout()


    plt.savefig(
        output_path,
        dpi=300
    )


    plt.close()

    return output_path


#================================================
def plot_model_comparison(results_df: pd.DataFrame, output_dir: Path):
    """
    Compare regression models using Test R² and RMSE.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    plt.style.use("seaborn-v0_8-whitegrid")

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    df_sorted_r2 = results_df.sort_values(by="R2", ascending=True)
    df_sorted_rmse = results_df.sort_values(by="RMSE", ascending=False)

    colors_r2 = [
        "#3498db" if "Extra" not in m and "Ada" not in m else "#e74c3c"
        for m in df_sorted_r2["Model"]
    ]

    axes[0].barh(
        df_sorted_r2["Model"],
        df_sorted_r2["R2"],
        color=colors_r2,
        edgecolor="black",
        alpha=0.85,
    )

    axes[0].set_title(
        "Model Comparison: Test $R^2$ Score",
        fontsize=13,
        fontweight="bold",
    )

    axes[0].set_xlabel("Test $R^2$")

    for index, value in enumerate(df_sorted_r2["R2"]):
        axes[0].text(
            value + 0.003,
            index,
            f"{value:.4f}",
            va="center",
            fontsize=9,
            fontweight="bold",
        )

    colors_rmse = [
        "#2ecc71" if "Extra" not in m and "Ada" not in m else "#e67e22"
        for m in df_sorted_rmse["Model"]
    ]

    axes[1].barh(
        df_sorted_rmse["Model"],
        df_sorted_rmse["RMSE"],
        color=colors_rmse,
        edgecolor="black",
        alpha=0.85,
    )

    axes[1].set_title(
        "Model Comparison: RMSE",
        fontsize=13,
        fontweight="bold",
    )

    axes[1].set_xlabel("RMSE")

    for index, value in enumerate(df_sorted_rmse["RMSE"]):
        axes[1].text(
            value + 10,
            index,
            f"{value:.1f}",
            va="center",
            fontsize=9,
            fontweight="bold",
        )

    plt.tight_layout()

    filepath = output_dir / "model_comparison.png"

    plt.savefig(filepath, dpi=300)

    plt.close()

    return filepath

#===================================================
def plot_actual_vs_predicted(
    trained_models: dict,
    results_df: pd.DataFrame,
    X_test,
    y_test,
    output_dir: Path,
):
    """
    Actual vs Predicted scatter plots
    for the four best models.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    plt.style.use("seaborn-v0_8-whitegrid")

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    axes = axes.flatten()

    top_models = (
        results_df.sort_values("R2", ascending=False)
        .head(4)["Model"]
        .tolist()
    )

    for i, model_name in enumerate(top_models):

        pipeline = trained_models[model_name]

        y_pred = pipeline.predict(X_test)

        r2 = results_df.loc[
            results_df["Model"] == model_name,
            "R2",
        ].values[0]

        rmse = results_df.loc[
            results_df["Model"] == model_name,
            "RMSE",
        ].values[0]

        axes[i].scatter(
            y_test,
            y_pred,
            alpha=0.7,
            edgecolors="black",
            s=40,
        )

        axes[i].plot(
            [y_test.min(), y_test.max()],
            [y_test.min(), y_test.max()],
            "r--",
            linewidth=2,
        )

        axes[i].set_title(
            f"{model_name}\n"
            f"R²={r2:.4f}, RMSE={rmse:.1f}",
            fontsize=11,
            fontweight="bold",
        )

        axes[i].set_xlabel("Actual Bike Rentals")

        axes[i].set_ylabel("Predicted Bike Rentals")

    plt.tight_layout()

    filepath = output_dir / "models_actual_vs_predicted.png"

    plt.savefig(filepath, dpi=300)

    plt.close()

    return filepath



#======================================================



