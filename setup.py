# -*- coding: utf-8 -*-
# @Time        : 2022/9/24 14:32
# @File        : setup.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_tuling",
    version="0.0.16",
    author="alex",
    author_email="liu_zhao_feng_alex@163.com",
    description="nonebot_plugin_tuling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matrix-King-Studio/nonebot_plugin_tuling",
    project_urls={
        "Bug Tracker": "https://github.com/Matrix-King-Studio/nonebot_plugin_tuling/issues",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires=">=3.9",
    platforms="any",
    install_requires=[
        "nonebot2>=2.0.0-beta.2",
        "nonebot-adapter-onebot",
        "httpx>=0.23.0"]
)
