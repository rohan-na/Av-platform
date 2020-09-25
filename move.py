#!/usr/bin/python
import rospy
from geometry_msgs.msg import TwistStamped
from mavros_msgs.msg import Mavlink

def move():
    rospy.init_node('rover_move',anonymous=True)
    vel_publisher=rospy.Publisher('/mavros/setpoint_velocity/cmd_vel',TwistStamped,queue_size=10)
    vel_msg=TwistStamped()

    print("Move your rover")
    speed=input("Enter your speed")
    distance=input("How Far")
    isForward=input("Forward?")

    if(isForward):
        vel_msg.twist.linear.x=abs(speed)
    else:
        vel_msg.twist.linear.x=-abs(speed)

    vel_msg.twist.linear.y=0
    vel_msg.twist.linear.z=0
    vel_msg.twist.angular.x=0
    vel_msg.twist.angular.y=0
    vel_msg.twist.angular.z=0

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():

        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            vel_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance=speed*(t1-t0)
        vel_msg.twist.linear.x=0
        vel_publisher.publish(vel_msg)
        rate.sleep()

if __name__=='__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass

