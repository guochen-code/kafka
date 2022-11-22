(1) download kafka
(2) create data folder, where create two folers called broker and zookeeper
(3) change path for zookeeper and server in config foler:
    dataDir=C:/Users/xx/Downloads/kafka_2.11-1.1.0/data/zookeeper
    log.dirs=C:/Users/xx/Downloads/kafka_2.11-1.1.0/data/broker
(4) start zookeeper: zookeeper-server-start.bat ..\..\config\zookeeper.properties (inside the bin/windows start cmd)
(5) start kafka: kafka-server-start.bat ..\..\config\server.properties (inside the bin/windows start cmd)
(6) create topic: kafka-topics.bat --zookeeper:2181 -topic sample --create --partitions 1 --replication-factor 1 (inside the bin/windows start cmd)
(7) check created topic: kafka-topics --list --zookeeper localhost:2181 (inside the bin/windows start cmd)
(8) create a consumer: kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic sample --from-beginning (inside the bin/windows start cmd)
(9) create a producer: kafka-console-producer.bat --broker-list localhost:9092 --topic sample (inside the bin/windows start cmd)
        
install java8
(1) download and install
(2) edit the system environment variables: environment variable:
        (1) under system variables: Path: create new: C:\Program Files\Java\jre1.8.0_341\bin
        (2) under system variables: new:create JAVA_HOME:C:\Program Files\Java\jre1.8.0_341

                        
java 8 download: https://www.oracle.com/ca-en/java/technologies/downloads/#java8-windows
kafka download: https://kafka.apache.org/downloads
