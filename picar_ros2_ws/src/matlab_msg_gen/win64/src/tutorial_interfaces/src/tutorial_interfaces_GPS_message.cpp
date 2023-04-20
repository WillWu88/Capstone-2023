// Copyright 2020 The MathWorks, Inc.
// Common copy functions for tutorial_interfaces/GPS
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
#include "tutorial_interfaces/msg/gps.hpp"
#include "visibility_control.h"
#include "class_loader/multi_library_class_loader.hpp"
#include "ROS2PubSubTemplates.hpp"
class TUTORIAL_INTERFACES_EXPORT tutorial_interfaces_msg_GPS_common : public MATLABROS2MsgInterface<tutorial_interfaces::msg::GPS> {
  public:
    virtual ~tutorial_interfaces_msg_GPS_common(){}
    virtual void copy_from_struct(tutorial_interfaces::msg::GPS* msg, const matlab::data::Struct& arr, MultiLibLoader loader); 
    //----------------------------------------------------------------------------
    virtual MDArray_T get_arr(MDFactory_T& factory, const tutorial_interfaces::msg::GPS* msg, MultiLibLoader loader, size_t size = 1);
};
  void tutorial_interfaces_msg_GPS_common::copy_from_struct(tutorial_interfaces::msg::GPS* msg, const matlab::data::Struct& arr,
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
        //latdeg
        const matlab::data::TypedArray<double> latdeg_arr = arr["latdeg"];
        msg->latdeg = latdeg_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'latdeg' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'latdeg' is wrong type; expected a double.");
    }
    try {
        //longdeg
        const matlab::data::TypedArray<double> longdeg_arr = arr["longdeg"];
        msg->longdeg = longdeg_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'longdeg' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'longdeg' is wrong type; expected a double.");
    }
    try {
        //latmin
        const matlab::data::TypedArray<double> latmin_arr = arr["latmin"];
        msg->latmin = latmin_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'latmin' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'latmin' is wrong type; expected a double.");
    }
    try {
        //longmin
        const matlab::data::TypedArray<double> longmin_arr = arr["longmin"];
        msg->longmin = longmin_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'longmin' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'longmin' is wrong type; expected a double.");
    }
    try {
        //flag
        const matlab::data::TypedArray<bool> flag_arr = arr["flag"];
        msg->flag = flag_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'flag' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'flag' is wrong type; expected a logical.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T tutorial_interfaces_msg_GPS_common::get_arr(MDFactory_T& factory, const tutorial_interfaces::msg::GPS* msg,
       MultiLibLoader loader, size_t size) {
    auto outArray = factory.createStructArray({size,1},{"MessageType","header","latdeg","longdeg","latmin","longmin","flag"});
    for(size_t ctr = 0; ctr < size; ctr++){
    outArray[ctr]["MessageType"] = factory.createCharArray("tutorial_interfaces/GPS");
    // header
    auto currentElement_header = (msg + ctr)->header;
    static auto msgClassPtr_header = loader->createInstance<MATLABROS2MsgInterface<std_msgs::msg::Header>>("std_msgs_msg_Header_common");
    outArray[ctr]["header"] = msgClassPtr_header->get_arr(factory, &currentElement_header, loader);
    // latdeg
    auto currentElement_latdeg = (msg + ctr)->latdeg;
    outArray[ctr]["latdeg"] = factory.createScalar(currentElement_latdeg);
    // longdeg
    auto currentElement_longdeg = (msg + ctr)->longdeg;
    outArray[ctr]["longdeg"] = factory.createScalar(currentElement_longdeg);
    // latmin
    auto currentElement_latmin = (msg + ctr)->latmin;
    outArray[ctr]["latmin"] = factory.createScalar(currentElement_latmin);
    // longmin
    auto currentElement_longmin = (msg + ctr)->longmin;
    outArray[ctr]["longmin"] = factory.createScalar(currentElement_longmin);
    // flag
    auto currentElement_flag = (msg + ctr)->flag;
    outArray[ctr]["flag"] = factory.createScalar(currentElement_flag);
    }
    return std::move(outArray);
  } 
class TUTORIAL_INTERFACES_EXPORT tutorial_interfaces_GPS_message : public ROS2MsgElementInterfaceFactory {
  public:
    virtual ~tutorial_interfaces_GPS_message(){}
    virtual std::shared_ptr<MATLABPublisherInterface> generatePublisherInterface();
    virtual std::shared_ptr<MATLABSubscriberInterface> generateSubscriberInterface();
};  
  std::shared_ptr<MATLABPublisherInterface> 
          tutorial_interfaces_GPS_message::generatePublisherInterface(){
    return std::make_shared<ROS2PublisherImpl<tutorial_interfaces::msg::GPS,tutorial_interfaces_msg_GPS_common>>();
  }
  std::shared_ptr<MATLABSubscriberInterface> 
         tutorial_interfaces_GPS_message::generateSubscriberInterface(){
    return std::make_shared<ROS2SubscriberImpl<tutorial_interfaces::msg::GPS,tutorial_interfaces_msg_GPS_common>>();
  }
#include "class_loader/register_macro.hpp"
// Register the component with class_loader.
// This acts as a sort of entry point, allowing the component to be discoverable when its library
// is being loaded into a running process.
CLASS_LOADER_REGISTER_CLASS(tutorial_interfaces_msg_GPS_common, MATLABROS2MsgInterface<tutorial_interfaces::msg::GPS>)
CLASS_LOADER_REGISTER_CLASS(tutorial_interfaces_GPS_message, ROS2MsgElementInterfaceFactory)
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif //_MSC_VER