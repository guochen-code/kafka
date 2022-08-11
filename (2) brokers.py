a kafka cluster is composed of multiple brokers (servers)

Every kafka broker is called a "bootstrap server"

that means you only need to connect to one broker, and the kafka client will automatically know how to connect to the entire cluster (smart clients)

each broker knows all the brokers, topics and partitions. (metadata)

