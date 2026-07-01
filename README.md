# Python Excel & CSV Automation Tool
## Overview
This project automates Excel and CSV data processing using Python.
The tool reads records from a CSV file, performs data cleaning, removes duplicate records, handles missing values, calculates employee bonuses, and generates both CSV and Excel reports.

## Features

- Read CSV files
- Remove duplicate records
- Handle missing values
- Format employee names
- Calculate salary bonus
- Export cleaned CSV
- Generate Excel report
  
## Technologies Used

- Python
- Pandas
- OpenPyXL

## Installation

pip install pandas openpyxl

## usage
## Generate both CSV and Excel
python Automation_main.py -i <Input file path> -o <output file path> -f both
## Generate only CSV
python Automation_main.py -i <Input file path> -o <output file path> -f csv
## Generate only Excel
python Automation_main.py -i <Input file path> -o <output file path> -f excel

## Output

The processed files are generated in the output folder.

## Skills Demonstrated

- Data Cleaning
- CSV Processing
- Excel Automation
- Python Scripting
- Pandas
- OpenPyXL

## Future Improvements

- Excel formatting(eg:multiple sheet handling)
- Charts and dashboards
- Interactive GUI using Tkinter
- Automated email report generation
