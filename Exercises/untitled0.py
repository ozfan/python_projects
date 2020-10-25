#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:38:00 2020

@author: ivan
"""

class PlayingCards(object):
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def display(self):
        print(self.value, self.suit)
    