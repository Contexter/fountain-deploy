Redis (Remote Dictionary Server) is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

Here's a foundational overview of Redis, structured as a "101" course:

### 1. Key Features of Redis

- **In-Memory Storage**: Redis stores all data in memory, which allows for extremely fast read and write operations—typically in the order of milliseconds.
  
- **Data Structures**: Unlike traditional key-value stores, Redis supports advanced data types such as lists, sets, sorted sets, and hashes, which are fundamental for solving complex problems efficiently.

- **Persistence**: Offers options for durability, including snapshotting and append-only files (AOF) that record every write operation received by the server.

- **Replication and Scalability**: Redis supports master-slave replication, allowing Redis servers to be mirrored on multiple slave nodes, which helps in scalability and data redundancy.

- **High Availability**: With Redis Sentinel, you can manage Redis nodes and automatically perform failover which is crucial for production environments.

- **Atomic Operations**: Redis operations on complex data types are atomic, meaning that you can safely perform operations like increments on a counter, append to a list, or add to a set without worrying about concurrency issues.

### 2. Basic Concepts

- **Keys**: Redis keys are binary safe, meaning you can use any binary sequence as a key, from a string like "foo" to the contents of a JPEG file.

- **Commands**: Redis commands are operations that can be performed on data types. For example, `GET` and `SET` for strings, `LPUSH` and `RPOP` for lists, `SADD` and `SMEMBERS` for sets.

- **Pub/Sub**: Redis supports Publish/Subscribe messaging paradigms where clients can subscribe to channels and publish messages that are broadcast to all subscribers of the channel.

- **Transactions**: Commands in Redis can be executed in a transactional manner using `MULTI`, `EXEC`, and `WATCH` commands, ensuring atomicity.

### 3. Data Types and Operations

- **Strings**: Most basic kind of Redis value. Redis supports strings up to 512 MB in size.
  - Example commands: `SET key value`, `GET key`, `INCR key`, `DECR key`

- **Lists**: Simple lists of strings, sorted by insertion order.
  - Example commands: `LPUSH key value`, `RPUSH key value`, `LPOP key`, `RPOP key`

- **Sets**: Unordered collections of unique strings.
  - Example commands: `SADD key value`, `SMEMBERS key`, `SISMEMBER key value`

- **Hashes**: Maps between string fields and string values.
  - Example commands: `HSET key field value`, `HGET key field`, `HGETALL key`

- **Sorted Sets**: Similar to Sets but with a value associated with each member, which dictates the order.
  - Example commands: `ZADD key score member`, `ZRANGE key start stop`

- **Streams**: A log-type data structure that provides multiple features like persistence, replication and client-side caching.
  - Example commands: `XADD key ID field string`, `XRANGE key start end`

### 4. Use Cases

- **Caching**: The most common use case for Redis is caches to reduce data fetching times.
- **Messaging Systems**: Redis pub/sub features support high-performance messaging systems.
- **Real-time Analysis**: With fast reads and writes, Redis can provide real-time analysis and monitoring.

### 5. Installing and Running Redis

You can install Redis by downloading it from the official [Redis website](https://redis.io/download) or using a package manager. Running Redis involves setting up the Redis server and connecting through a Redis client, which can be done via the command line.

### 6. Example Session

Here's a simple example to start with Redis:

```bash
redis-server # Starts the Redis server
redis-cli    # Opens the Redis command line interface
SET mykey somevalue
GET mykey
```

This will start Redis locally, set a key, and retrieve the value of the key.

Redis is a powerful tool when used for the right types of applications, particularly those needing quick read/write access to volatile data. Its simplicity in design and breadth of capabilities make it a popular choice for many developers and enterprises.