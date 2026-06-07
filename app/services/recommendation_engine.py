class RecommendationEngine:

    @staticmethod
    def generate(
        quality_info,
        anomaly_info,
        correlation_info
    ):

        recommendations = []

        if quality_info["missing_percentage"] > 5:

            recommendations.append(
                "Consider imputing missing values before analysis."
            )

        if quality_info["duplicate_rows"] > 0:

            recommendations.append(
                "Review and remove duplicate records."
            )

        if len(
            quality_info["sparse_columns"]
        ) > 0:

            recommendations.append(
                "Evaluate sparse columns for removal or imputation."
            )

        if anomaly_info["anomaly_percentage"] > 3:

            recommendations.append(
                "Investigate anomalous records before model training."
            )

        if len(
            correlation_info["top_correlations"]
        ) > 0:

            recommendations.append(
                "Leverage highly correlated features for predictive modeling."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Dataset appears healthy and ready for advanced analytics."
            )

        return recommendations