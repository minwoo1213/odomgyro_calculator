from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='odomgyro_calculator',
            executable='calculate_main',
            name='odomgyro_calculator',
            output='screen'
        )
    ])
