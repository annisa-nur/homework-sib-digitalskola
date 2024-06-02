# PySpark Job with SparkSubmitOperator in Airflow

## Project Overview

This project involves creating an Airflow Directed Acyclic Graph (DAG) to run a PySpark job using the SparkSubmitOperator. The objective is to schedule and manage a PySpark job that performs a word count on a text file.

## Objective

- **Task**: Execute a PySpark job using SparkSubmitOperator in Airflow.
- **Goal**: Create an Airflow DAG to run a PySpark job using SparkSubmitOperator.

## Instructions

### 1. Setup Airflow
Ensure Airflow is correctly installed and configured in your environment. The installation in this project will be done in docker. So, it needs to create a `Dockerfile` and `docker-compose.yaml`. Then, we can set up the airflow configuration in `airflow.env` with your own secret-key and add file `.dockerignore`

### 2. Create PySpark Script
Create a simple PySpark script named `helloworld.py` and `wordcount.py` that counts the occurrences of each word in a text file `book.txt`.

### 3. Create a New DAG
Create a new Python file named `spark_airflow.py` in your Airflow `dags` directory.

### 4. Define the DAG
Define a DAG scheduled to run daily.

### 5. Use SparkSubmitOperator
Add a task using SparkSubmitOperator to run the PySpark script `wordcount.py`.

### 6. Configure Dependencies
Ensure the task in the DAG has the correct dependencies.

### 7. Run and Verify
Run the DAG and verify that the PySpark job executes successfully. Open your localhost:8080 to run the DAG.

To trigger the DAG manually, use the Airflow web interface or the following CLI command:
```sh
airflow dags trigger pyspark_wordcount


