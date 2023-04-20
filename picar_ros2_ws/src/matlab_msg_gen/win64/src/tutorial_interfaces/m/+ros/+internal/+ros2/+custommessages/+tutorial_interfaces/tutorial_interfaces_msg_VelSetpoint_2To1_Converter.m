function ros1msg = tutorial_interfaces_msg_VelSetpoint_2To1_Converter(message,ros1msg)
%tutorial_interfaces_msg_VelSetpoint_2To1_Converter passes data of ROS 2 message to ROS message.
% Copyright 2019 The MathWorks, Inc.    
ros1msg.Header.Stamp.Sec = message.header.stamp.sec;
ros1msg.Header.Stamp.Nsec = message.header.stamp.nanosec;
ros1msg.Header.FrameId = message.header.frame_id{1};
ros1msg.Xvelsetpoint = message.xvelsetpoint;
ros1msg.Yvelsetpoint = message.yvelsetpoint;
end