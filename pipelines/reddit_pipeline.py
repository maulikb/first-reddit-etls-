from etls.reddit_etl import connect_reddit, extract_posts, transform_data , load_data_to_csv, load_data_to_csv
from utils.constants import CLIENT_ID, CLIENT_SECRET,OUTPUT_PATH
import pandas as pd
import os

def reddit_pipeline(file_name, subreddit, limit, time_filter):
    #connecting to reddit instance 
    #extract the data transformit and load it to csv
    instance  = connect_reddit(CLIENT_ID, CLIENT_SECRET, "my_reddit_bot/1.0 (by u/Tiny_Feedback5097  ")
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    post_df = transform_data (post_df)
    file_path = os.path.join(OUTPUT_PATH, f"{file_name}.csv")
    load_data_to_csv(post_df, file_path)
    print(f"Data loaded to {file_path}")
    return file_path
