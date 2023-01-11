# SPDX-FileCopyrightText: 2022 Shuma Kasai
# SPDX-License-Indentifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Query

def cb(request, response):
    if request.name == "葛西柊摩":
        request.age = 19
    else:
        response.age = 255
    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
