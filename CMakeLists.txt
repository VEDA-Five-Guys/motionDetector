cmake_minimum_required(VERSION 3.10)
project(practice)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# include 디렉토리 추가
include_directories(${PROJECT_SOURCE_DIR}/include)

# Python 라이브러리 찾기
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
if (NOT Python3_FOUND)
    message(FATAL_ERROR "Python3 not found!")
endif()

# Boost 라이브러리 찾기
find_package(Boost REQUIRED COMPONENTS system thread)
if (NOT Boost_FOUND)
    message(FATAL_ERROR "Boost not found!")
endif()

# Boost 및 Python 헤더 포함
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${Python3_INCLUDE_DIRS})

# 소스 파일 목록
set(SOURCES
    source/message_queue.cpp
    source/python_module.cpp
    source/websocket_client.cpp
    main.cpp
)

# 실행 파일 생성
add_executable(motion_detector ${SOURCES})

# 라이브러리 링크
target_link_libraries(motion_detector
    ${Boost_LIBRARIES}
    ${Python3_LIBRARIES}
    pthread
)
