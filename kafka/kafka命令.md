# Kafka

## 安装

### 使用docker安装和部署kafka服务


## 启动
```shell
# 启动 zookeeper-server
bin/zookeeper-server-start.sh config/zookeeper.properties

# 启动bin/kafka-server
bin/kafka-server-start.sh config/server.properties
```

## 基本kafka命令

### 创建主题
`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic-name`

### 修改主题
`bin/kafka-topics.sh —zookeeper localhost:2181 --alter --topic topic_name --parti-tions count`

### 删除主题
`bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic topic_name`

### 显示主题列表
`bin/kafka-topics.sh --list --zookeeper localhost:2181`

### 启动生产者发送消息
`bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic-name`

### 启动消费者接受消息
`bin/kafka-console-consumer.sh --zookeeper localhost:2181 —topic topic-name --from-beginning --whitelist topic-name`


### Replic CAP理论