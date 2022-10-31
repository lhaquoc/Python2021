#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 07:38:59 2022

@author: anhquoc
"""

import sys

import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
        print("moving right")
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        print("moving left")
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = False
    print("ship: (" + str(ship.rect.x) + ", " + str(ship.rect.y) + ")")
def check_events(ship):
    # Watch keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
            
def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()            