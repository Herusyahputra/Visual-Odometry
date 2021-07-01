"""
Project: Visual Odometry
Name : Heru-05 | M09158023
Date
"""

import numpy as np
import matplotlib.pyplot as plt

# use mplotlib figure to draw in 2d dynamic data

kPlotSleep = 0.0001 

class Mplot2d:
    def __init__(self, xlabel='', ylabel='', title=''):
        self.fig = plt.figure()
        #self.ax = self.fig.gca(projection='3d')
        self.ax = self.fig.gca()
        if title is not '':
            self.ax.set_title(title) 
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)	   
        self.ax.grid()		
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)

        self.axis_computed = False 
        self.xlim = [float("inf"),float("-inf")]
        self.ylim = [float("inf"),float("-inf")]    

        self.handle_map = {}
        self.setAxis()

    def setAxis(self):		
        # self.ax.axis('equal')        
        # if self.axis_computed:	
        #     self.ax.set_xlim(self.xlim)
        #     self.ax.set_ylim(self.ylim)                           
        self.ax.legend()
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()        

    def draw(self, xy_signal, name, color='r', marker='.'):  
        if name in self.handle_map:
            handle = self.handle_map[name]
            handle.set_xdata(np.append(handle.get_xdata(), xy_signal[0]))
            handle.set_ydata(np.append(handle.get_ydata(), xy_signal[1]))                
        else: 
            handle, = self.ax.plot(xy_signal[0], xy_signal[1], c=color, marker=marker,label=name)    
            self.handle_map[name] = handle

    def updateMinMax(self, np_signal):
        xmax,ymax = np.amax(np_signal,axis=0)
        xmin,ymin = np.amin(np_signal,axis=0)        
        cx = 0.5*(xmax+xmin)
        cy = 0.5*(ymax+ymin) 
        if False: 
            # update maxs       
            if xmax > self.xlim[1]:
                self.xlim[1] = xmax 
            if ymax > self.ylim[1]:
                self.ylim[1] = ymax                   
            # update mins
            if xmin < self.xlim[0]:
                self.xlim[0] = xmin   
            if ymin < self.ylim[0]:
                self.ylim[0] = ymin        
        # make axis actually squared
        if True:
            smin = min(xmin,ymin)                                            
            smax = max(xmax,ymax)            
            delta = 0.5*(smax - smin)
            self.xlim = [cx-delta,cx+delta]
            self.ylim = [cy-delta,cy+delta]   
        self.axis_computed = True   

    def refresh(self):
        self.setAxis()
        plt.pause(kPlotSleep)