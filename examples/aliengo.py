from mujoco_py import load_model_from_path, MjSim, MjViewer
import numpy as np
import os

model = load_model_from_path("/home/chenwang/mujoco_aliengo/aliengo_description/xacro/aliengo5.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0


def feet_contact(sim):
    feet_contact = []
    for i in range(4):
        if np.abs(sim.data.geom_xpos[13 + 8*i][2]) < 0.05:
            feet_contact.append(True)
        else:
            feet_contact.append(False)
    return feet_contact

while True:
    t += 1
    data = sim.data
    print(feet_contact(sim))
    if t == 115:
        print(t)
    sim.step()
    viewer.render()

    if t > 100 and os.getenv('TESTING') is not None:
        break
