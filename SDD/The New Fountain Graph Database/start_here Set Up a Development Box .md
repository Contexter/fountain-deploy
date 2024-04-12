# start_here
To set up your Ubuntu 20.04 development environment for Swift development, particularly for projects using Vapor, Redis, and the RedisGraph module, and ensuring all are installed from source, follow this comprehensive guide. This setup will align with the checks performed by the `START_HERE.sh` script.

### Step 1: Install Essential Tools

First, install essential build tools and libraries needed for building various software from source.

```bash
sudo apt update
sudo apt install -y build-essential curl wget git zlib1g-dev \
    libssl-dev libreadline-dev libbz2-dev libsqlite3-dev libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
    libcurl4-openssl-dev clang libicu-dev pkg-config
```

### Step 2: Install Swift

Download and install Swift from the official source. This ensures you have the latest compatible version.

1. **Download the appropriate Swift version**:
   
```bash
wget https://download.swift.org/swift-5.10-release/ubuntu2004/swift-5.10-RELEASE/swift-5.10-RELEASE-ubuntu20.04.tar.gz
```

2. **Extract the downloaded file**:

```bash
tar xzf swift-5.10-RELEASE-ubuntu20.04.tar.gz
```

3. **Export the Swift binary path** (add this to your `.bashrc` or `.profile` for persistence):

```bash
export PATH=/path/to/swift-5.10-RELEASE-ubuntu20.04/usr/bin:"${PATH}"
```

### Step 3: Install Vapor Toolbox

Clone the Vapor toolbox repository and build it.

1. **Clone the repository**:

```bash
git clone https://github.com/vapor/toolbox.git
cd toolbox
```

2. **Checkout the latest stable release**:

```bash
git checkout <latest-tag>  # Replace <latest-tag> with the latest release tag
```

3. **Build the toolbox**:

```bash
swift build -c release --disable-sandbox
```

4. **Install the toolbox**:

```bash
sudo cp .build/release/vapor /usr/local/bin
```

### Step 4: Install Redis

Install Redis server from source.

1. **Clone the Redis repository**:

```bash
git clone https://github.com/redis/redis.git
cd redis
```

2. **Build Redis**:

```bash
make
```

3. **Install Redis**:

```bash
sudo make install
```

### Step 5: Install RedisGraph

Install the RedisGraph module from source.

1. **Clone the RedisGraph repository**:

```bash
git clone --recurse-submodules -j8 https://github.com/RedisGraph/RedisGraph.git
cd RedisGraph
```

2. **Build RedisGraph**:

```bash
make
```

3. **Run Redis with the RedisGraph module**:

```bash
redis-server --loadmodule ./src/redisgraph.so
```

### `START_HERE.sh` Script in Final State

Now, ensure that the `START_HERE.sh` script is configured to check all these installations. Here’s the final version of the script:

```bash
#!/bin/bash

echo "Starting environment diagnostic and setup..."
echo "Make sure to source this script to stay in the Swift-Projects directory after completion."

# Ensure the Swift-Projects directory exists and move into it
PROJECT_DIR="$HOME/Swift-Projects"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Creating Swift-Projects directory..."
    mkdir -p "$PROJECT_DIR"
fi

echo "Changing to the Swift-Projects directory..."
cd "$PROJECT_DIR"
pwd

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Swift installation
if command_exists swift; then
    echo "Swift is installed:"
    swift --version
else
    echo "Swift is NOT installed."
fi

# Check Vapor Toolbox installation
if command_exists vapor; then
    echo "Vapor Toolbox is installed:"
    vapor --version
else
    echo "Vapor Toolbox is NOT installed."
fi

# Check Redis installation
if command_exists redis-server; then
    echo "Redis is installed:"
    redis-server --version
else
    echo "Redis is NOT installed."
fi

# Check RedisGraph module
echo "Attempting to load RedisGraph module..."
REDISGRAPH_TEST=$(redis-cli GRAPH.QUERY HelloWorld "CREATE (:Test {name:'test'})" 2>&1)
if [[ "$REDISGRAPH_TEST" == *"unknown command"* ]]; then
    echo "RedisGraph module is NOT loaded in Redis."
else
    echo "RedisGraph module is loaded correctly."
fi

echo "Environment diagnostic completed."
```

### Running the Script

To

 effectively use this script, source it from your terminal:

```bash
source ~/START_HERE.sh
```

Or set an alias in your `.bashrc` or `.zshrc` file:

```bash
echo "alias start_here='source ~/START_HERE.sh'" >> ~/.bashrc
source ~/.bashrc
```

Now, you can just type `start_here` in your terminal to execute this environment setup and verification script. This will prepare your development environment, verify all critical components are installed, and navigate into the Swift-Projects directory, making your workflow seamless and efficient.