#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 25/10/18 at 17:50
"""
import cv2

def close_windows():
    while True:
        if 0xFF & cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()
