docker pull 0xyg3n/cmpe443qemuimage:v1.0

FNAME=$(echo "$(cd $(dirname prog.elf); pwd -P)/$(basename prog.elf)")
docker run -p 1234:1234 -p 6942:6942 -v  $FNAME:/test.axf -it 0xyg3n/cmpe443qemuimage:v1.0 /usr/local/bin/qemu-system-arm -machine LPC4088 -kernel /test.axf -nographic -s -S
