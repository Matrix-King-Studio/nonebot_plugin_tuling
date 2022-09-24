# -*- coding: utf-8 -*-
# @Time        : 2022/9/24 11:39
# @File        : config.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from pathlib import Path
from typing import List

from nonebot import get_driver
from pydantic import BaseModel, Extra


# apikey = ["fad1ed7e71b14a0a947ce41b14206fd0"]


class Config(BaseModel, extra=Extra.ignore):
	config_path: Path = Path(__file__).parent / "resource"
	apikey: List[str] = list()


plugin_config = Config.parse_obj(get_driver().config)
