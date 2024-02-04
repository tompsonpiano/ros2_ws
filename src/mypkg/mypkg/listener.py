import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():

    def cb(msg):
        #global node
        node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
#pub = node.create_subscription(Int16, "countup", cb, 10)
listner = Listener(node)
rclpy.spin(node)