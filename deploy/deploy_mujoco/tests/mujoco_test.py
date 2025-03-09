import mujoco
import mujoco.viewer
from wheel_legged_gym import WHEEL_LEGGED_GYM_ROOT_DIR
import yaml
import argparse

def main():
    # get config file name from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str, help="config file name in the config folder")
    args = parser.parse_args()
    config_file = args.config_file

    with open(f"{WHEEL_LEGGED_GYM_ROOT_DIR}/deploy/deploy_mujoco/configs/{config_file}", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        xml_path = config["xml_path"].replace("{WHEEL_LEGGED_GYM_ROOT_DIR}", WHEEL_LEGGED_GYM_ROOT_DIR)

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