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
import asyncio
import json
import os
import random
from pathlib import Path
from typing import Any, Dict, Union, List, Optional

import httpx
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
		self._chat_json = plugin_config.config_path / "config.json"
		if not os.path.exists(self._chat_json):
			save_json(self._chat_json, {"groups_id": {}})
		self.apikey: List[str] = plugin_config.tu_ling_apikey

	def update_groups_on(self, gid: str, new_state: bool) -> None:
		logger.info(f"群 {gid} 闲聊设置状态为：{new_state}")
		self._chat = load_json(self._chat_json)
		self._chat["groups_id"][gid] = new_state
		save_json(self._chat_json, self._chat)

	async def do_chat(self, gid, user_msg) -> None:
		bot = get_bot()
		self._chat = load_json(self._chat_json)

		if self._chat["groups_id"].get(gid, False):
			if "下次再聊" in user_msg or "再见" in user_msg or "拜拜" in user_msg:
				self.update_groups_on(gid, False)

			msg = await self._get_chat_msg(user_msg)
			if isinstance(msg, MessageSegment) and bool(self._chat["groups_id"]) > 0:
				try:
					await bot.call_api("send_group_msg", group_id=int(gid), message=msg)
				except ActionFailed as e:
					logger.warning(f"发送群 {gid} 失败：{e}")

	async def _get_chat_msg(self, user_msg) -> Optional[MessageSegment]:
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
			headers = {"Content-Type": "application/json;charset=UTF-8"}
			async with httpx.AsyncClient(verify=False, timeout=None) as client:
				response = await client.post(api_url, json=req, headers=headers)
				response_dict = json.loads(response.text)
				res = response_dict["results"][0]["values"]["text"]
				logger.info("Tu Ling Robot said: " + res)
				await asyncio.sleep(len(res) / len(user_msg + res))
				return MessageSegment.text(res)
		except Exception as e:
			logger.warning(f"请求图灵机器人失败：{e}")


chat_manager = ChatManager()
