#!/bin/bash

# 目标路径定义
TARGETpy="robocasa/robocasa/tidybot.py"
TARGETdir="robosuite/robosuite/models/assets/stanford_tidybot"

# 执行标志
need_copy_py=false
need_copy_dir=false

# 检查Python文件
if [ -e "$TARGETpy" ]; then
    echo "目标已存在: $TARGETpy"
else
    echo "目标不存在: $TARGETpy (将执行复制)"
    need_copy_py=true
fi

# 检查目录
if [ -e "$TARGETdir" ]; then
    echo "目标已存在: $TARGETdir"
else
    echo "目标不存在: $TARGETdir (将执行复制)"
    need_copy_dir=true
fi

# 如果两个目标都存在则直接退出
if ! $need_copy_py && ! $need_copy_dir; then
    echo "所有目标均已存在，跳过复制操作"
    exit 0
fi

# 执行需要的复制操作
if $need_copy_py; then
    echo "正在复制tidybot.py..."
    mkdir -p "$(dirname "$TARGETpy")"  # 确保目录存在
    cp tidybot.py "$TARGETpy" || exit 1
fi

if $need_copy_dir; then
    echo "正在复制stanford_tidybot目录..."
    mkdir -p "$(dirname "$TARGETdir")"  # 确保目录存在
    cp -r stanford_tidybot "$TARGETdir" || exit 1
fi

echo "操作完成"