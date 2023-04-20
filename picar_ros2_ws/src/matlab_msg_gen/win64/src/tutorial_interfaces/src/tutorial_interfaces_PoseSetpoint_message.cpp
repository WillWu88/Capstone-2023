// Copyright 2020 The MathWorks, Inc.
// Common copy functions for tutorial_interfaces/PoseSetpoint
#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4100)
#pragma warning(disable : 4265)
#pragma warning(disable : 4456)
#pragma warning(disable : 4458)
#pragma warning(disable : 4946)
#pragma warning(disable : 4244)
#else
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wpedantic"
#pragma GCC diagnostic ignored "-Wunused-local-typedefs"
#pragma GCC diagnostic ignored "-Wredundant-decls"
#pragma GCC diagnostic ignored "-Wnon-virtual-dtor"
#pragma GCC diagnostic ignored "-Wdelete-non-virtual-dtor"
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wshadow"
#endif //_MSC_VER
#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/msg/pose_setpoint.hpp"
#include "visibility_control.h"
#include "class_loader/multi_library_class_loader.hpp"
#include "ROS2PubSubTemplates.hpp"
class TUTORIAL_INTERFACES_EXPORT tutorial_interfaces_msg_PoseSetpoint_common : public MATLABROS2MsgInterface<tutorial_interfaces::msg::PoseSetpoint> {
  public:
    virtual ~tutorial_interfaces_msg_PoseSetpoint_common(){}
    virtual void copy_from_struct(tutorial_interfaces::msg::PoseSetpoint* msg, const matlab::data::Struct& arr, MultiLibLoader loader); 
    //----------------------------------------------------------------------------
    virtual MDArray_T get_arr(MDFactory_T& factory, const tutorial_interfaces::msg::PoseSetpoint* msg, MultiLibLoader loader, size_t size = 1);
};
  void tutorial_interfaces_msg_PoseSetpoint_common::copy_from_struct(tutorial_interfaces::msg::PoseSetpoint* msg, const matlab::data::Struct& arr,
               MultiLibLoader loader) {
    try {
        //header
        const matlab::data::StructArray header_arr = arr["header"];
        static auto msgClassPtr_header = loader->createInstance<MATLABROS2MsgInterface<std_msgs::msg::Header>>("std_msgs_msg_Header_common");
        msgClassPtr_header->copy_from_struct(&msg->header,header_arr[0],loader);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'header' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'header' is wrong type; expected a struct.");
    }
    try {
        //yawsetpoint
        const matlab::data::TypedArray<double> yawsetpoint_arr = arr["yawsetpoint"];
        msg->yawsetpoint = yawsetpoint_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'yawsetpoint' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'yawsetpoint' is wrong type; expected a double.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T tutorial_interfaces_msg_PoseSetpoint_common::get_arr(MDFactory_T& factory, const tutorial_interfaces::msg::PoseSetpoint* msg,
       MultiLibLoader loader, size_t size) {
    auto outArray = factory.createStructArray({size,1},{"MessageType","header","yawsetpoint"});
    for(size_t ctr = 0; ctr < size; ctr++){
    outArray[ctr]["MessageType"] = factory.createCharArray("tutorial_interfaces/PoseSetpoint");
    // header
    auto currentElement_header = (msg + ctr)->header;
    static auto msgClassPtr_header = loader->createInstance<MATLABROS2MsgInterface<std_msgs::msg::Header>>("std_msgs_msg_Header_common");
    outArray[ctr]["header"] = msgClassPtr_header->get_arr(factory, &currentElement_header, loader);
    // yawsetpoint
    auto currentElement_yawsetpoint = (msg + ctr)->yawsetpoint;
    outArray[ctr]["yawsetpoint"] = factory.createScalar(currentElement_yawsetpoint);
    }
    return std::move(outArray);
  } 
class TUTORIAL_INTERFACES_EXPORT tutorial_interfaces_PoseSetpoint_message : public ROS2MsgElementInterfaceFactory {
  public:
    virtual ~tutorial_interfaces_PoseSetpoint_message(){}
    virtual std::shared_ptr<MATLABPublisherInterface> generatePublisherInterface();
    virtual std::shared_ptr<MATLABSubscriberInterface> generateSubscriberInterface();
};  
  std::shared_ptr<MATLABPublisherInterface> 
          tutorial_interfaces_PoseSetpoint_message::generatePublisherInterface(){
    return std::make_shared<ROS2PublisherImpl<tutorial_interfaces::msg::PoseSetpoint,tutorial_interfaces_msg_PoseSetpoint_common>>();
  }
  std::shared_ptr<MATLABSubscriberInterface> 
         tutorial_interfaces_PoseSetpoint_message::generateSubscriberInterface(){
    return std::make_shared<ROS2SubscriberImpl<tutorial_interfaces::msg::PoseSetpoint,tutorial_interfaces_msg_PoseSetpoint_common>>();
  }
#include "class_loader/register_macro.hpp"
// Register the component with class_loader.
// This acts as a sort of entry point, allowing the component to be discoverable when its library
// is being loaded into a running process.
CLASS_LOADER_REGISTER_CLASS(tutorial_interfaces_msg_PoseSetpoint_common, MATLABROS2MsgInterface<tutorial_interfaces::msg::PoseSetpoint>)
CLASS_LOADER_REGISTER_CLASS(tutorial_interfaces_PoseSetpoint_message, ROS2MsgElementInterfaceFactory)
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif //_MSC_VER