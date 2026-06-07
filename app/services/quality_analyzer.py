import pandas as pd


class QualityAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        total_cells = df.shape[0] * df.shape[1]

        missing_cells = int(df.isnull().sum().sum())

        missing_pct = (
            missing_cells / total_cells * 100
            if total_cells > 0 else 0
        )

        duplicate_rows = int(df.duplicated().sum())

        sparse_columns = []

        for col in df.columns:

            missing_ratio = (
                df[col].isnull().sum() / len(df)
            )

            if missing_ratio > 0.5:
                sparse_columns.append(col)

        score = 100

        score -= min(missing_pct, 40)

        score -= min(duplicate_rows, 20)

        score -= len(sparse_columns) * 5

        score = max(0, round(score))

        return {
            "health_score": score,
            "missing_percentage": round(missing_pct, 2),
            "duplicate_rows": duplicate_rows,
            "sparse_columns": sparse_columns
        }