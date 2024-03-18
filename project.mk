install:
	cd hello_world_package; /opt/rez/bin/rez/rez build --install

serve:
	/opt/rez/bin/rez/rez env hello_world_package -- python hello.py
