import os
import json
import random
import time
from upload import upload
import re

def truncate_title(title, max_length=75):
    if len(title) > max_length:
        return title[:max_length]
    return title

def clean_string(s):
    # 移除所有非字母数字字符
    return re.sub(r'\W+', '', s)


def upload_videos():
    # Load video information from JSON file
    with open('video_info.json') as f:
        video_info_list = json.load(f)

    for video_info in video_info_list:
        title = video_info['title']
        print(title)
        description = video_info['description']
        URL = video_info['URL']
        # Set the maximum length for filenames
        max_length = 75

        # Get the current working directory
        current_directory = os.getcwd()

        # Iterate through all files in the current directory
        for filename in os.listdir(current_directory):
            # Check if the filename length exceeds the maximum length
            if len(filename) > max_length:
                # Shorten the filename to the maximum allowed length
                new_filename = filename[:max_length]

                # Get the full path of the current and new filename
                old_filepath = os.path.join(current_directory, filename)
                new_filepath = os.path.join(current_directory, new_filename)

                # Rename the file
                os.rename(old_filepath, new_filepath)
        for file in os.listdir(current_directory):
            if clean_string(title) in clean_string(file):
                # path = os.path.join(current_dir, file)
                title_short = truncate_title(title)
                print(title_short)
                upload(title_short, description, URL, file)
                os.remove(file)
                break

        # Wait for a random time between 10 to 30 minutes
        wait_time = random.randint(100, 500)  # Random integer between 10 to 30 minutes (in seconds)
        print(f"Waiting for {wait_time // 60} minutes before uploading the next video...")
        time.sleep(wait_time)

    # Clear the JSON file after uploading
    with open('video_info.json', 'w') as f:
        f.write('[]')  # Write an empty list to clear the JSON file

if __name__ == '__main__':
    upload_videos()
