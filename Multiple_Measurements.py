#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
@version: ??
@author: Jay
@license: BSD Licence 
@file: Multiple_Measurements.py
@time: 2016/6/30 23:51
"""
p = []
n = 5
for i in range(5):
	p.append(1./n)

world = ['green','red','red','green','green']
measurements = ['red','green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
	q = []
	for i in range(len(p)):
		hit = (Z == world[i])
		q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
	s = sum(q)
	for i in range(len(q)):
		q[i] = q[i] / s
	return q

for k in range(len(measurements)):
	p = sense(p, measurements[k])

print p