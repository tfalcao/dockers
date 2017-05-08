FROM ubuntu:16.04

MAINTAINER Thiago Falcao "thiagofalcao@gmail.com"

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get -qq update \
    && apt-get -qq upgrade -y \
    && apt-get -qq -y install \
    build-essential \
    wget unzip \
    cmake \
    qt5-default \
    libvtk6-dev \
    zlib1g-dev \
    libjpeg-dev \
    libwebp-dev \
    libpng-dev \
    libtiff5-dev \
    libjasper-dev \
    libopenexr-dev \
    libgdal-dev \
    libdc1394-22-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libtheora-dev \
    libvorbis-dev \
    libxvidcore-dev \
    libx264-dev yasm \
    libopencore-amrnb-dev \
    libopencore-amrwb-dev \
    libv4l-dev libxine2-dev \
    libtbb-dev libeigen3-dev \
    && apt-get autoremove && apt-get clean

WORKDIR /
RUN wget https://github.com/opencv/opencv/archive/3.2.0.zip -O opencv3.zip && \
    unzip -q opencv3.zip && mv /opencv-3.2.0 /opencv
RUN wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip -O opencv_contrib3.zip && \
    unzip -q opencv_contrib3.zip && mv /opencv_contrib-3.2.0 /opencv_contrib
RUN mkdir /opencv/build
WORKDIR /opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON \
    -D FORCE_VTK=ON \
    -D WITH_QT=ON \
    -D WITH_OPENGL=ON \
    -D WITH_TBB=ON \
    -D WITH_XINE=ON \
    -D WITH_GDAL=ON \
    -D WITH_IPP=OFF \
    -D WITH_V4L=ON ..
RUN make -j4
RUN make install
RUN ldconfig
