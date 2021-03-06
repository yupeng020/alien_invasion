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
        """Initialize the game's static settings."""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 180, 230)

        # Ship settings
        self.ship_speed_factor = 16
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 12
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # Limiting the number of buttlets
        self.bullets_allowed = 8

        # Alien settings
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the alien point values increse
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)