import os

hello_world_message = os.environ.get('HELLO_WORLD_MESSAGE', 'Default Message')
print(hello_world_message)
