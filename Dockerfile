FROM ubuntu:20.04
WORKDIR /qemu

RUN apt-get install git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev git-email libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev librbd-dev librdmacm-dev libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev libvde-dev libvdeplug-dev libvte-2.90-dev libxen-dev liblzo2-dev valgrind xfslibs-dev libcapstone-dev
RUN mkdir src && cd src && git clone https://github.com/karacasoft/qemu.git && cd qemu && mkdir build  && cd build && ../configure --target-list=arm-softmmu --enable-debug && make -j2

CMD [ "entry.sh" ]