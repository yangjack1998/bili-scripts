from datetime import datetime, timedelta
from googleapiclient.discovery import build

def getLinks(keyword, topN, days):
    # 替换为你的API密钥
    API_KEY = ''

    # 替换为你的OAuth 2.0授权凭据文件路径
    # creds = Credentials.from_authorized_user_file('./client_secret_296833700058-s7gl10r479ifgek5khjs3f5fqm9h69u7.apps.googleusercontent.com.json')

    # 构建YouTube Data API客户端
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    days_ago = (datetime.now() - timedelta(days)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # 构建获取搜索结果的请求
    request = youtube.search().list(
        q=keyword,  # 搜索关键词
        type='video',  # 返回视频结果
        part='id',  # 只返回视频ID
        maxResults=topN,  # 返回最新的topN个视频
        publishedAfter=days_ago  # 指定只返回两周内发布的视频
    )

    # 发送请求并解析响应
    response = request.execute()
    # Parse the search results and print the video titles and URLs
    video_urls = []
    for search_result in response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_url = f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
            print(f"{video_url}")
            video_urls.append(video_url)

    return video_urls
