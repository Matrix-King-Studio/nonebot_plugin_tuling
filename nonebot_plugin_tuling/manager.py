# -*- coding: utf-8 -*-
# @Time        : 2022/9/24 12:16
# @File        : manager.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import json
import random
from pathlib import Path
from typing import Any, Dict, Union, List, Optional

import requests
from nonebot import get_bot, logger
from nonebot.adapters.onebot.v11 import ActionFailed
from nonebot.adapters.onebot.v11 import MessageSegment

from .config import plugin_config


def load_json(_file: Path) -> Any:
	with open(_file, 'r', encoding="utf-8") as f:
		return json.load(f)


def save_json(_file: Path, _data: Any) -> None:
	with open(_file, 'w', encoding="utf-8") as f:
		json.dump(_data, f, ensure_ascii=False, indent=4)


class ChatManager:
	def __init__(self):
		self._chat: Dict[str, Union[List[str], Dict[str, bool]]] = {}
		self._chat_json: Path = plugin_config.config_path / "config.json"
		self.apikey: List[str] = plugin_config.apikey

	def update_groups_on(self, gid: str, new_state: bool) -> None:
		"""
			Turn on/off chat in group
		"""
		self._chat = load_json(self._chat_json)

		if new_state:
			if gid not in self._chat["groups_id"]:
				self._chat["groups_id"].update({gid: True})
		else:
			if gid in self._chat["groups_id"]:
				self._chat["groups_id"].update({gid: False})

		save_json(self._chat_json, self._chat)

	async def do_chat(self, gid, user_msg) -> None:
		bot = get_bot()
		self._chat = load_json(self._chat_json)
		msg = self._get_chat_msg(user_msg)

		if isinstance(msg, MessageSegment) and bool(self._chat["groups_id"]) > 0:
			if self._chat["groups_id"].get(gid, False):
				try:
					await bot.call_api("send_group_msg", group_id=int(gid), message=msg)
				except ActionFailed as e:
					logger.warning(f"发送群 {gid} 失败：{e}")

	def _get_chat_msg(self, user_msg) -> Optional[MessageSegment]:
		""" Get a reply, return None if empty """
		try:
			api_url = "http://openapi.tuling123.com/openapi/api/v2"
			req = {
				"reqType": 0,
				"perception": {
					"inputText": {
						"text": user_msg
					},
					"selfInfo": {
						"location": {
							"city": "天津",
							"province": "天津",
							"street": "天津科技大学"
						}
					}
				},
				"userInfo": {
					"apiKey": random.choice(self.apikey),
					"userId": "Alex"
				}
			}
			response = requests.request(
				"post",
				api_url,
				json=req,
				headers={"Content-Type": "application/json;charset=UTF-8"}
			)
			response_dict = json.loads(response.text)

			res = response_dict["results"][0]["values"]["text"]
			logger.info("Tu Ling Robot said: " + res)
			return MessageSegment.text(res)
		except Exception as e:
			logger.warning(f"请求图灵机器人失败：{e}")
			return None


chat_manager = ChatManager()