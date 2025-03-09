import time
import mujoco.viewer
import mujoco
from wheel_legged_gym import WHEEL_LEGGED_GYM_ROOT_DIR
import torch
import yaml
import argparse

class WheelLegged():
    def __init__(self, config):
        self.policy_path = config["policy_path"].replace("{WHEEL_LEGGED_GYM_ROOT_DIR}", WHEEL_LEGGED_GYM_ROOT_DIR)
        self.xml_path = config["xml_path"].replace("{WHEEL_LEGGED_GYM_ROOT_DIR}", WHEEL_LEGGED_GYM_ROOT_DIR)

        self.simulation_duration = config["simulation_duration"]
        self.simulation_dt = config["simulation_dt"]
        self.control_decimation = config["control_decimation"]

        self.num_actions = config["num_actions"]
        self.num_obs = config["num_obs"]

        self.offset = config["offset"]
        self.l1 = config["l1"]
        self.l2 = config["l2"]
        self.l0_offset = config["l0_offset"]
        self.feedforward_force = config["feedforward_force"]
        self.default_angles = torch.tensor(config["default_angles"], dtype=torch.float)

        self.kp_theta = config["kp_theta"]
        self.kd_theta = config["kd_theta"]
        self.kp_l0 = config["kp_l0"]
        self.kd_l0 = config["kd_l0"]
        self.kd_wheel = config["kd_wheel"]

        self.action_scale_theta = config["action_scale_theta"]
        self.action_scale_l0 = config["action_scale_l0"]
        self.action_scale_vel = config["action_scale_vel"]

        self.ang_vel_scale = config["ang_vel_scale"]
        self.dof_pos_scale = config["dof_vel_scale"]
        self.torque_scale = config["torque_scale"]
        self.cmd_scale = torch.tensor(config["cmd_scale"], dtype=torch.float)

    def init_state(self):
        # load robot model
        self.model = mujoco.MjModel.from_xml_path(self.xml_path)
        self.data = mujoco.MjData(self.model)
        # set default angles
        self.data.qpos[7:] += self.default_angles.numpy()

    def set_camera(self, camera):
        # get target id
        target_body = "base_link"
        target_id = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_BODY, target_body)
        # get target pos
        target_pos = self.data.xpos[target_id]
        # set camera
        camera.fixedcamid = -1  
        camera.type = mujoco.mjtCamera.mjCAMERA_TRACKING  
        camera.trackbodyid = target_id  
        camera.lookat[:] = target_pos 
        camera.distance = 2.0  
        camera.elevation = -20  
        camera.azimuth = 90

    
def main():
    # get config file name from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str, help="config file name in the config folder")
    args = parser.parse_args()
    config_file = args.config_file
    with open(f"{WHEEL_LEGGED_GYM_ROOT_DIR}/deploy/deploy_mujoco/configs/{config_file}", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        env = WheelLegged(config=config)

    # init
    env.init_state()

    # launch MuJoCo viewer
    with mujoco.viewer.launch_passive(env.model, env.data) as viewer:
        while viewer.is_running():
            mujoco.mj_step(env.model, env.data)
            env.set_camera(camera=viewer.cam)
            viewer.sync() 

if __name__ == "__main__":
    main()
        

