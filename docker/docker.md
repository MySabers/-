# docker技术
## 一、镜像不熟命令记录
1. 查看镜像详细信息  : `docker image inspect imageName`   
2. 查看所有的镜像ID  : `docker image ls -q` 
3. 镜像导出 : `docker image save nginx > /root/nginx.tar`
4. 镜像导入 : `docker image load -i /root/nginx.tar`
5. 删除所有镜像: ``docker image rm -f `docker image ls -q` ``

## 二、容器不熟命令记录
1. docker容器启动后, 退出删除, 常用于测试 : `docker container run -it --name="test" --rm  imageName `
2. 连接容器（不常用，会改变原有进程） : `docker container attach containerName`
3. 连接容器（常用，会开一个新进程，常用于调试）: `docker container exec -it containerName /bin/bash`
4. 显示所有容器的不截断信息 : `docker container ls -a --no-trunc`
5. 显示docker容器内的进程信息 : `docker container top containerId`
6. 查看容器内的日志 : `docker container logs containerName`，参数 `-ft` 为实时显示日志, `docker logs -f -t  --tail=10 ptdlog-convert`  显示最后多少条日志
7. 基于容器做镜像 : `docker commit containerName newImagename:v1`
8. 通过指定`--restart=always`来指定重启 : `docker container run --restart="always --name="demo"  -d imageName`

## 三、docker数据卷
1. 主机文件拷贝到docker容器内 : `docker container cp index.html containerName:/root/html/`
2. 容器内文件拷贝到主机 : `docker container cp containerName:/root/html/index.html ./`
3. 挂载数据卷 : `docker image run --name="ceshi" -d -v /root/host:/root/docker nginx`
4. 数据卷容器 <br>
    作用:在集群化的管理当中，大批量容器都需要挂载多个相同的数据卷时，可以采用数据卷容器进行统一管理。  
    (1). 创建数据卷 : `docker image run -d --name="volumes_name" -v /root/volume:/root/volume imageName`  
    (2). 挂载数据卷 : `docker image run -d --name="ceshi" --volumes-from volumes_name  imageName`


## 四、dockerfile
### dickerfile未见内容
```dockerfile
# 定义基础镜像
FROM node
# 执行命令
RUN git clone -q https://github.com/docker-in-practice/todo.git
# 移动到新的克隆目录
WORKDIR todo
# 定义变量
ENV html=/var/www/html/
# 通过 ${}进行使用
COPY /html ${html}
# 运行命令
RUN npm install > /dev/null
# 宿主机文件拷贝到容器内，如果拷贝的是目录，就只拷贝目录下的文件
COPY index.html /var/www/html/
# 指定构建的容器需要监听的端口
EXPOSE 8000
# add命令如果传的压缩文件，是tar类型的，如aa.tar, a.tar.gz,自动解压,支持源为URL，但是即使为tar也不会解压
ADD a.tar /var/www/html/
# 指定启动容器需要执行的命令
# 这个方式执行的命令在运行镜像的时候可以被替换掉
# CMD ["npm","start"]

# 这个不会被替换掉
ENTRYPOINT ["npm","start"]
```
### 通过dockerfile生成镜像
`docker build -t imageName -f dockerfileName .`
`--no-cache` 参数代表完全重新构建不适用缓存

# 五、docker网络(学的不好)
1. 查看只是网络类型,用于docker和宿主机之间的通信 : `docker network ls`
```
[root@bogon docker2]# docker network ls
NETWORK ID          NAME                    DRIVER              SCOPE
580eaccd739e        bridge                  bridge              local
fd41ca63b6b9        docker-compose_sc-net   bridge              local
509c59ba7a67        host                    host                local
64377e89b452        none 

`bridge` : 相当于NAT模式，会建立一个docker0的桥，通过桥进行网络访问  
`none` : 无网络模式  
`host` : 公共宿主机Network NameSpace，和宿主机共用网络资源, 文件和命令是隔离的(不怎么用)  
`container` : 与其他容器公用 Network NameSpace
```
2. 跨主机之间的docker网络互联，通过`macvlan`<br>
(1) 创建通道 : `docker network create --driver macvlan --subnet=10.0.0.0/24 --gateway=10.0.0.254 -o parent=eth0 macvlan_1`  
(2) 指定网络类型的例子 : `docker run --name=demo --network=macvlan_1 -it centos:6.8 /bin/bash`
3. 跨主机的docker网络互联，通过`overlay`实现


## 六、docker本地仓库
1. 拉去本地仓库镜像 : `docker run -d -p 5000:5000 --restart=always --name registry -v /opt/registry:/var/lib/registry registry`
2. 修改配置文件 : `"insecure-registries" : ["10.255.175.198:5000"`
3. 推上去的镜像需要满足固定的格式 `ip:prot/projectName/imageName:version` , 如 `10.255.175.198:5000/jiju/redis:v1`
4. 更改镜像名 : `docker tag redis:alpine 10.255.175.198:5000/jiju/redis:v1`
5. 上传进项至私有仓库 : `docker push 10.255.175.198:5000/jiju/redis:v1`
6. 拉取镜像 : `docker pull 10.255.175.198:5000/jiju/redis:v1`
7. docker仓库体提交添加用户名和密码<br>
(1) 下载httpd-tools工具 : `yum install httpd-tools -y`  
(2) 生成密钥目录: `mkdir /opt/registry-auth/ -p`  
(3) 生成用户名和密码 : `htpasswd -Bbn jiju 123 > /opt/registry-auth/htpasswd`  
(4) 重新生成容器 : `docker run -d -p 5000:5000 -v  /opt/registry-auth/:/auth/ -v /opt/registry:/var/lib/registry --name register-auth -e "REGISTRY_AUTH=htpasswd" -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" registry`
(5) 进行登录 : `docker login 10.255.175.198:5000`
(6) 上传镜像 : `docker push 10.255.175.198:5000/jiju/redis:v1`



## 附记
### 1. docker出错或者命令执行失败用于调试的命令  
`socat -v UNIX-LISTEN:/tmp/dockerapi.sock UNIX-CONNECT:/var/run/docker.sock &`  
> `socat` 能够在几乎任意数据类型的数据通道之间中继数据，相当于加强版的 `necat`  
`-v` : 用于提高程序可读性  
`UNIX-LISTEN` : 是让socat在一个UNIX套接字上进行监听  
`UNIX-CONNECT` : 是让socat连接盗docker的Unix套接字  
`&` : 后台运行

理论上对工作中的任意网络服务都可以使用此命令 `socat`