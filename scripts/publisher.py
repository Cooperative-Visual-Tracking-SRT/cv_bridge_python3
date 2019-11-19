#!/usr/bin/env python3

import rospkg
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2

if __name__ == '__main__':
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('camera', Image, queue_size=2)
    rate = rospy.Rate(20)

    cap = cv2.VideoCapture(0)
    assert cap.isOpened(), 'Camera is not available.'

    bridge = CvBridge()

    while not rospy.is_shutdown():
        _, frame = cap.read()
        msg = bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        pub.publish(msg)
        rate.sleep()

    cap.release()