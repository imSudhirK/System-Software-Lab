#! /usr/bin/python3

import sys , math
import numpy as np
from PIL import Image

def im_mean(x):
	im = Image.open(x)
	pixels = list(im.getdata())
	Mean = np.mean(pixels, axis =0)
	return Mean

built_mean = im_mean('builtup.png')
lake_mean = im_mean('lake.png')
mumbai_mean = im_mean('mumbai.png')
sea1_mean = im_mean('sea1.png')
sea2_mean = im_mean('sea2.png')
sea3_mean = im_mean('sea3.png')
vegetation1_mean = im_mean('vegetation1.png')
vegetation2_mean = im_mean('vegetation2.png')
vegetation3_mean = im_mean('vegetation3.png')
vegetation4_mean = im_mean('vegetation4.png')
sea_total = sea1_mean + sea2_mean + sea3_mean
sea_mean = sea_total/ 3.0 
veg_total = vegetation1_mean + vegetation2_mean + vegetation3_mean + vegetation4_mean
vegetation_mean = veg_total/4.0

def eu_dist(vec1, P):
	Distance = 0
	d2 =0
	for i in range(0, 3):
		d2= d2+ (vec1[i]-P[i])**2
	Distance = math.sqrt(d2)
	return Distance

def man_dist(vec2, P):
	D = 0
	for i in range(0, 3):
		D = D + abs(vec2[i]- P[i])
	return D

if(len(sys.argv) !=2):
	print("Unknown option")
elif(sys.argv[1] != 'eu' and sys.argv[1] != 'man'):
	print("Unknown option")
elif(sys.argv[1]== 'eu'):
	mumbai_im = Image.open('mumbai.png')
	mumbai_pixels = list(mumbai_im.getdata())
	eu_im = Image.new('L', mumbai_im.size)
	eu_data = []
	for i in range(0,len(mumbai_pixels)):
		b_dist = eu_dist(built_mean, mumbai_pixels[i])
		l_dist = eu_dist(lake_mean, mumbai_pixels[i])
		s_dist = eu_dist(sea_mean, mumbai_pixels[i])
		v_dist = eu_dist(vegetation_mean, mumbai_pixels[i])
		minimum = min(b_dist, l_dist, s_dist, v_dist)
		if(minimum == b_dist):
			eu_data.append(255)
		elif(minimum == l_dist):
			eu_data.append(75)
		elif(minimum == s_dist):
			eu_data.append(0)
		elif(minimum == v_dist):
			eu_data.append(128)
	eu_im.putdata(eu_data)
	eu_im.save("segmented_eu.png")
elif(sys.argv[1]== 'man'):
	mumbai_im = Image.open('mumbai.png')
	mumbai_pixels = list(mumbai_im.getdata())
	man_im = Image.new('L', mumbai_im.size)
	man_data = []
	for i in range(0,len(mumbai_pixels)):
		b_dist = man_dist(built_mean, mumbai_pixels[i])
		l_dist = man_dist(lake_mean, mumbai_pixels[i])
		s_dist = man_dist(sea_mean, mumbai_pixels[i])
		v_dist = man_dist(vegetation_mean, mumbai_pixels[i])
		minimum = min(b_dist, l_dist, s_dist, v_dist)
		if(minimum == b_dist):
			man_data.append(255)
		elif(minimum == l_dist):
			man_data.append(75)
		elif(minimum == s_dist):
			man_data.append(0)
		elif(minimum == v_dist):
			man_data.append(128)
	man_im.putdata(man_data)
	man_im.save("segmented_man.png")
