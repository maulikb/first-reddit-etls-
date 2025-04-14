import os
from utils.constants import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_BUCKET_NAME, REDDIT_SECRET_KEY, REDDIT_CLIENT_ID

def test_constants_loaded():
    """Test that constants are loaded correctly from the environment."""
    os.environ["AWS_ACCESS_KEY"] = "test-access-key"
    os.environ["AWS_SECRET_KEY"] = "test-secret-key"
    os.environ["AWS_REGION"] = "test-region"
    os.environ["AWS_BUCKET_NAME"] = "test-bucket"
    os.environ["REDDIT_SECRET_KEY"] = "test-reddit-secret"
    os.environ["REDDIT_CLIENT_ID"] = "test-reddit-client"

    assert AWS_ACCESS_KEY == "test-access-key"
    assert AWS_SECRET_KEY == "test-secret-key"
    assert AWS_REGION == "test-region"
    assert AWS_BUCKET_NAME == "test-bucket"
    assert REDDIT_SECRET_KEY == "test-reddit-secret"
    assert REDDIT_CLIENT_ID == "test-reddit-client"
