from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_scraper():
    subprocess.run(["python", "/opt/airflow/etl/scraper.py"], check=True)

def run_transform():
    subprocess.run(["python", "/opt/airflow/etl/transform.py"], check=True)

def run_load():
    subprocess.run(["python", "/opt/airflow/etl/load.py"], check=True)

with DAG(
    dag_id="etl_piepline",
    start_date=datetime(2025, 9, 9),
    schedule_interval=None,
    catchup=False
) as dag:
    scraper_task = PythonOperator(task_id="scraper", python_callable=run_scraper)
    transform_task = PythonOperator(task_id="transform", python_callable=run_transform)
    load_task = PythonOperator(task_id="load", python_callable=run_load)

    scraper_task >> transform_task >> load_task

