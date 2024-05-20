import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

with open(r'D:\NCKU_MDL\NCKU_MDL_AD_API_TEST\NCKU_MDL_AD\database\sqlconfig.yaml', 'r') as file:
    yaml_datas = yaml.safe_load(file)
  
# 数据库连接配置
SQLALCHEMY_DATABASE_URI = (
    f"""mysql+pymysql://{yaml_datas['mysql_dev']['user']}:{yaml_datas['mysql_dev']['password']}@{yaml_datas['mysql_dev']['host']}/{yaml_datas['mysql_dev']['db']}?charset=utf8mb4"""
)

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 声明基类
Base = declarative_base()
