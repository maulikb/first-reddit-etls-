from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os 
import sys

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(sys.path)

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline
default_args = {
    'owner': 'Maulik',
    'start_date': datetime(2025, 4, 1)
}

file_postfix = datetime.now().strftime("%Y%m%d%H%M%S")

dag = DAG(
    dag_id='reddit_dag',
    default_args=default_args,
    schedule_interval='@daily',
    tags=['reddit', 'etl', 'pipeline'],
    catchup=False
) 

#extract from reddit

extract = PythonOperator(
    task_id='extract_reddit',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_data_{file_postfix}',
        'subreddit': 'dataengineering',
        'limit': 10,
        'time_filter': 'day'
    },
    dag=dag
)


# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3