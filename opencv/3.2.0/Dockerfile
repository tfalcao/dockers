FROM thiagofalcao/python2.7

MAINTAINER Thiago Falcao "thiagofalcao@gmail.com"

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    wget \
    unzip \
    cmake \
    git \
    pkg-config \
    libatlas-base-dev \
    gfortran \
    libjasper-dev \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjasper-dev \
    libv4l-dev \
    && apt-get autoremove \
    && apt-get clean

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


WORKDIR /
RUN wget https://github.com/opencv/opencv/archive/3.2.0.zip -O opencv3.zip && \
    unzip -q opencv3.zip && mv /opencv-3.2.0 /opencv
RUN wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip -O opencv_contrib3.zip && \
    unzip -q opencv_contrib3.zip && mv /opencv_contrib-3.2.0 /opencv_contrib
RUN mkdir /opencv/build
WORKDIR /opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D BUILD_PYTHON_SUPPORT=ON \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D WITH_IPP=OFF \
    -D WITH_V4L=ON ..
RUN make -j4
RUN make install
RUN ldconfig

WORKDIR /app