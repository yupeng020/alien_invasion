# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************************************
# Author       :张 玉 鹏
# Last modified:2020-07-21 11:53
# Email        :yupeng020@163.com
# WebSite      :https://www.kyvision.cn
# Filename     :game_functions.py
# Description  :
# ******************************************************

import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

