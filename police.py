#!/usr/bin/env python

import math
import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(1)
width,height=unicorn.get_shape()

counter = 0;

def update_colors():
	for x in range( width ):
		for y in range( height ):
			brightness = ( math.sin( ( x + counter ) / 2 ) * 100 ) + 156;
			unicorn.set_pixel( x, y, 0, 0, int( brightness ) );

# main update loop
for i in range( 0, 100 ):
	update_colors()
	unicorn.show();
	counter += 1
	time.sleep( 0.05 )
