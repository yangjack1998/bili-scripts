from biliup.plugins.bili_webup import BiliBili, Data

def upload(title, desc, source, path):
    video = Data()
    video.title = title
    video.desc = desc
    video.source = source
    # 设置视频分区,默认为122 野生技能协会
    video.tid = 232
    video.set_tag(['VEX', 'VEX机器人'])
    with BiliBili(video) as bili:
        bili.login("bili.cookie", {
            'cookies':{
                'SESSDATA': 'a9e48c41%2C1743204809%2Cbcff7%2A91CjC0PQKSr7KwrlhNQUr3_DyN_hCu6RgUZlge-dplWIVEXISKSGwlBpuD7mNfPlm-160SVmF2b2VTV1FFUHM5ZkttcUtxcUpPU1ZVRjltM01RanFBZnJhLURSdWQ0VFJNTGFOSzlyY1lKUnhTMnY1VHBHV2VjekhDdVhnUVFoUmozbm1NeUZ4b0lRIIEC',
                'bili_jct': '008d714419fe0d8cbbe01dc28187d38f',
                'DedeUserID__ckMd5': 'ac8e4a18c9540d83',
                'DedeUserID': '8990444'
            },'access_token': '8b5103fd3075ad7df418bdf956c7bed0'})
        # bili.login("bili.cookie", {
        #     'cookies':{
        #         'SESSDATA': 'e2a4cca2%2C1668364392%2C80d71751',
        #         'bili_jct': '6082018bdecdb622d01ea9bebe6fc0dd',
        #         'DedeUserID__ckMd5': '6a8389837fb61ceb',
        #         'DedeUserID': '601608698'
        #     },'access_token': '675cccf497425a770cba55579fefdc51'})
        # bili.login_by_password("username", "password")
        #for file in file_list:
        file = path
        video_part = bili.upload_file(file)  # 上传视频
        video.append(video_part)  # 添加已经上传的视频
        #video.cover = bili.cover_up('/cover_path').replace('http:', '')
        #video.cover = './cover.webp'
        ret = bili.submit()  # 提交视频
