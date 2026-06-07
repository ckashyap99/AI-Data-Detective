import pandas as pd


class CorrelationAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        numeric_df = df.select_dtypes(
            include=["int64", "float64", "int32", "float32"]
        )

        if numeric_df.shape[1] < 2:
            return {
                "top_correlations": []
            }

        corr_matrix = numeric_df.corr(numeric_only=True)

        IGNORE_KEYWORDS = [
            "id",
            "latitude",
            "longitude",
            "lat",
            "lon"
        ]

        correlations = []

        columns = corr_matrix.columns

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):

                corr_value = corr_matrix.iloc[i, j]

                if pd.isna(corr_value):
                    continue

                strength = "Weak"

                if abs(corr_value) >= 0.8:
                    strength = "Very Strong"

                elif abs(corr_value) >= 0.6:
                    strength = "Strong"

                elif abs(corr_value) >= 0.4:
                    strength = "Moderate"

                feature_1 = columns[i]
                feature_2 = columns[j]

                feature_1_lower = feature_1.lower()
                feature_2_lower = feature_2.lower()

                if any(
                    keyword in feature_1_lower
                    for keyword in IGNORE_KEYWORDS
                ):
                    continue

                if any(
                    keyword in feature_2_lower
                    for keyword in IGNORE_KEYWORDS
                ):
                    continue
                
                if abs(corr_value) < 0.3:
                    continue

                correlations.append({
                    "feature_1": columns[i],
                    "feature_2": columns[j],
                    "correlation": round(corr_value, 3),
                    "absolute_correlation": abs(corr_value),
                    "strength": strength
                })

        correlations.sort(
            key=lambda x: x["absolute_correlation"],
            reverse=True
        )

        return {
            "top_correlations": correlations[:10]
        }