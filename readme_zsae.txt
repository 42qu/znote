
ZSAE

如何运行

1. 安装sae-python-dev-guide:

下载代码:
git clone http://github.com/SAEPython/saepythondevguide.git

安装:
cd dev_server
python ./setup.py install

2. 执行

开启本地 mysql 服务，执行
create database app_zsae;

dev_server.py --mysql=user:pw@localhost:3306

