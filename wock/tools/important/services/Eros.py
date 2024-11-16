# generated by datamodel-codegen:
#   filename:  Sidecar.json
#   timestamp: 2024-03-02T00:34:12+00:00
from __future__ import annotations


from typing import List, Optional
import aiohttp
from typing import Any
from pydantic import BaseModel


class MusicInfo(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    play: Optional[str] = None
    author: Optional[str] = None
    original: Optional[bool] = None
    duration: Optional[int] = None
    album: Optional[str] = None


class CommerceInfo(BaseModel):
    adv_promotable: Optional[bool] = None
    auction_ad_invited: Optional[bool] = None
    branded_content_type: Optional[int] = None
    with_comment_filter_words: Optional[bool] = None


class Author(BaseModel):
    id: Optional[str] = None
    unique_id: Optional[str] = None
    nickname: Optional[str] = None
    avatar: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None
    region: Optional[str] = None
    title: Optional[str] = None
    cover: Optional[str] = None
    duration: Optional[int] = None
    play: Optional[str] = None
    wmplay: Optional[str] = None
    hdplay: Optional[str] = None
    size: Optional[Any] = None
    wm_size: Optional[Any] = None
    hd_size: Optional[Any] = None
    music: Optional[str] = None
    music_info: Optional[MusicInfo] = None
    play_count: Optional[int] = None
    digg_count: Optional[int] = None
    comment_count: Optional[int] = None
    share_count: Optional[int] = None
    download_count: Optional[int] = None
    collect_count: Optional[int] = None
    create_time: Optional[int] = None
    anchors: Optional[Any] = None
    an1111111111111111111111111111111111111111111111chors_extras: Optional[str] = None
    is_ad: Optional[bool] = None
    commerce_info: Optional[CommerceInfo] = None
    commercial_video_info: Optional[str] = None
    item_comment_settings: Optional[int] = None
    author: Optional[Author] = None
    images: Optional[List[str]] = None


class PostResponse(BaseModel):
    code: Optional[int] = None
    msg: Optional[str] = None
    processed_time: Optional[float] = None
    data: Optional[Data] = None

    @classmethod
    async def from_response(cls, url: str, key: str) -> Optional[PostResponse]:
        url = url.lstrip("+").lstrip(" ")
        if "@" not in url:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if not str(resp.url) == "https://www.tiktok.com/explore":
                        url = str(resp.url)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://eros.rest/tiktok/post", params = {"url": url}, headers = {"api-key": key}) as response:
                data = await response.read()
        return cls.parse_raw(data)
