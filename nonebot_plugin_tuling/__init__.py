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

from .manager import chat_manager

chat_on = on_command("开启闲聊", aliases={"开启聊天"}, priority=10, block=True)
chat_off = on_command("关闭闲聊", aliases={"关闭聊天"}, priority=10, block=True)

reply = on_message(priority=100)


@chat_on.handle()
async def _(event: GroupMessageEvent):
	chat_manager.update_groups_on(str(event.group_id), True)
	await chat_on.finish("已开启闲聊~")


@chat_off.handle()
async def _(event: GroupMessageEvent):
	chat_manager.update_groups_on(str(event.group_id), False)
	await chat_off.finish("已关闭闲聊~")


@reply.handle()
async def chat(event: GroupMessageEvent):
	user_msg = str(event.get_message()).strip()
	await chat_manager.do_chat(str(event.group_id), user_msg)
