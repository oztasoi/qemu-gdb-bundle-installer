docker pull 0xyg3n/cmpe443qemuimage:v1.0
docker run -p 1234:1234 -p 6942:6942 -v $(pwd)/$1:/$1 -it 0xyg3n/cmpe443qemuimage:v1.0 /usr/local/bin/qemu-system-arm -machine LPC4088 -kernel /$1 -nographic -s -S
