# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:43:43 2020

@author: bosem
"""

import numpy as np
import holoviews as hv
from holoviews import opts, dim

def Pitch(height, width):
    height, width = height, width
    line_color, pitch_color,pitch_linewidth = "black", "white", 1
    lin = np.linspace(0,np.pi/2,200)
    def corners(t,x,y,r,theta):
        return (x+r*np.cos(t+theta),y+r*np.sin(t+theta),t)
    def int_angles(radius, h, k, line_y):
        """
        Calculate the intersection angles of the arc above the D-boxes
    
        Parameters: 
            radius (float): Radius of the arc
            h(float): x coordinate of the centre of the arc
            k(float): y coordiante of the centre of the arc
            line_y(float): y coordinate of the D-box or the line to be intersected by the arc
    
        Returns: 
            theta1(float): First intersection angle
            theta2(float): Second intersection angle
        """
        x1 = h + np.sqrt(radius**2 - (line_y - k)**2) 
        x2 = h - np.sqrt(radius**2 - (line_y - k)**2)
        theta1 = np.arccos((x1-h)/radius)
        theta2 = np.pi - theta1
        return theta1, theta2
    theta1, theta2 = int_angles(0.075*height,width/2,0.1*height,0.15*height)
    lin2 = np.linspace(theta1,theta2,200)
    def boxarcs(t,x,y,r,theta):
        return (x+r*np.cos(t+theta),y+r*np.sin(t+theta),t)
    
    #Pitch outline
    matchpitch = hv.Curve([(0,0),(0,height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(0,height),(width,height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(width,height),(width,0)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(width,0),(0,0)]).opts(color = line_color)
    #Halfline
    matchpitch = matchpitch*hv.Curve([(0,height/2),(width, height/2)]).opts(color = line_color)
    #Bottom Penalty Area
    matchpitch = matchpitch*hv.Curve([(.225*width,0),(.225*width, .15*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.225*width, .15*height),(.775*width,.15*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.775*width, .15*height),(.775*width, 0)]).opts(color = line_color)
    #Top Penalty Area
    matchpitch = matchpitch*hv.Curve([(.225*width,height),(.225*width, .85*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.225*width, .85*height),(.775*width, .85*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.775*width, .85*height),(.775*width, height)]).opts(color = line_color)
    #Bottom 6 yard Box
    matchpitch = matchpitch*hv.Curve([(.375*width,0),(.375*width,0.05*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.375*width,0.05*height),(.625*width,0.05*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.625*width,0.05*height),(.625*width, 0)]).opts(color = line_color)   
    #Top 6 yard Box
    matchpitch = matchpitch*hv.Curve([(.375*width,height),(.375*width, .95*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.375*width, .95*height),(.625*width, .95*height)]).opts(color = line_color)
    matchpitch = matchpitch*hv.Curve([(.625*width, .95*height),(.625*width, height)]).opts(color = line_color)
    #Prepare Circles
    #Center circle and kickoff spot
    matchpitch = matchpitch*hv.Ellipse(width/2,height/2,2*.076*height).opts(color=line_color)
    matchpitch = matchpitch*hv.Points((width/2, height/2)).opts(color=line_color,size=5)
    #Bottom Penalty Spot 
    matchpitch = matchpitch*hv.Points((width/2,0.1*height)).opts(color=line_color,size=5)
    #Top Penalty Spot
    matchpitch = matchpitch*hv.Points((width/2.0, .9*height)).opts(color=line_color,size=5)
    #Bottom left corner
    matchpitch = matchpitch*hv.Path([corners(lin, 0, 0, 0.025*height, 0)]).opts(color=line_color)
    #Bottom right corner
    matchpitch = matchpitch*hv.Path([corners(lin, width, 0, 0.025*height, np.pi/2)]).opts(color=line_color)
    #Top left corner
    matchpitch = matchpitch*hv.Path([corners(lin, 0, height, 0.025*height, 3.0*np.pi/2)]).opts(color=line_color)
    #Top right corner
    matchpitch = matchpitch*hv.Path([corners(lin, width, height, 0.025*height, np.pi)]).opts(color=line_color)
    #Bottom box arc
    matchpitch = matchpitch*hv.Path([boxarcs(lin2, width/2, 0.1*height, 0.075*height, 0)]).opts(color=line_color)
    #Top box arc
    matchpitch = matchpitch*hv.Path([boxarcs(lin2, width/2, 0.9*height, 0.075*height, np.pi)]).opts(color=line_color)
    xl = -10
    xr = width + 10
    yb = -10
    yt = height + 10
    w = 2.5*(xr-xl)
    h = 2.5*(yt-yb)
    matchpitch.opts(width = w, height = h, xlim = (xl,xr), ylim = (yb,yt),data_aspect=1,
                   xaxis=None, yaxis=None)
    return matchpitch