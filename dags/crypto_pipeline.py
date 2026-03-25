from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Jan",
    "retries": 1
}

with DAG (
    dag_id="crypto_pipeline_v1",
    default_args = default_args,
    schedule = "@hourly",
    start_date = datetime(2026, 1, 1),
    catchup = False
) as dag:
    task_1_extract = BashOperator(
        task_id='extract_data_from_api',
        bash_command='python /opt/airflow/dags/extractor.py'
    )

    task_2_dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /opt/airflow/dags/crypto_dbt && dbt run --profiles-dir .'
    )

    task_1_extract >> task_2_dbt_run