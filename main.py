import os
import pickle
import json
from download import download
from getLinks import getLinks

def isRepeat(URL):
    file = 'urls.data'
    with open(file, 'rb') as f:
        urls = pickle.load(f)
    url_set = set(urls)
    return URL in url_set

def execute(URL):
    if isRepeat(URL):
        print("Video already downloaded. Skipping...")
        return

    title, description = download(URL)
    print(title)
    path = title
    current_dir = os.getcwd()
    for file in os.listdir(os.getcwd()):
        if title in file:
            path = os.path.join(current_dir, file)
            break
    if len(description) > 500:
        description = description[:500]
    
    # Saving URL to file if not already downloaded
    file = 'urls.data'
    with open(file, 'rb') as f:
        urls = pickle.load(f)
    urls.append(URL)
    with open(file, 'wb') as f:
        pickle.dump(urls, f)

    # Saving video information to a JSON file
    video_info = {
        "title": title,
        "description": description,
        "URL": URL,
        "path": path
    }
    if os.path.exists('video_info.json'):
        with open('video_info.json') as f:
            video_info_list = json.load(f)
    video_info_list.append(video_info)
    with open('video_info.json', 'w') as json_file:
        json.dump(video_info_list, json_file, indent=4)

if __name__ == '__main__':
    URLs = getLinks(keyword="vex high stakes", topN = 5,days = 7)
    print(URLs)
    
    for URL in URLs:
        execute(URL)
