
# Omics Analysis Demo - Python Pipeline
Simple omics data analysis pipeline that runs automatically on GitHub. Demonstrates sample-to-group mapping, group averaging, and result generation using Python + pandas.

## 🎯 What it does
Reads gene expression matrix (data/expression_matrix.csv)

Maps samples to conditions (data/samples.csv)

Calculates mean expression per group (control vs treated)

Saves results to results/group_means.csv

Runs automatically via GitHub Actions on every push!

## 📁 Structure

### omics-python-demo/
├── data/
│   ├── expression_matrix.csv  # Gene x Sample matrix
│   └── samples.csv           # Sample metadata
├── analysis.py               # Main analysis script
├── requirements.txt          # Python dependencies
└── .github/workflows/        # CI/CD pipeline
    └── omics-analysis.yml

## 🚀 Quick Start
Local run:

'''bash
pip install -r requirements.txt
python analysis.py

GitHub Actions: Push to main → workflow runs automatically → check Actions tab!

📊 Sample Output
text
**Results saved:** results/group_means.csv

        control  treated  log2FC
GeneA     11.0    29.0    1.40
GeneB      6.0    19.0    1.66
GeneC    105.0    92.5   -0.18



**Copy → `nano README.md` → Save → `git add .` → `git push`** 

**Result:** Beautiful GitHub page with colored code! 🎨
