#!/usr/bin/env python

import math
import time
import random
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(1)
width,height=unicorn.get_shape()

counter = 0;
nrofsources = 3;
sources = [];

class Source:
	xpos = 0
	ypos = 0
	radius = 0;
	speed = 0;
	offset = 0;
	r = 0;
	g = 0;
	b = 0;

def init_source( s ):
	s.radius = random.randint( 10, 100 )
	s.speed = random.uniform( 0.1, 0.75 )
	if random.random() < 0.5 :
		s.speed = -s.speed
	s.offset = random.uniform( 0, 2*math.pi )
	s.r = random.randint( 100, 255 )
	s.g = random.randint( 50, int( s.r * 0.8 ) )
	s.b = 0
	return s

# create sources
for i in range( nrofsources ):
	sources.append( init_source( Source() ) )


def update_sources():
	for i in range( len( sources ) ):
		x = math.sin( ( counter * sources[i].speed ) + sources[i].offset ) * sources[i].radius
		sources[i].xpos = x
		y = -math.cos( ( counter * sources[i].speed ) + sources[i].offset ) * sources[i].radius
		sources[i].ypos = y


def update_colors():
	for x in range( width ):
		for y in range( height ):
			ledposx = ( x * 10 ) - 35
			ledposy = ( y * 10 ) - 35
			r = 0
			g = 0
			b = 0
			for s in sources:
				xdist = ledposx - s.xpos
				ydist = ledposy - s.ypos
				dist = pythagoras( xdist, ydist )
				influence = max( 0, ( 1 - ( dist / 100 ) ) )
				r += ( influence * s.r )
				g += ( influence * s.g )
				b += ( influence * s.b )
			r = int( max( 0, min( 255, r ) ) )
			g = int( max( 0, min( 255, g ) ) )
			b = int( max( 0, min( 255, b ) ) )
			#print( r )
			unicorn.set_pixel( x, y, r, g, b )


def pythagoras( a, b ):
	value = math.sqrt( a*a + b*b )
	return value


for i in range( 0, 200 ):
	update_sources()
	update_colors()
	unicorn.show();
	counter += 1
	time.sleep( 0.05 )

