# 🕵️ AI Data Detective

## Transforming Noisy Data into Actionable Insights

AI Data Detective is an intelligent analytics platform that automatically investigates tabular datasets and uncovers hidden patterns, anomalies, relationships, and business insights.

Built for the **Microsoft AI Hackathon 2026** under the theme:

> AI Meets Data: From Noise to Insight

Instead of requiring users to manually explore data, AI Data Detective performs an automated investigation and generates actionable findings.

---

## Problem Statement

Organizations generate massive amounts of data, but extracting meaningful insights often requires specialized analytical skills.

Many datasets contain:

* Missing values
* Duplicate records
* Hidden correlations
* Outliers
* Domain-specific patterns

These signals are often buried beneath noisy raw data.

AI Data Detective automates the discovery process and surfaces insights that teams can immediately act upon.

---

## Key Features

### 📊 Automated Data Profiling

* Dataset overview
* Column classification
* Missing value detection
* Duplicate detection
* Datetime detection

### 🎯 Domain Detection

Automatically identifies the dataset domain:

* Healthcare
* Real Estate
* Sales
* Finance
* Generic Business Data

### 💚 Data Health Assessment

Generates a health score based on:

* Missing values
* Duplicate records
* Sparse columns
* Overall data quality

### 🔍 Relationship Discovery

Identifies and ranks:

* Strong correlations
* Moderate correlations
* Potential predictive relationships

### 🚨 Anomaly Detection

Uses Isolation Forest to identify:

* Suspicious records
* Outliers
* Potential data quality issues

### 🧠 AI-Powered Investigation

Uses Large Language Models to generate:

* Business insights
* Risks
* Opportunities
* Confidence scores
* Recommended actions

### 📈 Interactive Visualizations

* Correlation Heatmaps
* Missing Value Analysis
* Feature Explorer
* Distribution Analysis
* Boxplots

### ✅ Recommendation Engine

Provides actionable next steps such as:

* Data cleaning suggestions
* Missing value handling
* Anomaly investigation
* Feature engineering opportunities

---

## System Architecture

![Architecture](architecture.png)

---

## Technology Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Isolation Forest

### Visualizations

* Matplotlib
* Seaborn

### AI Models

* Groq API (Llama 3.3 70B)

### Development Tools

* GitHub Copilot
* ChatGPT

---

## Project Structure

```text
AI-Data-Detective/
│
├── app/
│   ├── services/
│   │   ├── anomaly_detector.py
│   │   ├── correlation_analyzer.py
│   │   ├── data_loader.py
│   │   ├── domain_detector.py
│   │   ├── evidence_builder.py
│   │   ├── insight_generator.py
│   │   ├── profiler.py
│   │   ├── quality_analyzer.py
│   │   ├── recommendation_engine.py
│   │   └── visualizer.py
│
├── streamlit_app.py
├── requirements.txt
├── architecture.png
├── .gitignore
└── README.md
```

---

## Installation

```bash
git clone <repository-url>

cd AI-Data-Detective

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run Locally

```bash
streamlit run streamlit_app.py
```

---

## Workflow

```text
Upload Dataset
      ↓
Data Profiling
      ↓
Domain Detection
      ↓
Quality Assessment
      ↓
Relationship Discovery
      ↓
Anomaly Detection
      ↓
Evidence Aggregation
      ↓
AI Investigation
      ↓
Recommendations & Insights
```

---

## Future Enhancements

* Document Investigation (PDF, DOCX, TXT)
* Retrieval-Augmented Generation (RAG)
* Feature Importance Analysis
* SHAP Explainability
* Azure OpenAI Integration
* Multi-Document Intelligence
* Dataset + Document Fusion Analysis

---

## Hackathon Compliance

This project was developed during the hackathon period and leverages AI-assisted development tools including GitHub Copilot and ChatGPT. All external libraries and APIs are properly disclosed.

---

## Author

Chethan Kashyap
Vinay Desai