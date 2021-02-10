cmake_minimum_required(VERSION 3.17)
project(TTK4900_Master)

find_package(OpenCV 4 CONFIG REQUIRED)
find_package(Eigen3 3.3.4 CONFIG REQUIRED)
find_package(Sophus CONFIG REQUIRED)

set(CMAKE_CXX_STANDARD 14)

add_executable(TTK4900_Master main.cpp testFunctions.cpp testFunctions.h stereoCalibTest.cpp)
target_link_libraries(${PROJECT_NAME}
        ${OpenCV_LIBS}
        Eigen3::Eigen
        Sophus::Sophus
        )