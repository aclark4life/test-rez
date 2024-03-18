name = "hello_world_package"
version = "1.0"

variants = [["platform-linux", "arch-x86_64", "os-centos-7"]]
requires = []

def commands():
    env.PATH.append("{root}/bin")
    env.HELLO_WORLD_MESSAGE.set("Hello, world!")
