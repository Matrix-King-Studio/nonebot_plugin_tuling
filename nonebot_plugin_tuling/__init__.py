# -*- coding: utf-8 -*-
# @Time        : 2022/9/24 11:30
# @File        : __init__.py.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from nonebot import on_message, on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent

from .config import Config
from .manager import chat_manager

chat_on = on_command("开启闲聊", aliases={"开启聊天"}, priority=12, block=True)
chat_off = on_command("关闭闲聊", aliases={"关闭聊天"}, priority=12, block=True)

reply = on_message(priority=100)


@chat_on.handle()
async def _(event: GroupMessageEvent):
	gid = str(event.group_id)
	chat_manager.update_groups_on(gid, True)
	await chat_on.finish("已开启闲聊~")


@chat_off.handle()
async def _(event: GroupMessageEvent):
	gid = str(event.group_id)
	chat_manager.update_groups_on(gid, False)
	await chat_off.finish("已关闭闲聊~")


@reply.handle()
async def chat(event: GroupMessageEvent):
	gid = str(event.group_id)
	user_msg = str(event.get_message()).strip()
	if "下次再聊" in user_msg or "再见" in user_msg or "拜拜" in user_msg:
		chat_manager.update_groups_on(gid, False)
		await chat_off.finish("已关闭闲聊~")
	await chat_manager.do_chat(gid, user_msg)