import pandas as pd
import streamlit as st

from app.services.data_loader import DataLoader
from app.services.profiler import DataProfiler
from app.services.domain_detector import DomainDetector
from app.services.quality_analyzer import QualityAnalyzer
from app.services.correlation_analyzer import CorrelationAnalyzer
from app.services.anomaly_detector import AnomalyDetector
from app.services.insight_generator import InsightGenerator
from app.services.evidence_builder import EvidenceBuilder
from app.services.visualizer import Visualizer
from app.services.recommendation_engine import RecommendationEngine


st.set_page_config(
    page_title="AI Data Detective",
    page_icon="🕵️",
    layout="wide"
)

st.title("🕵️ AI Data Detective")
st.write(
    "Upload any tabular dataset and let the detective investigate."
)

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:

    try:
        # Load dataset
        df = DataLoader.load_file(uploaded_file)

        st.success("Dataset loaded successfully!")

        # Generate profile
        profile = DataProfiler.profile_dataset(df)

        # Detect Domain
        domain_info = DomainDetector.detect_domain(df)

        # Quality Info
        quality_info = QualityAnalyzer.analyze(df)

        # Correlation Info
        correlation_info = CorrelationAnalyzer.analyze(df)

        # Anomaly Detection
        anomaly_info = AnomalyDetector.detect(df)

        # Recommendations
        recommendations = (
            RecommendationEngine.generate(
                quality_info,
                anomaly_info,
                correlation_info
            )
        )

        # Evidence
        evidence = EvidenceBuilder.build(
            profile,
            domain_info,
            quality_info,
            correlation_info,
            anomaly_info
        )

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📊 Overview",
                "🔍 Patterns",
                "📈 Visualizations",
                "🕵️ AI Investigation"
            ]
        )

        #######################################################################
        # OVERVIEW TAB
        #######################################################################

        with tab1:

            st.subheader("📋 Executive Summary")

            st.info(
                f"""
                **Domain:** {domain_info['domain']}

                **Health Score:** {quality_info['health_score']}/100

                **Anomalies Found:** {anomaly_info['anomaly_count']}

                **Strong Relationships Found:** {len(correlation_info['top_correlations'])}
                """
            )

            st.subheader("Dataset Preview")
            st.dataframe(
                df.head(),
                width="stretch"
            )

            st.subheader("🎯 Detected Domain")

            st.success(
                f"Detected Domain: {domain_info['domain']}"
            )

            score_df = pd.DataFrame(
                domain_info["scores"].items(),
                columns=["Domain", "Score"]
            )

            st.dataframe(
                score_df,
                width="stretch"
            )

            st.subheader("💚 Dataset Health")

            score = quality_info["health_score"]

            st.progress(
                quality_info["health_score"] / 100
            )

            if score >= 80:
                st.success(
                    f"Health Score: {score}/100"
                )

            elif score >= 60:
                st.warning(
                    f"Health Score: {score}/100"
                )

            else:
                st.error(
                    f"Health Score: {score}/100"
                )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Missing %",
                    quality_info["missing_percentage"]
                )

            with col2:
                st.metric(
                    "Duplicate Rows",
                    quality_info["duplicate_rows"]
                )

            if quality_info["sparse_columns"]:

                st.warning(
                    f"Sparse Columns (>50% missing): "
                    f"{quality_info['sparse_columns']}"
                )

            else:

                st.success(
                    "No sparse columns detected."
                )

            st.subheader("📦 Dataset Overview")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Rows",
                    profile["rows"]
                )

            with col2:
                st.metric(
                    "Columns",
                    profile["columns"]
                )

            st.subheader("🏷️ Column Classification")

            st.write(
                f"### Numeric Columns ({len(profile['numeric_columns'])})"
            )
            st.write(profile["numeric_columns"])

            st.write(
                f"### Categorical Columns ({len(profile['categorical_columns'])})"
            )
            st.write(profile["categorical_columns"])

            st.write(
                f"### Datetime Columns ({len(profile['datetime_columns'])})"
            )
            st.write(profile["datetime_columns"])

        #######################################################################
        # PATTERNS TAB
        #######################################################################

        with tab2:

            st.subheader("🔍 Relationship Discovery")

            if correlation_info["top_correlations"]:

                corr_df = pd.DataFrame(
                    correlation_info["top_correlations"]
                )

                st.dataframe(
                    corr_df[
                        [
                            "feature_1",
                            "feature_2",
                            "correlation",
                            "strength"
                        ]
                    ],
                    width="stretch"
                )

            else:

                st.info(
                    "Not enough numeric columns for correlation analysis."
                )

            st.subheader("🚨 Suspicious Records")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Anomalies Found",
                    anomaly_info["anomaly_count"]
                )

            with col2:
                st.metric(
                    "Anomaly %",
                    anomaly_info["anomaly_percentage"]
                )

            if anomaly_info["anomaly_count"] > 0:

                anomaly_rows = df.loc[
                    anomaly_info["anomaly_indices"]
                ]

                st.write(
                    "Sample Anomalous Records"
                )

                st.dataframe(
                    anomaly_rows.head(10),
                    width="stretch"
                )

            st.subheader("✅ Recommended Next Actions")

            for idx, rec in enumerate(
                recommendations,
                start=1
            ):

                st.write(
                    f"{idx}. {rec}"
                )

        #######################################################################
        # VISUALIZATIONS TAB
        #######################################################################

        with tab3:

            st.subheader("🔥 Correlation Heatmap")

            heatmap_fig = (
                Visualizer.correlation_heatmap(df)
            )

            if heatmap_fig:
                st.pyplot(heatmap_fig)

            st.subheader(
                "📉 Missing Values Analysis"
            )

            missing_fig = (
                Visualizer.missing_values_chart(df)
            )

            if missing_fig:
                st.pyplot(missing_fig)

            st.subheader(
                "🔬 Interactive Feature Explorer"
            )

            selected_column = st.selectbox(
                "Choose a column",
                df.columns
            )

            if pd.api.types.is_numeric_dtype(
                df[selected_column]
            ):

                st.write(
                    "### Summary Statistics"
                )

                st.dataframe(
                    df[selected_column]
                    .describe()
                    .to_frame(),
                    width="stretch"
                )

                distribution_fig = (
                    Visualizer.feature_distribution(
                        df,
                        selected_column
                    )
                )

                st.pyplot(
                    distribution_fig
                )

                boxplot_fig = (
                    Visualizer.boxplot(
                        df,
                        selected_column
                    )
                )

                st.pyplot(
                    boxplot_fig
                )

            else:

                category_fig = (
                    Visualizer.category_distribution(
                        df,
                        selected_column
                    )
                )

                st.pyplot(
                    category_fig
                )

        #######################################################################
        # AI INVESTIGATION TAB
        #######################################################################

        with tab4:

            st.subheader(
                "🕵️ AI Detective Findings"
            )

            if st.button(
                "🕵️ Run AI Investigation"
            ):

                with st.spinner(
                    "Investigating dataset..."
                ):

                    insights = (
                        InsightGenerator.generate(
                            evidence
                        )
                    )

                    st.markdown(
                        insights
                    )

    except Exception as e:
        st.error(str(e))