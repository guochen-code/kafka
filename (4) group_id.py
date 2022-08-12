kafka-console-consumer:
  use a random group id



 override the group.id for kafka-console-consumer using:
    
    --group mygroupid
    
    
I perform operations on the consumer offsets using:
  kafka-consumer-groups NOT kafka-console-consumer
