from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "untitled-0519131308",
}

dag = DAG(
    "untitled-0519131308",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using untitled.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_c068763a_ce4e_4df9_a1de_8dfa4cdc8a0f = NotebookOp(
    name="data_extraction",
    namespace="marco",
    task_id="data_extraction",
    notebook="notebooks/ML_EXAMPLE_PIPELINE/data_extraction.py",
    cos_endpoint="http://127.0.0.1:9999",
    cos_bucket="testbkmio",
    cos_directory="untitled-0519131308",
    cos_dependencies_archive="data_extraction-c068763a-ce4e-4df9-a1de-8dfa4cdc8a0f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="continuumio/anaconda3:2020.07",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)
