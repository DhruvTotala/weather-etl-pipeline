from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from fetch_weather import fetch_weather
from load_to_db import load_to_sqlite

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='weather_etl_pipeline_sqlite',
    default_args=default_args,
    schedule_interval='@daily',
    description='ETL weather data and store in SQLite',
    tags=['weather', 'sqlite']
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_weather',
        python_callable=fetch_weather
    )

    load_task = PythonOperator(
        task_id='load_to_sqlite',
        python_callable=load_to_sqlite
    )

    fetch_task >> load_task
