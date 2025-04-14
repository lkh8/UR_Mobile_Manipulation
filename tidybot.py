import numpy as np
from robosuite.robots import register_robot_class
from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.models.bases.mobile_base_model import MobileBaseModel
from robosuite.utils.mjcf_utils import xml_path_completion
from robosuite.models.bases import register_base
from robosuite.models.robots.manipulators.kinova3_robot import Kinova3
import robosuite as suite
from robosuite.controllers import load_composite_controller_config
from robosuite.models.robots import Panda
import mujoco

@register_base
class TidyBase(MobileBaseModel):
    """
    TidyBot Base

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("stanford_tidybot/base.xml"), idn =idn)

    @property
    def top_offset(self):
        return np.array([0, 0, 0])
    
    @property
    def horizontal_radius(self):
        return 0.25


@register_robot_class("WheeledRobot")
class TidyBot(Kinova3):
    @property 
    def default_base(self):
        return "TidyBase"
    
    # @property
    # def default_base(self):
    #     return "OmronMobileBase"
     
    @property
    def init_qpos(self):
        return np.array([0.00, np.radians(-15), 0.00, np.radians(15), 0.00, np.pi / 2, -np.pi / 2])
    @property
    def default_arm(self):
        return {"right": "Kinova3"}
    


# env = suite.make(
#     env_name="Lift",
#     robots="TidyBot",
#     controller_configs=load_composite_controller_config(controller="BASIC"),
#     has_renderer=True,
#     has_offscreen_renderer=False,
#     render_camera="agentview",
#     use_camera_obs=False,
#     control_freq=20,
# )

# # Run the simulation, and visualize it
# env.reset()
# print("successfully")
# mujoco.viewer.launch(env.sim.model._model, env.sim.data._data)

# @register_robot_class("WheeledRobot")
# class MobilePanda(Panda):
#     @property
#     def default_base(self):
#         return "OmronMobileBase"

#     @property
#     def default_arms(self):
#         return {"right": "Panda"}

# # Create environment
# env = suite.make(
#     env_name="Lift",
#     robots="MobilePanda",
#     controller_configs=load_composite_controller_config(controller="BASIC"),
#     has_renderer=True,
#     has_offscreen_renderer=False,
#     render_camera="agentview",
#     use_camera_obs=False,
#     control_freq=20,
# )

# # Run the simulation, and visualize it
# env.reset()
# mujoco.viewer.launch(env.sim.model._model, env.sim.data._data)