#!/usr/bin/env python

import math
import time
import datetime
import random
import sys
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(1)
width,height=unicorn.get_shape()

colors = unicorn.get_pixels()
counter = 0;
nrofsources = 3;
sources = [];
start_time = time.time() 
scenelength = 50;

# if a valid duration was supplied on the command line, use it
seconds = 30
if sys.argv[1].isnumeric() :
	seconds = float( sys.argv[1] )
end_time = start_time + seconds

# Create a class to contain one source color object
class Source:
	xpos = 0
	ypos = 0
	radius = 0;
	speed = 0;
	offset = 0;
	r = 0;
	g = 0;
	b = 0;

# function to initialize a new Source with random values
def init_source( s ):
	s.radius = random.randint( 10, 100 )
	s.speed = random.uniform( 0.1, 0.75 )
	if random.random() < 0.5 :
		s.speed = -s.speed
	s.offset = random.uniform( 0, 2*math.pi )
	s.r = random.randint( 0, 255 )
	s.g = random.randint( 0, 255 )
	s.b = random.randint( 0, 255 )
	return s

# update the source (which move around the center for the grid)
def update_sources():
	for i in range( len( sources ) ):
		x = math.sin( ( counter * sources[i].speed ) + sources[i].offset ) * sources[i].radius
		sources[i].xpos = x
		y = -math.cos( ( counter * sources[i].speed ) + sources[i].offset ) * sources[i].radius
		sources[i].ypos = y

# calculate the color for each LED in the array based on the source positions 
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
			unicorn.set_pixel( x, y, r, g, b )

# helper function to calculate distances
def pythagoras( a, b ):
	value = math.sqrt( a*a + b*b )
	return value

# start a new scene by resetting the sources and other values
def start_scene():
	global sources, scenelength, nrofsources
	sources = [];
	scenelength = 10 + random.randint( 0, 50 )
	for i in range( nrofsources ):
		sources.append( init_source( Source() ) )
	unicorn.brightness( 0.25 + random.random() * 0.75 )

# kick off the first scene
start_scene();

# main update loop
try:
	while time.time() < end_time:
		update_sources()
		update_colors()
		unicorn.show();
		counter += 1
		# check if the scene is over
		if ( counter >= scenelength ):
			counter = 0
			start_scene()
		time.sleep( 0.05 )

except KeyboardInterrupt:
	unicorn.off()
