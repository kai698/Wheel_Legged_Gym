import mujoco
import mujoco.viewer

model_path = "/home/kai/mujoco-3.2.3/model/humanoid/humanoid.xml"
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
