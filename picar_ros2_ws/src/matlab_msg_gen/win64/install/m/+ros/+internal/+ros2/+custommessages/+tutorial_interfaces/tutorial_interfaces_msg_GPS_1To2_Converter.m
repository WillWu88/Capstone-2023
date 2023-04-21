function ros2msg = tutorial_interfaces_msg_GPS_1To2_Converter(message,ros2msg)
%tutorial_interfaces_msg_GPS_1To2_Converter passes data of ROS message to ROS 2 message.
% Copyright 2019 The MathWorks, Inc.
ros2msg.header.stamp.sec = message.Header.Stamp.Sec;
ros2msg.header.stamp.nanosec = message.Header.Stamp.Nsec;
ros2msg.header.frame_id = message.Header.FrameId;
ros2msg.latdeg = message.Latdeg;
ros2msg.longdeg = message.Longdeg;
ros2msg.latmin = message.Latmin;
ros2msg.longmin = message.Longmin;
ros2msg.flag = message.Flag;
end