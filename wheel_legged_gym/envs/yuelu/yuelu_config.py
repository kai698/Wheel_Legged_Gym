from wheel_legged_gym.envs.base.legged_robot_config import (
    LeggedRobotCfg,
    LeggedRobotCfgPPO,
)

class YueLuCfg(LeggedRobotCfg):

    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.3]  # x,y,z [m]
        default_joint_angles = {  # target angles when action = 0.0
            "lf0_Joint": -0.5,
            "lf1_Joint": -0.5,
            "l_wheel_Joint": 0.0,
            "rf0_Joint": 0.5,
            "rf1_Joint": 0.5,
            "r_wheel_Joint": 0.0,
        }

    class env(LeggedRobotCfg.env):
        num_privileged_obs = (
            LeggedRobotCfg.env.num_observations + 7 * 11 + 3 + 6 * 7 + 3 + 3
        )

    class control(LeggedRobotCfg.control):
        pos_action_scale = 0.5
        vel_action_scale = 10.0

        action_scale_theta = 0.5
        action_scale_l0 = 0.1
        action_scale_vel = 10.0

        l0_offset = 0.2
        feedforward_force = 50.0  # [N]

        kp_theta = 10.0  # [N*m/rad]
        kd_theta = 0.5  # [N*m*s/rad]
        kp_l0 = 600.0  # [N/m]
        kd_l0 = 10.0  # [N*s/m]

        # PD Drive parameters:
        stiffness = {"f0": 0.0, "f1": 0.0, "wheel": 0}  # [N*m/rad]
        damping = {"f0": 0.0, "f1": 0.0, "wheel": 0.125}  # [N*m*s/rad]

    class asset(LeggedRobotCfg.asset):
        file = "{WHEEL_LEGGED_GYM_ROOT_DIR}/resources/robots/yuelu/urdf/yuelu.urdf"
        name = "YueLu"
        offset = 0.075
        l1 = 0.15
        l2 = 0.27
        penalize_contacts_on = ["lf", "rf", "base"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 1  # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = False

    class normalization(LeggedRobotCfg.normalization):
        class obs_scales(LeggedRobotCfg.normalization.obs_scales):
            l0 = 5.0
            l0_dot = 0.25

    class noise(LeggedRobotCfg.noise):
        class noise_scales(LeggedRobotCfg.noise.noise_scales):
            l0 = 0.02
            l0_dot = 0.1

    class terrain(LeggedRobotCfg.terrain):
        mesh_type = "plane"


class YueLuCfgPPO(LeggedRobotCfgPPO):

    class runner(LeggedRobotCfgPPO.runner):
        # logging
        experiment_name = "yuelu"
        max_iterations = 2000

    class algorithm(LeggedRobotCfgPPO.algorithm):
        kl_decay = (
            LeggedRobotCfgPPO.algorithm.desired_kl - 0.002
        ) / LeggedRobotCfgPPO.runner.max_iterations

    
    