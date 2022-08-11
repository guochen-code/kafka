# Producers are the ones who choose where the message is going to end up/which partition, thanks to the key byte.

# key hashing is the process of determining the mapping of a key to a partition.

# in the default kafka partition, the keys are hashed using the murmur2 algorithm:
  target partition = Math.abs(Utils.murmur2(keyBytes)))%(numPartition-1)
  
  
