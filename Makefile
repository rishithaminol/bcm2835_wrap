LIB_DIR = libbcm2835

default: bcm2835_wrap

bcm2835_wrap: setup.py bcm2835_wrap.pyx $(LIB_DIR)/libbcm2835.a
	python3 setup.py build_ext --inplace
	rm -rf bcm2835_wrap.c build

$(LIB_DIR)/libbcm2835.a:
	make -C $(LIB_DIR) libbcm2835.a

clean:
	rm -rf *.o *.so bcm2835_wrap.c build
	make -C libbcm2835 clean
