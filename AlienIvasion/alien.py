#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 07:58:53 2022

@author: anhquoc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:16:33 2022

@author: anhquoc
"""
import pygame

class Alien():
    
    def __init__(self, screen):
        self.screen = screen
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/alien.bmp').convert()
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)    