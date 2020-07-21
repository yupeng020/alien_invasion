# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************************************
# Author       :张 玉 鹏
# Last modified:2020-07-16 14:38
# Email        :yupeng020@163.com
# WebSite      :https://www.kyvision.cn
# Filename     :settings.py
# Description  :
# ******************************************************
"""
本文件储存一些设置参数
"""

import pygame

class Settings:


    def __init__(self):
        """初始化程序"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 180, 230)


        # Ship settings
        self.ship_speed_factor = 6

    
