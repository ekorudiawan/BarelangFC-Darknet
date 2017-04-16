make clean
make
./darknet detector demo cfg/coco.data cfg/cpuNet6.cfg cpuNet6_15000.weights -thresh 0.7
