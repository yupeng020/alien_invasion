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

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from button import Button

from ship import Ship

from alien import Alien

import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Make a group of alien.
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # print(len(bullets))       # 打印追踪子弹数量
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, 
                play_button)


run_game()
