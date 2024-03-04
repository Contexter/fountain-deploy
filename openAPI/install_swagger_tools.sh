#!/bin/bash

# Ensure running from the openAPI directory
cd "$(dirname "$0")"

# Update and install necessary packages
echo "Updating package lists..."
sudo apt-get update

echo "Installing jq..."
sudo apt-get install -y jq

echo "Installing Node.js and npm..."
# Using NodeSource's binary distributions for a more recent version of Node.js
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node -v
npm -v

echo "Installing Swagger tools..."
# Install swagger-cli for OpenAPI operations
sudo npm install -g swagger-cli

# Install swagger-diff for comparing OpenAPI specs
sudo npm install -g swagger-diff

echo "All tools installed successfully."
