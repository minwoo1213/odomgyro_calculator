# odomgyro_calculator

A ROS 2 package to calculate yaw from odometry.
This package was developed by mwcha because checking better for /odomgyro topic on Neubie while handling Issue!

## Dependencies

This package depends on the following ROS 2 packages:

- rclpy
- geometry_msgs
- nav_msgs
- transforms3d (Dependency)
```bash
sudo apt-get update
sudo apt-get install ros-{$ROS_DISTRO}-desktop
pip install transforms3d
```

Make sure to have these packages installed in your ROS 2 environment before using `odomgyro_calculator`.

## Installation

1. Clone the repository into your ROS 2 workspace's `src` director

```bash
cd /{workspace}/src
git clone https://github.com/your_username/odomgyro_calculator.git
```

2. Build the package using colcon

```bash
cd /{workspace}/
colcon build
```

3. Source the setup script to add the package to your ROS 2 environment

```bash
source /{workspace}/install/local_setup.bash
```

4. Launch your package

```bash
ros2 launch odomgyro_calculator calculate_main.launch.py
```
