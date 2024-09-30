import json
import yt_dlp

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
def download(url):
    # ydl_opts = {'format': 'mp4'}
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        info_dic = ydl.sanitize_info(info)
        real_info =json.dumps(ydl.sanitize_info(info))
        # ℹ️ ydl.sanitize_info makes the info json-serializable
        title = info_dic['title']
        description = info_dic['description']
        ydl.download(url)
    return title,description

