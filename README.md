# Mage AI Orchestrated Project: Sports Data ETL Pipeline

This project is an example of using Mage AI to orchestrate an Extract, Transform, and Load (ETL) pipeline for sports data. The pipeline pulls data from a sports API, transforms it into a pandas DataFrame, and saves it as a CSV file. The CSV file is then uploaded to an AWS S3 bucket, where it can be accessed for further analysis or visualization in a Tableau dashboard.

## Overview

The project consists of the following steps:

1. **Extraction**: The data is recursively pulled from the sports API in JSON format using Mage AI's capabilities.
2. **Transformation**: The extracted JSON data is transformed into a pandas DataFrame using Mage AI's data manipulation capabilities.
3. **Loading**: The transformed DataFrame is saved as a CSV file.
4. **Uploading**: The CSV file is uploaded to an AWS S3 bucket.

## Prerequisites

To run this project, you need the following:

- Mage AI: Install and set up Mage AI in your environment.
- Sports API Access: Obtain access credentials or API keys for the sports API you want to fetch data from.
- AWS Account: Create an AWS account to use S3 for storing the CSV file.
- Tableau: Install Tableau to create a dashboard and connect it to the S3 bucket for data visualization.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Willowyboat2388/football-analytics.git
   cd football-analytics
   ```

2. Set up the Mage AI environment with the required dependencies.

3. Configure API access: Update the data_loaders files with your API credentials.

4. Configure AWS credentials: Set up your AWS credentials by following the AWS documentation.

5. Update the Mage AI pipeline definition: Modify the pipeline definition files  to specify the extraction, transformation, and loading steps according to your API and data requirements.

6. Run the Mage AI pipeline: Execute the pipeline definition using Mage AI to trigger the data extraction, transformation, and loading process.

## Directory Structure

The project directory has the following structure:

- `data_loaders/`: Configuration folder for the API access credentials and data loading step.
- `transformers/`: Directory for source code on the transformation steps of the pipeline.
- `data_exporters/`: Contains the source code for the exporting of the csv files of the project.
- `output/`: Directory to store the extracted and transformed data files.
- `io_config.yaml`: File to store AWS credentials file for S3 access.
- `metadata/`: Contains additional documentation on Mage setup.

## Usage

1. Set up the project as described in the "Getting Started" section.

2. Configure the API credentials in `io_config.yaml`.

3. Update the pipeline definitions accordingly to match your API and data requirements.

4. Execute the Mage AI pipeline using the following command in the root of the project:

   ```bash
   mage start
   ```

   This will trigger the data extraction, transformation, and loading process according to the defined steps.

5. Once the pipeline completes successfully, the transformed data will be saved as a CSV file in the `data/` directory and uploaded to the specified AWS S3 bucket.

6. Access the uploaded CSV file in the S3 bucket and connect it to your Tableau dashboard for visualization and analysis.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request or open an issue

 in the GitHub repository.