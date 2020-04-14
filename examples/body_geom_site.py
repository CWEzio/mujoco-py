# This example comes from Mujoco official document
from mujoco_py import load_model_from_xml, MjSim, MjViewer
import math
import os

MODEL_XML = """
<mujoco>
   <worldbody>
      <body pos="0 0 0">
         <geom type="sphere" size=".1" rgba=".9 .9 .1 1"/>
         <geom type="capsule" pos="0 0 .1" size=".05 .1" rgba=".9 .9 .1 1"/>
         <site type="box" pos="0 -.1 .3" size=".02 .02 .02" rgba=".9 .1 .9 1"/>
         <site type="ellipsoid" pos="0 .1 .3" size=".02 .03 .04" rgba=".9 .1 .9 1"/>
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
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
