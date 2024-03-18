install:
	rez build --install
	rez env hello_world_package -- python hello.py
