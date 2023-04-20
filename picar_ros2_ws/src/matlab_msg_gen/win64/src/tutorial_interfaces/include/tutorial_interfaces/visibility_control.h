#ifndef TUTORIAL_INTERFACES__VISIBILITY_CONTROL_H_
#define TUTORIAL_INTERFACES__VISIBILITY_CONTROL_H_
#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define TUTORIAL_INTERFACES_EXPORT __attribute__ ((dllexport))
    #define TUTORIAL_INTERFACES_IMPORT __attribute__ ((dllimport))
  #else
    #define TUTORIAL_INTERFACES_EXPORT __declspec(dllexport)
    #define TUTORIAL_INTERFACES_IMPORT __declspec(dllimport)
  #endif
  #ifdef TUTORIAL_INTERFACES_BUILDING_LIBRARY
    #define TUTORIAL_INTERFACES_PUBLIC TUTORIAL_INTERFACES_EXPORT
  #else
    #define TUTORIAL_INTERFACES_PUBLIC TUTORIAL_INTERFACES_IMPORT
  #endif
  #define TUTORIAL_INTERFACES_PUBLIC_TYPE TUTORIAL_INTERFACES_PUBLIC
  #define TUTORIAL_INTERFACES_LOCAL
#else
  #define TUTORIAL_INTERFACES_EXPORT __attribute__ ((visibility("default")))
  #define TUTORIAL_INTERFACES_IMPORT
  #if __GNUC__ >= 4
    #define TUTORIAL_INTERFACES_PUBLIC __attribute__ ((visibility("default")))
    #define TUTORIAL_INTERFACES_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define TUTORIAL_INTERFACES_PUBLIC
    #define TUTORIAL_INTERFACES_LOCAL
  #endif
  #define TUTORIAL_INTERFACES_PUBLIC_TYPE
#endif
#endif  // TUTORIAL_INTERFACES__VISIBILITY_CONTROL_H_
// Generated 19-Apr-2023 19:08:59
 