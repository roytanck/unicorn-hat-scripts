#!/usr/bin/env python

import time
import random
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.75)
width,height=unicorn.get_shape()

colors = unicorn.get_pixels()
#print( colors )

def init_colors():
	for x in range( width ):
		for y in range( height ):	
			rgblist = list( colors[x][y] );
			for i in range( len( rgblist ) ):
				rgblist[i] = random.randint( 0, 255 )
			colors[x][y] = tuple( rgblist )


def update_colors():
	for x in range( width ):
		for y in range( height ):
			rgblist = list( colors[x][y] );
			for i in range( len( rgblist ) ):
				addition = random.randint( 0, 50 ) - 25;
				rgblist[i] = max( 0, min( 255, rgblist[i] + addition ) )
			colors[x][y] = tuple( rgblist )


init_colors()

for i in range( 0, 50 ):
	update_colors()
	unicorn.set_pixels( colors )
	unicorn.show()
	time.sleep( 0.05 );


time.sleep( 1 )
