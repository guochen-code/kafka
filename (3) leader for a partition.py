at any time only one broker can be a leader for a given partition

producers can only send data to the broker that is leader of a partition

the other brokers will replicate the data

therefore, each broker has one leader and multiple ISR (in-sybc replica)

kafka consumers by default will read data from the leader broker for a parition.

************************** kafka onsumers replica fetching (kafka v2.4+) **************************
since kafka 2.4, it allows to configure consumers to read data from the closet replica

this may help to improve latency

