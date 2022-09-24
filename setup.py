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
    version="0.0.1",
    author="alex",
    author_email="liu_zhao_feng_alex@163.com",
    description="nonebot_plugin_tuling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matrix-King-Studio/nonebot_plugin_tuling",
    project_urls={
        "Bug Tracker": "https://github.com/Matrix-King-Studio/nonebot_plugin_tuling/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
