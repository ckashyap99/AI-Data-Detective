# 🕵️ AI Data Detective

> Turning Raw Data into Actionable Intelligence with the Power of AI

AI Data Detective is an AI-powered analytics platform that investigates both **structured datasets** and **unstructured documents** to uncover hidden insights, anomalies, risks, patterns, and actionable recommendations.

Built for the **Microsoft AI Hackathon 2026**, the platform helps users transform noisy data into meaningful business intelligence with minimal effort.

---

## 🚀 Problem Statement

Organizations generate massive amounts of data every day:

- CSV and Excel datasets
- Reports and PDFs
- Meeting notes
- Research papers
- Operational records

However, extracting valuable insights from this data often requires specialized skills and significant manual effort.

AI Data Detective bridges this gap by automatically investigating data and documents, surfacing insights that might otherwise remain hidden.

---

## 💡 Solution

AI Data Detective provides two investigation engines:

### 📊 Structured Data Investigation

Upload any CSV or Excel file and automatically discover:

- Dataset profiling
- Domain detection
- Data quality assessment
- Missing value analysis
- Correlation discovery
- Anomaly detection
- Interactive visualizations
- AI-generated business insights
- Actionable recommendations

---

### 📄 Document Investigation (RAG)

Upload PDF, DOCX, or TXT documents and:

- Extract document content
- Generate semantic embeddings
- Perform vector-based retrieval
- Generate AI investigation reports
- Ask questions using natural language
- Receive evidence-backed answers

---

# 🏗️ System Architecture

![Architecture](architecture.png)

---

# 🔍 Key Features

## 📊 Structured Data Analytics

### Data Profiling
- Dataset overview
- Column classification
- Data type detection
- Missing value analysis

### Domain Detection

Automatically identifies domains such as:

- Healthcare
- Finance
- Real Estate
- Sales
- Retail
- Generic Business Data

### Data Quality Analysis

Calculates:

- Health Score
- Missing Data %
- Duplicate Rows
- Sparse Columns

### Correlation Discovery

Identifies:

- Strong feature relationships
- Hidden patterns
- Potential predictors

### Anomaly Detection

Detects:

- Outliers
- Abnormal records
- Data quality issues

### AI Insight Generation

Generates:

- Business insights
- Impact analysis
- Risks
- Recommendations

---

## 📄 Document Intelligence (RAG)

### Supported Documents

- PDF
- DOCX
- TXT

### Retrieval-Augmented Generation

Pipeline:

```text
Document
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Semantic Retrieval
    ↓
LLM Analysis
```

### Investigation Report

Automatically generates:

- Executive Summary
- Key Topics
- Important Numbers
- Risks
- Recommended Actions
- Confidence Assessment

# 🧠 AI & ML Components

## Structured Data Pipeline

- Profiling Engine
- Domain Detector
- Quality Analyzer
- Correlation Analyzer
- Anomaly Detector
- Recommendation Engine
- Evidence Builder
- Insight Generator

---

## Document Intelligence Pipeline

- Document Loader
- Text Chunker
- Embedding Generator
- Chroma Vector Store
- Semantic Retriever
- Document Investigator
- Question Answering Engine

---

# 🛠️ Technology Stack

## Frontend

- Streamlit

## Data Processing

- Pandas
- NumPy
- Scikit-Learn

## Visualization

- Matplotlib

## LLM

- Groq API(reference) or Microsoft AI Ecosystem Compatible
- Llama 3.3 70B Versatile

## Embeddings

- Sentence Transformers
- all-MiniLM-L6-v2

## Vector Database

- ChromaDB

## Document Processing

- PyMuPDF
- python-docx

## Development

- GitHub Copilot

---

# 📂 Project Structure

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
│   │
│   └── rag/
│       ├── document_loader.py
│       ├── document_investigator.py
│       ├── qa_engine.py
│       ├── text_chunker.py
│       └── vector_store.py
│
├── data/
│   └── chroma_db/
│
├── architecture.png
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/ckashyap99/AI-Data-Detective.git

cd AI-Data-Detective
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run streamlit_app.py
```

---

# 📈 Example Use Cases

### Real Estate Analytics

Upload housing datasets and discover:

- Property value drivers
- Market anomalies
- Geographic patterns

---

### Healthcare Data Analysis

Analyze:

- Patient records
- Disease indicators
- Clinical datasets

---

### Sales Intelligence

Identify:

- Revenue drivers
- Regional trends
- Customer behavior patterns

---

### Financial Reports

Upload annual reports and:

- Generate executive summaries
- Extract risks
- Ask questions about financial performance

---

# 🔮 Future Enhancements

- SHAP Explainability
- Multi-document RAG
- Agentic Investigation Workflows
- Azure OpenAI Integration
- Power BI Integration
- Report Export (PDF)
- Real-Time Data Monitoring

---

# 🤖 AI Tools Used

The following AI tools were used during development:

- GitHub Copilot (Coding Assistant)
- Groq LLM
- ChatGPT

---

# 👨‍💻 Author

**Chethan Kashyap**,
**Vinay Desai**

Built for the Microsoft AI Hackathon 2026.

---

# 🎯 Theme Alignment

### AI Meets Data: From Noise to Insight

AI Data Detective transforms noisy, messy, structured and unstructured data into actionable intelligence through automated investigation, pattern discovery, anomaly detection, semantic search, and AI-generated recommendations.