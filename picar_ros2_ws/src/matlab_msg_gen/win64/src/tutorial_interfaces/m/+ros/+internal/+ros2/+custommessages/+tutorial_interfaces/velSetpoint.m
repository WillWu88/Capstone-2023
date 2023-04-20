function [data, info] = velSetpoint
%VelSetpoint gives an empty data for tutorial_interfaces/VelSetpoint
% Copyright 2019-2020 The MathWorks, Inc.
data = struct();
data.MessageType = 'tutorial_interfaces/VelSetpoint';
[data.header, info.header] = ros.internal.ros2.messages.std_msgs.header;
info.header.MLdataType = 'struct';
[data.xvelsetpoint, info.xvelsetpoint] = ros.internal.ros2.messages.ros2.default_type('double',1,0);
[data.yvelsetpoint, info.yvelsetpoint] = ros.internal.ros2.messages.ros2.default_type('double',1,0);
info.MessageType = 'tutorial_interfaces/VelSetpoint';
info.constant = 0;
info.default = 0;
info.maxstrlen = NaN;
info.MaxLen = 1;
info.MinLen = 1;
info.MatPath = cell(1,7);
info.MatPath{1} = 'header';
info.MatPath{2} = 'header.stamp';
info.MatPath{3} = 'header.stamp.sec';
info.MatPath{4} = 'header.stamp.nanosec';
info.MatPath{5} = 'header.frame_id';
info.MatPath{6} = 'xvelsetpoint';
info.MatPath{7} = 'yvelsetpoint';
