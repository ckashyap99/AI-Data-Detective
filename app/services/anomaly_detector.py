import pandas as pd
from sklearn.ensemble import IsolationForest


class AnomalyDetector:

    @staticmethod
    def detect(df: pd.DataFrame):

        numeric_df = df.select_dtypes(
            include=["int64", "float64", "int32", "float32"]
        )

        # Need at least 2 numeric columns
        if numeric_df.shape[1] < 2:
            return {
                "anomaly_count": 0,
                "anomaly_percentage": 0,
                "anomaly_indices": []
            }

        # Fill missing values
        numeric_df = numeric_df.fillna(
            numeric_df.median()
        )

        model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

        predictions = model.fit_predict(
            numeric_df
        )

        anomaly_indices = (
            numeric_df[predictions == -1]
            .index
            .tolist()
        )

        anomaly_count = len(anomaly_indices)

        anomaly_percentage = round(
            (anomaly_count / len(df)) * 100,
            2
        )

        return {
            "anomaly_count": anomaly_count,
            "anomaly_percentage": anomaly_percentage,
            "anomaly_indices": anomaly_indices[:20]
        }