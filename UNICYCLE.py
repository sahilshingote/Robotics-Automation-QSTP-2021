"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose 
        """
        
        self.v=v
        self.w=w
        self.n=n
        i=1
        j=1
        k=1
        #To calculate position after timestamps
        for k in range(1,self.n):
            
            self.theta=self.w*self.dt*k
            self.x=self.v*np.cos(self.theta)*self.dt
            self.y=self.v*np.sin(self.theta)*self.dt
            k+=1
            while i<self.n:
                    self.x_points.append(self.x)
                    i+=1
            while j<self.n:
                    self.y_points.append(self.y)
                    j+=1
        
        

        return self.x, self.y, self.theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        
        plt.show()
        
         #plt.savefig(f"Unicycle_{v}_{w}.png")

        
    
    
    






if __name__ == "__main__":
    print("Unicycle Model Assignment")

    # make an object of the robot and plot various trajectories
#EXECUTION2
#2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
exec=Unicycle(0,0,1.57,0.2)
exec.step(0.5,1,10)
exec.x_points
#exec.plot(0.5,1)