kalman:
	gcc -c -fPIC c_src/kalman.c -o c_src/kalman.o
	gcc -shared -Wl,-soname,libkalman.so -o c_src/libkalman.so c_src/kalman.o

