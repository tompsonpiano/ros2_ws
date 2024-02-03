import rclpy
from rclpy.node import Node
from person_msgs.srv import Query
 
def cb(request, response):
    if request.name == "上田隆一":
        response.age = 44
    else:
        response.age = 255

<<<<<<< HEAD
    return response
 
rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
=======
class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
>>>>>>> lesson10
rclpy.spin(node)