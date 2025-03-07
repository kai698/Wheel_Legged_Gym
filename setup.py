from setuptools import find_packages
from distutils.core import setup

setup(
    name="wheel_legged_gym",
    version="1.0.0",
    author="kai",
    license="BSD-3-Clause",
    packages=find_packages(),
    description="Isaac Gym environments for Wheel Legged Robots",
    install_requires=[
        "isaacgym",
        "matplotlib",
        "tensorboard",
        "setuptools==59.5.0",
        "numpy>=1.16.4",
        "numpy<1.20.0",
        "GitPython",
        "onnx",
        'mujoco==3.2.3'
    ],
)
