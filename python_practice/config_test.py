import os
from configparser import ConfigParser

config = ConfigParser()
config_file_path = os.path.dirname(os.path.realpath(__file__)) + "/../config/test_cfg"
print(config_file_path)
config_file_path  # config.read(config_file_path)

# 获取所用的section节点
print(config.sections())
