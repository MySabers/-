# clickhouse
## 安装
### yum源安装
1. `yum install yum-utils`
2. `sudo rpm --import https://repo.clickhouse.tech/CLICKHOUSE-KEY.GPG` 可以换为本地文件路径
3. `yum-config-manager --add-repo https://repo.clickhouse.tech/rpm/stable/x86_64` 
4. `yum install clickhouse-server clickhouse-client`

### docker方式安装
1. `docker run -d --name ch-server --ulimit nofile=262144:262144 -p 8123:8123 -p 9000:9000 -p 9009:9009 yandex/clickhouse-server`

## 启动
### yum方式安装的启动

1. 以守护进程的方式启动: `service clickhouse-server start`
2. 前台启动: `clickhouse-server --config-file=/etc/clickhouse-server/config.xml`


## 配置密码
1. `PASSWORD=$(base64 < /dev/urandom | head -c8); echo "你的密码"; echo -n "你的密码" | sha256sum | tr -d '-'`, <br> 打完这条命令会出现以下两条结果
    ```
    A940922h
    dd2cef99d7122cd3e2455491f79b567400ce238b7eca309f73e089670df70eb6 
    ```
    第一行为密码铭文,第二行为密码密文

2. 之后 `vim user.xml`,将55行的 替换为 `<password_sha256_hex> 密码密文 </password_sha256_hex>`


## 连接
1. `clickhouse-client --host=example.com`,` --host=example.com` 可以省略
2. `clickhouse-client -h 127.0.0.1 -d default -m -u default --password '你的密码'`