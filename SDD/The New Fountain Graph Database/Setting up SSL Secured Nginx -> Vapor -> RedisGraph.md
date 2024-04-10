Setting up a Vapor application with RedisGraph as the backend and securing it with SSL through Nginx as a reverse proxy involves several steps. This setup ensures that your application is scalable, secure, and production-ready. Here's a detailed guide to achieve this on an Ubuntu 20.04 server:

### Requirements

1. **Ubuntu Server 20.04** - Fresh installation.
2. **Swift** - The language used to develop Vapor apps.
3. **Vapor Framework** - Swift's web framework.
4. **Redis** - Memory store required for RedisGraph.
5. **RedisGraph** - Graph database module for Redis.
6. **Nginx** - To serve as a reverse proxy and to handle SSL/TLS.
7. **SSL Certificate** - Can use Let's Encrypt for a free certificate.

### Step 1: Install Dependencies

#### Update and Upgrade System:

```bash
sudo apt update && sudo apt upgrade -y
```

#### Install Swift:

First, install required dependencies:

```bash
sudo apt-get install clang libicu-dev libatomic1 build-essential pkg-config libssl-dev zlib1g-dev libcurl4 libpython2.7 git libbsd0 tzdata -y
```

Then, install Swift from Swift.org or use swiftenv:

```bash
wget https://swift.org/builds/swift-5.3.3-release/ubuntu2004/swift-5.3.3-RELEASE/swift-5.3.3-RELEASE-ubuntu20.04.tar.gz
tar xzf swift-5.3.3-RELEASE-ubuntu20.04.tar.gz
sudo mv swift-5.3.3-RELEASE-ubuntu20.04 /usr/share/swift
echo "export PATH=/usr/share/swift/usr/bin:$PATH" >> ~/.bashrc
source ~/.bashrc
```

#### Install Redis and RedisGraph:

```bash
sudo apt install redis-server -y
git clone --recurse-submodules -j8 https://github.com/RedisGraph/RedisGraph.git
cd RedisGraph
make
sudo cp src/redisgraph.so /usr/lib/redis/modules/
```

Modify the Redis configuration to load RedisGraph:

```bash
echo "loadmodule /usr/lib/redis/modules/redisgraph.so" | sudo tee -a /etc/redis/redis.conf
sudo systemctl restart redis-server
```

### Step 2: Setup Vapor Project

#### Create Vapor App:

```bash
vapor new MyVaporApp
cd MyVaporApp
```

Modify `Package.swift` to include Redis package:

```swift
.package(url: "https://github.com/vapor/redis.git", from: "4.0.0")
```

And add `"Redis"` to dependencies in the target:

```swift
.target(
    name: "App",
    dependencies: [
        .product(name: "Vapor", package: "vapor"),
        .product(name: "Redis", package: "redis"),
        // Add other dependencies here
    ],
    swiftSettings: [
        .unsafeFlags(["-cross-module-optimization"], .when(configuration: .release))
    ]
)
```

#### Integrate RedisGraph:

Implement functionality using Redis commands in your Vapor controllers. See [Vapor documentation](https://docs.vapor.codes/4.0/) for more details.

### Step 3: Setup Nginx as a Reverse Proxy with SSL

#### Install Nginx and Let's Encrypt:

```bash
sudo apt install nginx certbot python3-certbot-nginx -y
```

#### Configure Nginx:

Create a new configuration file for your site:

```bash
sudo nano /etc/nginx/sites-available/myvaporapp
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name example.com;  # Change to your domain

    location / {
        proxy_pass http://localhost:8080;  # Forward requests to Vapor server
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site by linking the file to the `sites-enabled` directory:

```bash
sudo ln -s /etc/nginx/sites-available/myvaporapp /etc/nginx/sites-enabled/
```

#### Secure Nginx with SSL:

Request an SSL certificate:

```bash
sudo certbot --nginx -d example.com
```

Follow the prompts to configure HTTPS. Certbot will automatically adjust the Nginx configuration to use SSL.

### Step 4: Final Steps

#### Restart Nginx:

```bash
sudo systemctl restart nginx
```

#### Run Vapor App:

Deploy your Vapor app typically using:

```bash
vapor build --release
vapor run serve --env production --hostname 

0.0.0.0 --port 8080
```

Or configure a service for systematic startup.

### Conclusion

Your Vapor application is now running with RedisGraph as its backend, secured through SSL via Nginx as a reverse proxy. This setup ensures that your application is not only secure but also benefits from the high-performance capabilities of RedisGraph and Vapor. Adjust configurations based on specific security, performance, and deployment needs.