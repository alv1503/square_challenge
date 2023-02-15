#! /usr/bin/env python3

# IMPORTACIONES

import rospy
from geometry_msgs.msg import Twist
from time import sleep

def move():
    rospy.init_node('square_challenge')
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    vel_msg = Twist
    
    for i in range 4:
        vel.msg.linear.x = 0
        vel.msg.angular.z = 0
        
        seconds = 5
        t = rospy.Time.now().to_sec()
        move_time = t + seconds
        
        while t < move_time:
            vel_msg.linear.x = 0.22
            velocity_publisher.publish(vel_msg)
            rate.sleep()
            t = rospy.Time.now().to_sec()
        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0.22
        
        sleep(4)
        
        velocity_publisher.publish(vel_msg)
    
    vel_msg.linear.x = 0
    vel_msg.linear.z = 0
    
if __name__ == '__main__':
    try:
        move()
        
    except rospy.ROSInterruptException: pass
