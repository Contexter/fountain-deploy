To set up RedisGraph on an Ubuntu 20.04 system, you can follow these detailed steps, which include installing Redis, loading the RedisGraph module, and running a simple Cypher query to test the installation. 

### Step 1: Install Redis

First, you need to install Redis. Ubuntu’s default repositories contain Redis packages, so you can install them using `apt`. However, it’s a good practice to update your package index first and then install Redis:

```bash
sudo apt update
sudo apt install redis-server
```

After installation, the Redis service should start automatically. You can check the status of the Redis service with:

```bash
sudo systemctl status redis-server
```

This command will tell you if Redis is running. Configuration files for Redis are located at `/etc/redis/redis.conf`. The default configuration should be sufficient for most initial setups, including development environments.

### Step 2: Install RedisGraph

RedisGraph is not included in the default Redis installation, so you need to load it separately. You can do this by building from source:

#### Install Build Essentials and Git

If you don't have `build-essential`, `cmake`, and `git` installed, you'll need to install them:

```bash
sudo apt install build-essential cmake git
```

#### Clone the RedisGraph Repository

Clone the RedisGraph repository from GitHub:

```bash
git clone --recurse-submodules -j8 https://github.com/RedisGraph/RedisGraph.git
cd RedisGraph
```

#### Build RedisGraph Module

Now, build the RedisGraph module:

```bash
make
```

### Step 3: Run Redis with RedisGraph

After building RedisGraph, you can start Redis and load the RedisGraph module:

```bash
redis-server --loadmodule ./src/redisgraph.so
```

This command starts the Redis server and loads the RedisGraph module that you just built.

### Step 4: Test RedisGraph

To test if RedisGraph is running correctly, use the `redis-cli` command-line interface:

```bash
redis-cli
```

Once in the Redis CLI, you can create a graph and run a Cypher query:

```bash
127.0.0.1:6379> GRAPH.QUERY myGraph "CREATE (:Person {name: 'John Doe'})"
127.0.0.1:6379> GRAPH.QUERY myGraph "MATCH (n:Person) RETURN n"
```

These commands create a node labeled `Person` with a name property set to 'John Doe' and then retrieve all `Person` nodes.

### Optional: Configure Redis to Load RedisGraph on Startup

If you plan to use RedisGraph regularly, you might want to configure Redis to load the RedisGraph module automatically on startup:

1. **Open Redis Configuration File:**

```bash
sudo nano /etc/redis/redis.conf
```

2. **Add the Following Line at the End of the File:**

```bash
loadmodule /path/to/redisgraph/src/redisgraph.so
```

Replace `/path/to/redisgraph/src/redisgraph.so` with the actual path to the `redisgraph.so` file on your system.

3. **Restart Redis Service:**

```bash
sudo systemctl restart redis-server
```

This setup ensures that every time Redis starts, it will also load RedisGraph, making it ready to process graph queries.

### Conclusion

With these steps, you have successfully set up Redis and RedisGraph on Ubuntu 20.04. You can now start developing applications that leverage the speed and flexibility of Redis combined with the powerful graph processing capabilities of RedisGraph.