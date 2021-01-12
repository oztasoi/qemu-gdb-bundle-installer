export MAC_LINK="https://developer.arm.com/-/media/Files/downloads/gnu-rm/10-2020q4/gcc-arm-none-eabi-10-2020-q4-major-mac.tar.bz2?revision=48a4e09a-eb5a-4eb8-8b11-d65d7e6370ff&la=en&hash=8AACA5F787C5360D2C3C50647C52D44BCDA1F73F"
export LINUX_X86_LINK="https://developer.arm.com/-/media/Files/downloads/gnu-rm/10-2020q4/gcc-arm-none-eabi-10-2020-q4-major-x86_64-linux.tar.bz2?revision=ca0cbf9c-9de2-491c-ac48-898b5bbc0443&la=en&hash=68760A8AE66026BCF99F05AC017A6A50C6FD832A"
export TAR_DIRECTORY="~/Downloads/arm-toolchain.tar.bz2"

if [ -d $(pwd)/gcc-arm-none-eabi-10-2020-q4-major ]; then
    echo "ARM-GDB is already installed. Skipping download & installation..." && echo "Starting ARM-GDB..." && $(pwd)/gcc-arm-none-eabi-10-2020-q4-major/bin/arm-none-eabi-gdb
elif [ -f "$TAR_DIRECTORY" ]; then
    echo "ARM-GDB is already downloaded. Starting extraction..." && tar -xjvf ~/Downloads/arm-toolchain.tar.bz2 --directory $(pwd) && echo "Finished extraction." && sleep 1 && echo "Clearing stdout..." && sleep 1 && clear
else
    if [ $(uname -s) == "Darwin" ]; then
        echo "Download is starting..." && wget -O $TAR_DIRECTORY $MAC_LINK && echo "Download completed." && echo "Starting extraction..." && tar -xjvf ~/Downloads/arm-toolchain.tar.bz2 --directory $(pwd) && echo "Finished extraction." && sleep 1 && echo "Clearing stdout..." && sleep 1 && clear && echo "Starting ARM-GDB..." && $(pwd)/gcc-arm-none-eabi-10-2020-q4-major/bin/arm-none-eabi-gdb
    fi

    if [ $(uname -s) == "Linux" ]; then
        echo "Download is starting..." && wget -O $TAR_DIRECTORY $LINUX_X86_LINK && echo "Download completed." && echo "Starting extraction..." && tar -xjvf ~/Downloads/arm-toolchain.tar.bz2 --directory $(pwd) && echo "Finished extraction." && sleep 1 && echo "Clearing stdout..." && sleep 1 && clear && echo "Starting ARM-GDB..." && $(pwd)/gcc-arm-none-eabi-10-2020-q4-major/bin/arm-none-eabi-gdb
    fi
fi
