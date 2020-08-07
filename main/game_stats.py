# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************************************
# Author       :张 玉 鹏
# Last modified:2020-07-27 11:50
# Email        :yupeng020@163.com
# WebSite      :https://www.kyvision.cn
# Filename     :game_stats.py
# Description  :
# ******************************************************


class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1