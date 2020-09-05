from django.shortcuts import render

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

import os
import pathlib
import glob
import pixivpy3
from django.conf import settings
import datetime
import shutil
from time import sleep
import json
import tweepy as tw
from pprint import pprint
from time import sleep


PIXIV_ID = os.environ["PIXIV_ID"]
PIXIV_PASSWORD = os.environ["PIXIV_PASSWORD"]
TWITTER_API_KEY=os.environ["TWITTER_API_KEY"]
TWITTER_API_SERCRET_KEY=os.environ["TWITTER_API_SERCRET_KEY"]
TWITTER_API_ACCESS_TOKEN=os.environ["TWITTER_API_ACCESS_TOKEN"]
TWITTER_API_SERCRET_TOKEN=os.environ["TWITTER_API_SERCRET_TOKEN"]

GET_PICS_NUM = getattr(settings, "GET_PICS_NUM", None)

# TODO:ヘルパ関数staticを使用する
PUBLIC_PATH = '/static/pixiv_img/'
TARGET_PATH = 'static/pixiv_img/'

def index(request):
    return render(request, 'api/index.html')

def getDirectory(request):
    """
    vue_srcに設置したjpgファイルの一覧を取得する
    """
    # Vueのcomponentからの相対パス( /vue_src/public/以下)で、文字列のリストを作成
    l = []
    if os.path.exists(TARGET_PATH):
        l = [PUBLIC_PATH + p  for p in os.listdir(TARGET_PATH)]

    # pprint(l)

    return JsonResponse({'filepaths': l})

def getPixivRanking(request):
    """
    pixivpyから、ランキングの画像を取得する
    """

    # ディレクトリを作成
    if os.path.exists(TARGET_PATH):
        shutil.rmtree(TARGET_PATH)
    os.mkdir(TARGET_PATH)

    PAPI = pixivpy3.PixivAPI()
    PAPI.login(PIXIV_ID, PIXIV_PASSWORD)

    # TODO 見直す
    if request.GET.get("genre") == None:
        return JsonResponse({'status': 'Error'})

    ranking_genre = request.GET.get("genre")

    # TODO クラスメソッド化
    # ランキングを取得
    json_result = PAPI.ranking_all(mode=ranking_genre, page=1, per_page=GET_PICS_NUM, date=None)

    for illust in json_result.response[0].works:

        # ランキング順位を作成する、10未満はゼロ埋め
        rank_no = str(illust.rank) if len(str(illust.rank)) > 1 else "0" + str(illust.rank)

        if illust.work.page_count == 1:
            # ファイル名 = 作品ID_ページ番号.jpg
            file_name = rank_no + '_' +  str(illust.work.id) + '.jpg'
            PAPI.download(illust.work.image_urls.px_480mw, path=TARGET_PATH, name=file_name)

        else:
            page_infos = PAPI.works(illust.work.id)
            for page_no in range(0, page_infos.response[0].page_count):
                # ファイル名 = ランキング順位_作品ID_ページ番号.jpg
                file_name = rank_no + '_' + str(illust.work.id) + '_' + str(page_no + 1) + '.jpg'
                page_info = page_infos.response[0].metadata.pages[page_no]
                PAPI.download(page_info.image_urls.px_480mw, path=TARGET_PATH, name=file_name)

        sleep(2)

    return JsonResponse({'status': 'OK!'})

@csrf_exempt
def tweet(request):
    # TODO クラスメソッド化
    # 取得したキーとアクセストークンを設定する
    auth = tw.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SERCRET_KEY)
    auth.set_access_token(TWITTER_API_ACCESS_TOKEN, TWITTER_API_SERCRET_TOKEN)

    api = tw.API(auth)

    json_dict = json.loads(request.body)
    tweet_content = json_dict['tweet']

    # txt = "テスト投稿です。ｲｪｰｲ"
    api.update_status(tweet_content)

    return JsonResponse({'status': 'OK!'})

@csrf_exempt
def getPixivInfo(request):
    # TODO クラスメソッド化
    PAPI = pixivpy3.PixivAPI()
    PAPI.login(PIXIV_ID, PIXIV_PASSWORD)

    if request.GET.get("illust_id") == None:
        pass

    illust_id = request.GET.get("illust_id")

    # pprint(illust_id)
    illust_infos = PAPI.works(int(illust_id))

    raw_illust_info = illust_infos.response[0]

    title = raw_illust_info.title
    author_name = raw_illust_info.user.name
    url = 'https://www.pixiv.net/artworks/' + str(illust_id)

    _dict = {'title': title, 'author_name': author_name, 'url': url}
    txt = '{title} | {author_name} #pixiv #PixivRankingViewer \r\n{url}'

    illust_info = txt.format(**_dict)

    return JsonResponse({'illust_info': illust_info})