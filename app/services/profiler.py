import pandas as pd


class DataProfiler:

    @staticmethod
    def profile_dataset(df: pd.DataFrame) -> dict:
        """
        Generate basic profiling information for a dataset.
        """

        # Numeric columns
        numeric_cols = df.select_dtypes(
            include=["int64", "float64", "int32", "float32"]
        ).columns.tolist()

        # Categorical columns
        categorical_cols = df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        # Datetime columns
        datetime_cols = []

        date_keywords = [
            "date",
            "time",
            "timestamp",
            "created",
            "updated",
            "dob",
            "birth"
        ]

        for col in df.columns:

            if pd.api.types.is_numeric_dtype(df[col]):
                continue

            col_lower = col.lower()

            if not any(keyword in col_lower for keyword in date_keywords):
                continue

            converted = pd.to_datetime(
                df[col],
                errors="coerce"
            )

            valid_ratio = converted.notna().mean()

            if valid_ratio > 0.8:
                datetime_cols.append(col)
                
        categorical_cols = [
            col
            for col in categorical_cols
            if col not in datetime_cols
        ]

        # Missing values per column
        missing_values = (
            df.isnull()
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

        # Duplicate rows
        duplicate_rows = int(df.duplicated().sum())

        # print("\nCOLUMN DTYPES:")
        # print(df.dtypes)

        return {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "numeric_columns": numeric_cols,
            "categorical_columns": categorical_cols,
            "datetime_columns": datetime_cols,
            "missing_values": missing_values,
            "duplicate_rows": duplicate_rows
        }