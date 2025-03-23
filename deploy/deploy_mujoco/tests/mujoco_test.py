import mujoco
import mujoco.viewer
from wheel_legged_gym import WHEEL_LEGGED_GYM_ROOT_DIR

def main():
    # model path
    xml_path = f"{WHEEL_LEGGED_GYM_ROOT_DIR}/resources/robots/yuelu/xml/scene.xml"

    # load robot model
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

    # launch MuJoCo viewer
    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            mujoco.mj_step(model, data)
            # refresh viewer
            viewer.sync() 

if __name__ == "__main__":
    main()