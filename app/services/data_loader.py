import pandas as pd
from pathlib import Path


class DataLoader:
    """
    Handles loading datasets from supported file formats.
    """

    SUPPORTED_EXTENSIONS = [".csv", ".xlsx"]

    @staticmethod
    def load_file(uploaded_file):
        """
        Loads a CSV or Excel file into a Pandas DataFrame.

        Parameters
        ----------
        uploaded_file : UploadedFile
            Streamlit uploaded file object

        Returns
        -------
        pd.DataFrame
        """

        file_extension = Path(uploaded_file.name).suffix.lower()

        if file_extension not in DataLoader.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file format: {file_extension}. "
                f"Supported formats are {DataLoader.SUPPORTED_EXTENSIONS}"
            )

        try:
            if file_extension == ".csv":
                df = pd.read_csv(uploaded_file)

            elif file_extension == ".xlsx":
                df = pd.read_excel(uploaded_file)

            if df.empty:
                raise ValueError("Uploaded dataset is empty.")

            return df

        except Exception as e:
            raise ValueError(f"Error loading file: {str(e)}")