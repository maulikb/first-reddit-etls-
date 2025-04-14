# Reddit Data Pipeline

This project implements a data pipeline to process Reddit data. The pipeline reads Reddit data from a CSV file, processes it, and uploads the data directly to an AWS S3 bucket. The pipeline is orchestrated using Apache Airflow running in a Dockerized environment.

---

## Project Setup

Follow the steps below to set up and run the project.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd RedditDataPipeline
```

---

### 2. Configure Environment Variables

1. Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```

2. Add the following environment variables to the `.env` file:
   ```properties
   AWS_ACCESS_KEY=your-access-key
   AWS_SECRET_KEY=your-secret-key
   AWS_REGION=ap-south-1
   AWS_BUCKET_NAME=reddit-project-data-01

   # Reddit API Keys
   REDDIT_SECRET_KEY=your-reddit-secret-key
   REDDIT_CLIENT_ID=your-reddit-client-id
   ```

---

### 3. Install Dependencies

Dependencies are managed using `requirements.txt`. These will be installed automatically in the Docker container. If you want to install them locally for testing, run:
```bash
pip install -r requirements.txt
```

---

### 4. Prepare Input Data

1. Place the Reddit CSV file in the `data/input/reddit/` directory. For example:
   ```
   data/input/reddit/reddit_20231022.csv
   ```

2. Ensure the file is structured as follows:
   ```csv
   id,title,score,num_comments,author,created_utc,url,over_18,edited,spoiler,stickied
   17d3xk3,What is data engineering *not*?,58,76,No_Newspaper3209,2023-10-21 14:34:12,https://www.reddit.com/r/dataengineering/comments/17d3xk3/what_is_data_engineering_not/,False,False,False,False
   ```

---

### 5. Start Dockerized Airflow Environment

1. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

2. Access the Airflow webserver in your browser:
   ```
   http://localhost:8080
   ```

3. Login with the default credentials:
   - Username: `admin`
   - Password: `admin`

---

### 6. Run the Pipeline

1. Navigate to the Airflow UI.
2. Enable the `reddit_dag`.
3. Trigger the DAG manually or wait for the scheduled interval.

---

## Project Structure

```
RedditDataPipeline/
├── dags/                     # Airflow DAGs
│   └── reddit_dag.py         # Main DAG for the Reddit data pipeline
├── data/                     # Input and output data
│   └── input/reddit/         # Input Reddit data (CSV files)
├── utils/                    # Utility scripts
│   ├── s3_utils.py           # S3 upload utility
│   └── constants.py          # Loads configuration from environment variables
├── pipelines/                # Additional pipeline logic (if any)
├── logs/                     # Airflow logs
├── plugins/                  # Airflow plugins
├── tests/                    # Test scripts
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # Docker Compose configuration
├── .env                      # Environment variables for sensitive configurations
├── Dockerfile                # Dockerfile for Airflow
└── README.md                 # Project documentation
```

---

## Key Components

### 1. **DAG: `reddit_dag.py`**
   - Reads Reddit data from a CSV file located at `/opt/airflow/data/input/reddit/reddit_20231022.csv`.
   - Uploads the CSV file directly to an S3 bucket.

### 2. **S3 Utility: `s3_utils.py`**
   - Handles uploading files to S3.
   - Ensures the S3 bucket exists or creates it if necessary.

### 3. **Environment Variables**
   - Sensitive configurations like AWS credentials and Reddit API keys are stored in the `.env` file.
   - The `constants.py` file loads these configurations using the `dotenv` library.

### 4. **Dockerized Environment**
   - The project uses Docker Compose to set up an Airflow environment with the following services:
     - **Postgres**: Metadata database for Airflow.
     - **Redis**: Message broker for Airflow.
     - **Airflow Webserver, Scheduler, Worker**: Core Airflow components.

---

## Testing

1. **Unit Tests**:
   Add test cases in the `tests/` directory to validate the pipeline logic.

2. **Manual Testing**:
   - Place a sample CSV file in `data/input/reddit/`.
   - Trigger the DAG in the Airflow UI and verify the file is uploaded to S3.

---

## Troubleshooting

1. **Airflow DAG Not Showing**:
   - Ensure the `dags/` directory is correctly mounted in the Docker container.
   - Restart the Airflow webserver:
     ```bash
     docker-compose restart airflow-webserver
     ```

2. **S3 Upload Issues**:
   - Verify AWS credentials in the `.env` file.
   - Check the S3 bucket name and region.

3. **Docker Build Errors**:
   - Ensure Docker is running and the `docker-compose.yml` file is correctly configured.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
