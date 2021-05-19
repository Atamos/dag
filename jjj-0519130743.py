from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "jjj-0519130743",
}

dag = DAG(
    "jjj-0519130743",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using jjj.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_0d52a44c_0e15_4750_8efa_a86919e8d759 = NotebookOp(
    name="data_extraction",
    namespace="testml",
    task_id="data_extraction",
    notebook="notebooks/ML_EXAMPLE_PIPELINE/data_extraction.py",
    cos_endpoint="http://127.0.0.1:9999",
    cos_bucket="testbkmio",
    cos_directory="jjj-0519130743",
    cos_dependencies_archive="data_extraction-0d52a44c-0e15-4750-8efa-a86919e8d759.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    resources={
        "request_cpu": "1",
    },
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)
