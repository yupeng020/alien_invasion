# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************************************
# Author       :张 玉 鹏
# Last modified:2020-07-16 14:30
# Email        :yupeng020@163.com
# WebSite      :https://www.kyvision.cn
# Filename     :ship.py
# Description  :
# ******************************************************
"""
本文件储存飞船ship的一些特性
"""

import pygame


class Ship():


    def __init__(self, screen):
        """初始化飞船并设定初始位置"""
        self.screen = screen

        # 中英文输入法切换太他妈麻烦，以下注释用英文
        # Load the ship image and get its rect.
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the botton center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

