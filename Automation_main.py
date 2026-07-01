import os
import pandas as pd
import argparse
import logging

logging.basicConfig(
    level=logging.DEBUG,    
)
logger = logging.getLogger(__name__)


# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Process employee CSV file and generate cleaned CSV and Excel report."
)
parser.add_argument(
    "-i",
    "--input",
    help="Path to the input CSV file"
)

parser.add_argument(
    "-o",
    "--output",
    help="Output folder path"
)

parser.add_argument(
    "-f",
    "--format",
    type=str.lower,
    choices=["csv", "excel", "both"],
    default="both",
    help="Output format: csv, excel, or both (default: both)"
)

args = parser.parse_args()
INPUT_FILE = args.input
OUTPUT_FOLDER = args.output
OUTPUT_FORMAT = args.format

logger.info("Loading CSV file...")

df = pd.read_csv(INPUT_FILE)

logger.info(f"Original Records: {len(df)}")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing Employee ID
df = df.dropna(subset=["Employee ID"])

# Fill missing department values
df["Department"] = df["Department"].fillna("Not Assigned")

# Standardize employee names
df["Employee Name"] = df["Employee Name"].str.title()

# Calculate Salary Bonus (10%)
df["Bonus"] = df["Salary"] * 0.10

# Save cleaned CSV
if OUTPUT_FORMAT in ["csv", "both"]:
    csv_output = os.path.join(OUTPUT_FOLDER)
    df.to_csv(csv_output, index=False)
    logger.info(f"CSV saved to: {csv_output}")

# Save Excel report
if OUTPUT_FORMAT in ["excel", "both"]:
    excel_output = os.path.join(OUTPUT_FOLDER)
    logger.info(f"Excel report saved to: {excel_output}")

    with pd.ExcelWriter(excel_output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Employees")

logger.info("Processing Complete!")

