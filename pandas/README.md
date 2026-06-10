# Data Analysis

# ʕ·ᴥ·ʔ

This project uses the Python `pandas` library to load, clean, and analyze car sales data.

## Project structure

```
├── data/
│   ├── car-sales.csv              # Raw, untouched source dataset
│   └── Exported-car-sales.csv     # Cleaned, processed output dataset
├── analysis.py                    # Main execution script for the pipeline
├── README.md                      # Project documentation (this file)
└── requirements.txt               # Project dependencies
```

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python analysis.py
```

## Notes

- `data/car-sales.csv` is the original car sales dataset.
- `data/Exported-car-sales.csv` is the processed/exported dataset.
- `analysis.py` reads and previews the raw dataset.
