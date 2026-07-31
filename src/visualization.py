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


