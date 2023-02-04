"""
bilibili_api.rank

和哔哩哔哩视频排行榜相关的 API
所有数据都会显示在热门页面
（点击主页“热门”按钮进入）
https://www.bilibili.com/v/popular/all
"""

from .utils.network_httpx import request
from .utils.utils import get_api
from enum import Enum

API = get_api("rank")


class RankAPIType(Enum):
    """
    排行榜 API 接口类型

    - PGC: https://api.bilibili.com/pgc/web/rank/list
    - V2: https://api.bilibili.com/x/web-interface/ranking/v2
    """
    PGC = "pgc"
    V2 = "x"


class RankDayType(Enum):
    """
    RankAPIType.PGC 排行榜时间类型

    - THREE_DAY: 三日排行
    - WEEK: 周排行
    """
    THREE_DAY = 3
    WEEK = 7

class RankType(Enum):
    """
    排行榜类型

    - All: 全部
    - Bangumi: 番剧
    - GuochuangAnime: 国产动画
    - Guochuang: 国创相关
    - Documentary: 纪录片
    - Douga: 动画
    - Music: 音乐
    - Dance: 舞蹈
    - Game: 游戏
    - Knowledge: 知识
    - Technology: 科技
    - Sports: 运动
    - Car: 汽车
    - Life: 生活
    - Food: 美食
    - Animal: 动物圈
    - Kitchen: 鬼畜
    - Fashion: 时尚
    - Ent: 娱乐
    - Cinephile: 影视
    - Movie: 电影
    - TV: 电视剧
    - Variety: 综艺
    - Original: 原创
    - Rookie: 新人
    """
    All = {"api_type": "x", "rid": 0, "type": "all"}
    Bangumi = {"api_type": "pgc", "season_type": 1}
    GuochuangAnime = {"api_type": "pgc", "season_type": 4}
    Guochuang = {"api_type": "x", "rid": 168, "type": "all"}
    Documentary = {"api_type": "pgc", "season_type": 3}
    Douga = {"api_type": "x", "rid": 1, "type": "all"}
    Music = {"api_type": "x", "rid": 3, "type": "all"}
    Dance = {"api_type": "x", "rid": 129, "type": "all"}
    Game = {"api_type": "x", "rid": 4, "type": "all"}
    Knowledge = {"api_type": "x", "rid": 36, "type": "all"}
    Technology = {"api_type": "x", "rid": 188, "type": "all"}
    Sports = {"api_type": "x", "rid": 234, "type": "all"}
    Car = {"api_type": "x", "rid": 223, "type": "all"}
    Life = {"api_type": "x", "rid": 160, "type": "all"}
    Food = {"api_type": "x", "rid": 211, "type": "all"}
    Animal = {"api_type": "x", "rid": 217, "type": "all"}
    Kichiku = {"api_type": "x", "rid": 119, "type": "all"}
    Fashion = {"api_type": "x", "rid": 155, "type": "all"}
    Ent = {"api_type": "x", "rid": 5, "type": "all"}
    Cinephile = {"api_type": "x", "rid": 181, "type": "all"}
    Movie = {"api_type": "pgc", "season_type": 2}
    TV = {"api_type": "pgc", "season_type": 5}
    Variety = {"api_type": "pgc", "season_type": 7}
    Original = {"api_type": "x", "rid": 0, "type": "origin"}
    Rookie = {"api_type": "x", "rid": 0, "type": "rookie"}


class VIPRankType(Enum):
    """
    大会员中心热播榜单类型，即 rank_id

    - VIP: 会员
    - BANGUMI: 番剧
    - GUOCHUANG: 国创
    - MOVIE: 电影
    - DOCUMENTARY: 纪录片
    - TV: 电视剧
    - VARIETY: 综艺
    """
    VIP = 279
    BANGUMI = 118
    GUOCHUANG = 119
    MOVIE = 174
    DOCUMENTARY = 175
    TV = 176
    VARIETY = 177

class MangeRankType(Enum):
    """
    漫画排行榜类型

    - NEW: 新作
    - BOY: 男生
    - GRIL: 女生
    - GUOCHUANG: 国漫
    - JAPAN: 日漫
    - SOUTHKOREA: 韩漫
    - OFFICAL: 宝藏
    - FREE: 免费
    - FINISH: 完结
    """
    NEW = 7
    BOY = 11
    GRIL = 12
    GUOCHUANG = 1
    JAPAN = 0
    SOUTHKOREA = 2
    OFFICAL = 5
    FREE = 8
    FINISH = 13

async def get_hot_videos(pn: int = 1, ps: int = 20) -> dict:
    """
    获取热门视频

    Args:
        pn (int): 第几页. Default to 1.
        ps (int): 每页视频数. Default to 20.

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["hot"]
    params = {"ps": ps, "pn": pn}
    return await request("GET", url=api["url"], params=params)


async def get_weakly_hot_videos_list() -> dict:
    """
    获取每周必看列表(仅概述)

    Returns:
        调用 API 返回的结果
    """
    api = API["info"]["weakly_series"]
    return await request("GET", url=api["url"])


async def get_weakly_hot_videos(week: int = 1) -> dict:
    """
    获取一周的每周必看视频列表

    Args:
        week(int): 第几周. Default to 1.

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["weakly_details"]
    params = {"number": week}
    return await request("GET", url=api["url"], params=params)


async def get_history_popular_videos() -> dict:
    """
    获取入站必刷 85 个视频

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["history_popular"]
    params = {"page_size": 85, "page": 1}
    return await request("GET", url=api["url"], params=params)


async def get_rank(type_: RankType = RankType.All, day: RankDayType = RankDayType.THREE_DAY) -> dict:
    """
    获取视频排行榜

    Args:
        type_ (RankType): 排行榜类型. Defaults to RankType.All
        day (RankDayType): 排行榜时间. Defaults to RankDayType.THREE_DAY
                           仅对 api_type 为 RankAPIType.PGC 有效

    Returns:
        dict: 调用 API 返回的结果
    """
    params = {}
    
    # 确定 API 接口类型
    if type_.value["api_type"] == RankAPIType.V2.value:
        api = API["info"]["v2_ranking"]
        params["rid"] = type_.value["rid"]
    elif type_.value["api_type"] == RankAPIType.PGC.value:
        api = API["info"]["pgc_ranking"]
        params["season_type"] = type_.value["season_type"]
        params["day"] = day.value
    else:
        raise Exception("Unknown RankType")

    return await request("GET", api["url"], params=params)


async def get_music_rank_list() -> dict:
    """
    获取全站音乐榜每周信息(不包括具体的音频列表)

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["music_weakly_series"]
    params = {"list_type": 1}
    return await request("GET", api["url"], params=params)


async def get_music_rank_weakly_detail(week: int = 1) -> dict:
    """
    获取全站音乐榜一周的详细信息(不包括具体的音频列表)

    Args:
        week(int): 第几周. Defaults to 1.

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["music_weakly_details"]
    params = {"list_id": week}
    return await request("GET", api["url"], params=params)


async def get_music_rank_weakly_musics(week: int = 1) -> dict:
    """
    获取全站音乐榜一周的音频列表

    Args:
        week(int): 第几周. Defaults to 1.

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["music_weakly_content"]
    params = {"list_id": week}
    return await request("GET", api["url"], params=params)

async def get_vip_rank(type_: VIPRankType = VIPRankType.VIP) -> dict:
    """
    获取大会员中心的排行榜

    Args:
        type_ (VIPRankType): 排行榜类型. Defaults to VIPRankType.VIP

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["VIP_rank"]
    params = {"rank_id": type_.value}
    return await request("GET", api["url"], params=params)

async def get_manga_rank(type_ : MangeRankType = MangeRankType.NEW) -> dict:
    """
    获取漫画专属排行榜

    Returns:
        dict: 调用 API 返回的结果
    """
    api = API["info"]["manga_rank"]
    params = {"device": "pc","platform": "web"}
    data = {"id": type_.value}
    return await request("POST", api["url"], params=params, data=data, no_csrf=True)
