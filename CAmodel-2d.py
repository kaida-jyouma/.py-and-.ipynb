# -*- coding: utf-8 -*-
import math as mt
import random as rdm
import sys
import time as tm
lv = chr(9632)
nn = chr(9633)
fi = chr(9635)
def check(list_name, x, y): # list_name => 2次元配列
	# return format => [set_bool, top_bool, right_bool, bottom_bool, left_bool]
	retl = [False, False, False, False, False]
	if list_name[x][y] == lv: # 指定の座標がlvであれば
		retl[0] = True
		if x == 0: # xがリストの最初の列を指定した時
            
		elif x == (len(list_name) - 1): # xがリストの最後の列を指定した時
            
		elif y == 0: # yがリストの最初の行を指定した時
			
		elif y == (len(list_name) - 1): # yがリストの最後の行を指定した時
			
		else: #その他
			
	else:
