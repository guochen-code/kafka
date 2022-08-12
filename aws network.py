By default, clients can access an MSK cluster only if they're in the same VPC as the cluster. 
To connect to your MSK cluster from a client that's in the same VPC as the cluster, 
make sure the cluster's security group has an inbound rule that accepts traffic from the client's security group.

'''
have 3 brokers !!!!!!!!!!!!!!!!!!!!!!!!!!!
Use the ListNodes API or the list-nodes command in the AWS CLI to get a list of the brokers in your cluster. 
The results of this operation include the IDs of the elastic network interfaces (ENIs) that are associated with the brokers.
'''

(1) aws MSK:
  properties - networking settings - security groups applied - sg-0b0f7d9561f838f7b 
  
(2) EC2:
  security groups - sg-0b0f7d9561f838f7b - inbound rules (can contain many security groups, sg-02955b75da3b7d0fa / KafkaClient)
  
(3) EC2:
  security groups (one KafkaClient) - sg-02955b75da3b7d0fa - inbound rules - add port range 22, source 0.0.0.0/0
  
(4) EC2:
  network interfaces (3 KafkaClient) - (3 different lastic network interfaces (ENIs)) - click any of the three - action drop down menu - change security groups 
  - can find security group ID sg-02955b75da3b7d0fa
  
  


