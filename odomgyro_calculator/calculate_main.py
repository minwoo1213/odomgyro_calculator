#Dev on 240531 mwcha >.<
#Instagram @minwoo._.exfp
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Quaternion
from nav_msgs.msg import Odometry
import transforms3d.euler as euler

class OdomGyroCalculator(Node):

    def __init__(self):
        super().__init__('odomgyro_calculator')
        self.subscription = self.create_subscription(
            Odometry,
            '/odomgyro',
            self.odom_callback,
            10)
        self.subscription  # prevent unused variable warning !
        self.rate = self.create_rate(1.0)

    def quaternion_to_euler(self, quaternion):
        quat = [quaternion.w, quaternion.x, quaternion.y, quaternion.z]
        roll, pitch, yaw = euler.quat2euler(quat)
        return roll, pitch, yaw

    def odom_callback(self, msg):
        quaternion = msg.pose.pose.orientation
        roll, pitch, yaw = self.quaternion_to_euler(quaternion)    
        
        self.get_logger().info("\n")
        self.get_logger().info(f"Quaternion values:\n x: {quaternion.x}\n y: {quaternion.y}\n z: {quaternion.z}\n w: {quaternion.w}")
        self.get_logger().info(f"Converted Euler angles:\n R: {roll}\n P: {pitch}\n Y: {yaw}")
        #self.get_logger().info("\n")

def main(args=None):
    rclpy.init(args=args)
    node = OdomGyroCalculator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

