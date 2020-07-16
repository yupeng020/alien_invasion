# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************************************
# Author       :张 玉 鹏
# Last modified:2020-07-16 14:28
# Email        :yupeng020@163.com
# WebSite      :https://www.kyvision.cn
# Filename     :alien_invasion.py
# Description  :
# ******************************************************


import sys

import pygame

from settings import Settings

from ship import Ship


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(screen)
    
   
    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass though the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most resently drawn screen visible.
        pygame.display.flip()

run_game()

