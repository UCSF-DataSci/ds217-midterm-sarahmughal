#!/bin/bash

# Assignment 5, Question 8: Pipeline Automation Script
# Run the clinical trial data analysis pipeline

# NOTE: This script assumes Q1 has already been run to create directories and generate the dataset
# NOTE: Q2 (q2_process_metadata.py) is a standalone Python fundamentals exercise, not part of the main pipeline
# NOTE: Q3 (q3_data_utils.py) is a library imported by the notebooks, not run directly
# NOTE: The main pipeline runs Q4-Q7 notebooks in order

mkdir -p reports
echo "Starting clinical trial data pipeline..." > reports/pipeline_log.txt

notebooks=("q4_exploration.ipynb" "q5_missing_data.ipynb" "q6_transformation.ipynb" "q7_aggregation.ipynb")

for notebook in "${notebooks[@]}"; do
    python3 -m nbconvert --to notebook --execute \
        --ExecutePreprocessor.kernel_name=python3 --ExecutePreprocessor.timeout=900 \
        "$notebook" --output "${notebook%.ipynb}.executed.ipynb" \
        >> reports/pipeline_log.txt 2>&1 || {
        echo "Error occurred while processing $notebook" >> reports/pipeline_log.txt
        exit 1
    }
    echo "Successfully processed $notebook" >> reports/pipeline_log.txt
done

echo "Pipeline complete!" >> reports/pipeline_log.txt
