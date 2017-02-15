FROM ubuntu:14.04
MAINTAINER Thiago Falcao "thiagofalcao@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

# Python
RUN apt-get update
RUN apt-get install -y \
    python2.7-dev python-pip wget unzip \
    build-essential cmake git pkg-config libatlas-base-dev gfortran \
    libjasper-dev libgtk2.0-dev libavcodec-dev libavformat-dev \
    libswscale-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libv4l-dev && \
    apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install numpy matplotlib


# OpenCV
RUN wget https://github.com/Itseez/opencv/archive/3.2.0.zip -O opencv3.zip && \
    unzip -q opencv3.zip && mv /opencv-3.2.0 /opencv
RUN wget https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip -O opencv_contrib3.zip && \
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

CMD ["bash"]
