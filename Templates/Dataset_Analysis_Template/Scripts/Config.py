"""
Project Configuration File
--------------------------
Purpose: Central repository for all file paths and project settings.
Usage: Import this file in all analysis scripts to ensure consistency.
"""

import os
from pathlib import Path

# ==============================================================================
# 1. PROJECT STRUCTURE
# ==============================================================================

# Get the absolute path of the project root (one level up from this Scripts folder)
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define core directory paths
DATA_DIR = PROJECT_ROOT / "Data"
DOCS_DIR = PROJECT_ROOT / "Docs"
OUTPUTS_DIR = PROJECT_ROOT / "Outputs"
SCRIPTS_DIR = PROJECT_ROOT / "Scripts"

# Define sub-directories
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REFERENCE_DIR = DATA_DIR / "reference"

TABLES_DIR = OUTPUTS_DIR / "tables"
FIGURES_DIR = OUTPUTS_DIR / "figures"

# ==============================================================================
# 2. DATA CONFIGURATION (AI TO UPDATE)
# ==============================================================================

# Exact filename of the source file in Data/raw/
# [AI_INSTRUCTION]: Update this filename after user intake
RAW_DATA_FILE = "PLACEHOLDER_FILENAME.csv" 

# Define full paths (Do not modify)
RAW_DATA_PATH = RAW_DATA_DIR / RAW_DATA_FILE
CLEAN_DATA_PATH = PROCESSED_DATA_DIR / "cleaned_data.csv"

# ==============================================================================
# 3. ANALYSIS SETTINGS
# ==============================================================================

# Global settings for outputs
RANDOM_SEED = 42
FIGURE_SIZE = (10, 6)
DPI = 300

# Create directories if they don't exist (Safety Check)
dirs = [RAW_DATA_DIR, PROCESSED_DATA_DIR, REFERENCE_DIR, TABLES_DIR, FIGURES_DIR]
for d in dirs:
    d.mkdir(parents=True, exist_ok=True)

print(f"✅ Configuration loaded. Project Root: {PROJECT_ROOT}")
