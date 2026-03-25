FROM apache/airflow:2.8.1
RUN pip install --no-cache-dir requests pandas psycopg2-binary dbt-postgres python-dotenv