class EvidenceBuilder:

    @staticmethod
    def build(
        profile,
        domain_info,
        quality_info,
        correlation_info,
        anomaly_info
    ):

        top_missing = []

        missing_values = profile["missing_values"]

        for column, count in missing_values.items():

            if count > 0:

                top_missing.append({
                    "column": column,
                    "missing_count": count
                })

        return {

            "domain": domain_info["domain"],

            "dataset_summary": {
                "rows": profile["rows"],
                "columns": profile["columns"]
            },

            "quality_metrics": {
                "health_score":
                    quality_info["health_score"],

                "missing_percentage":
                    quality_info["missing_percentage"],

                "duplicate_rows":
                    quality_info["duplicate_rows"],

                "sparse_columns":
                    quality_info["sparse_columns"]
            },

            "correlation_findings":
                correlation_info[
                    "top_correlations"
                ][:3],

            "anomaly_findings": {
                "anomaly_count":
                    anomaly_info["anomaly_count"],

                "anomaly_percentage":
                    anomaly_info[
                        "anomaly_percentage"
                    ]
            },

            "missing_value_findings":
                top_missing[:5]
        }