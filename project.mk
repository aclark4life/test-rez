install:
	/opt/rez/bin/rez/rez build --install
	/opt/rez/bin/rez/rez env hello_world_package -- python hello.py
