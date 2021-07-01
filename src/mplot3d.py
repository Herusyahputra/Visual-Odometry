"""
Project: Visual Odometry
Name : Heru-05 | M09158023
Date
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# use mplotlib figure to draw in 3D trajectories 

kPlotSleep = 0.0001 
class Mplot3d:
    def __init__(self, title=''):
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d') 
        if title is not '':
            self.ax.set_title(title)     
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')		   		

        self.axis_computed = False 
        self.xlim = [float("inf"),float("-inf")]
        self.ylim = [float("inf"),float("-inf")]
        self.zlim = [float("inf"),float("-inf")]        

        self.handle_map = {}
        self.setAxis()

    def setAxis(self):		
        self.ax.axis('equal')        
        if self.axis_computed:	
            self.ax.set_xlim(self.xlim)
            self.ax.set_ylim(self.ylim)  
            self.ax.set_zlim(self.zlim)                             
        self.ax.legend()

    def drawTraj(self, traj, name, color='r', marker='.'):
        np_traj = np.asarray(traj)        
        if name in self.handle_map:
            handle = self.handle_map[name]
            self.ax.collections.remove(handle)
        self.updateMinMax(np_traj)
        handle = self.ax.scatter3D(np_traj[:, 0], np_traj[:, 1], np_traj[:, 2], c=color, marker=marker)
        handle.set_label(name)
        self.handle_map[name] = handle

    def updateMinMax(self, np_traj):
        xmax,ymax,zmax = np.amax(np_traj,axis=0)
        xmin,ymin,zmin = np.amin(np_traj,axis=0)        
        cx = 0.5*(xmax+xmin)
        cy = 0.5*(ymax+ymin)
        cz = 0.5*(zmax+zmin) 
        if False: 
            # update maxs       
            if xmax > self.xlim[1]:
                self.xlim[1] = xmax 
            if ymax > self.ylim[1]:
                self.ylim[1] = ymax 
            if zmax > self.zlim[1]:
                self.zlim[1] = zmax                         
            # update mins
            if xmin < self.xlim[0]:
                self.xlim[0] = xmin   
            if ymin < self.ylim[0]:
                self.ylim[0] = ymin        
            if zmin < self.zlim[0]:
                self.zlim[0] = zmin     
        # make axis actually squared
        if True:
            #smin = min(self.xlim[0],self.ylim[0],self.zlim[0])                                            
            #smax = max(self.xlim[1],self.ylim[1],self.zlim[1])
            smin = min(xmin,ymin,zmin)                                            
            smax = max(xmax,ymax,zmax)            
            delta = 0.5*(smax - smin)
            self.xlim = [cx-delta,cx+delta]
            self.ylim = [cy-delta,cy+delta]
            self.zlim = [cz-delta,cz+delta]      
        self.axis_computed = True   

    def refresh(self):
        self.setAxis()
        plt.pause(kPlotSleep)
