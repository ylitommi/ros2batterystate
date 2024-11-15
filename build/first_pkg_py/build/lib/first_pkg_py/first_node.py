import rclpy
from rclpy.node import Node

from sensor_msgs.msg import BatteryState
    


class Tilaaja(Node):

    def __init__(self):
        super().__init__('Tilaaja')
        self.subscription = self.create_subscription(
            BatteryState,
            'battery/battery_status',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Akun varaustaso: "%s"' % msg.percentage)
        self.get_logger().info(f"Akun jännite {msg.voltage}")


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Tilaaja()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()