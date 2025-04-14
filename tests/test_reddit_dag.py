from airflow.models import DagBag

def test_reddit_dag_loaded():
    """Test that the reddit_dag is loaded correctly."""
    dag_bag = DagBag()
    assert "reddit_dag" in dag_bag.dags
    dag = dag_bag.get_dag("reddit_dag")
    assert len(dag.tasks) == 2

def test_reddit_dag_dependencies():
    """Test task dependencies in the reddit_dag."""
    dag_bag = DagBag()
    dag = dag_bag.get_dag("reddit_dag")

    read_task = dag.get_task("read_reddit_data")
    upload_task = dag.get_task("upload_to_s3")

    assert read_task.downstream_list == [upload_task]
    assert upload_task.upstream_list == [read_task]
