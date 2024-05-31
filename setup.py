from setuptools import setup
import os
from glob import glob

package_name = 'odomgyro_calculator'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'odomgyro_calculator.calculate_main',
    ],
    data_files=[
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mwcha',
    maintainer_email='mwcha@neubility.co.kr',
    description='A ROS2 package to calculate yaw from odometry(/odomgyro)',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'calculate_main = odomgyro_calculator.calculate_main:main',
        ],
    },
)