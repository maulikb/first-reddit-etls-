import configparser
import os 

parser = configparser.ConfigParser()
parser.read(os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/config.conf')))


<<<<<<< HEAD
CLIENT_SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')


DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_PORT = parser.get('database', 'database_port') 
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')



#AWS
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)
=======
# Reddit API Configuration
REDDIT_SECRET_KEY = os.getenv("REDDIT_SECRET_KEY")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")

# File Path Template for S3
RAW_DATA_PATH = "bucket/raw/{file_name}"  # File path template for raw data
>>>>>>> 77f228e... Removed secrets from config and updated to use .env
