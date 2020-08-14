from mujoco_py import load_model_from_xml, MjSim, MjViewer
import os
import numpy as np

MODEL_XML = """
<?xml version="1.0" ?>
<mujoco>
    <option timestep="0.001" />
    <compiler inertiafromgeom="false" coordinate="global"/>
    <asset>
        <texture type="skybox" builtin="gradient" rgb1="0.3 0.5 0.7" rgb2="0 0 0" width="512" height="512"/> 

        <texture name="texplane" type="2d" builtin="checker" rgb1=".2 .3 .4" rgb2=".1 0.15 0.2" width="512" height="512" mark="cross" markrgb=".8 .8 .8"/>  

        <texture name="texgeom" type="cube" builtin="flat" mark="cross" width="127" height="1278" 
            rgb1="0.8 0.6 0.4" rgb2="0.8 0.6 0.4" markrgb="1 1 1" random="0.01"/>  

        <material name="matplane" reflectance="0.3" texture="texplane" texrepeat="1 1" texuniform="true"/>

        <material name="matgeom" texture="texgeom" texuniform="true" rgba="0.8 0.6 .4 1"/>
    </asset>
    
    <worldbody>
        <geom name="floor" pos="0 0 0" size="0 0 .25" type="plane" material="matplane" condim="3"/>
        <light directional="false" diffuse=".2 .2 .2" specular="0 0 0" pos="0 0 5" dir="0 0 -1" castshadow="false"/>
        
        
        <body>
            <inertial pos="0 0 0.29" mass="9" diaginertia="0.07 0.26 0.242" />
            <geom type="box" pos="0 0 0.29" size="0.38 0.228 0.05" rgba="0.9 0.9 0.1 1" />
            <joint type="free"/>
        </body>
        
    </worldbody>
            
</mujoco>
"""

model = load_model_from_xml(MODEL_XML)
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    t += 1
    sim.step()
    data = sim.data
    sim.data.xfrc_applied[1, :] = np.array([0.1, 0, 9*9.82, 0, 0, 0.1])  # external force is expressed in global frame
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
