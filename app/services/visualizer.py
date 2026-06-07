import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Visualizer:

    @staticmethod
    def correlation_heatmap(df):

        numeric_df = df.select_dtypes(
            include=["int64", "float64", "int32", "float32"]
        )

        if numeric_df.shape[1] < 2:
            return None

        corr_matrix = numeric_df.corr()

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        sns.heatmap(
            corr_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            ax=ax
        )

        plt.title(
            "Correlation Heatmap"
        )

        return fig
    
    @staticmethod
    def missing_values_chart(df):

        missing = (
            df.isnull()
            .sum()
            .sort_values(ascending=False)
        )

        missing = missing[
            missing > 0
        ]

        if len(missing) == 0:
            return None

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        missing.plot.bar(ax=ax)

        plt.title(
            "Missing Values by Column"
        )

        plt.ylabel(
            "Count"
        )

        return fig
    
    @staticmethod
    def feature_distribution(df, column):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(8, 4))

        df[column].dropna().hist(
            bins=30,
            ax=ax
        )

        plt.title(
            f"Distribution of {column}"
        )

        return fig
    
    @staticmethod
    def boxplot(df, column):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(
            figsize=(8, 2)
        )

        ax.boxplot(
            df[column].dropna(),
            vert=False
        )

        plt.title(
            f"Boxplot of {column}"
        )

        return fig
    
    @staticmethod
    def category_distribution(
        df,
        column
    ):

        import matplotlib.pyplot as plt

        counts = (
            df[column]
            .value_counts()
            .head(10)
        )

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        counts.plot.bar(ax=ax)

        plt.title(
            f"{column} Distribution"
        )

        return fig