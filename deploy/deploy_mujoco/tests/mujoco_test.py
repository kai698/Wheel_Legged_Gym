import mujoco
import mujoco.viewer
from wheel_legged_gym import WHEEL_LEGGED_GYM_ROOT_DIR

model_path = f"{WHEEL_LEGGED_GYM_ROOT_DIR}/resources/robots/yuelu/xml/scene.xml"
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
