The architecture of modern web applications is increasingly moving towards microservices, a pattern that structures an application as a collection of loosely coupled services, which implement business capabilities. The microservice architecture implemented using PostgreSQL, PostgREST, and Nginx, offers a robust and scalable way to build and manage services. Here's an introductory and explanatory text about this architecture, highlighting the mapping of database tables to schemas served as OpenAPI.

---

# Introduction to Microservices Architecture with PostgreSQL, PostgREST, and Nginx

In the realm of web application development, the microservices architecture has emerged as a paradigm that prioritizes flexibility, scalability, and independence. This approach decomposes an application into a set of smaller, interconnected services instead of a single monolithic structure. Each service in a microservices architecture is designed to execute a specific business function and can be developed, deployed, and scaled independently.

## Role of PostgreSQL in Microservices

PostgreSQL, a powerful open-source object-relational database system, serves as the foundation for storing and managing data across microservices. Its advanced features, such as support for complex data types, full-text search, and extensibility, make PostgreSQL an ideal choice for microservices that require robust data persistence and transactional support. In a microservices architecture, each service can have its dedicated PostgreSQL schema, ensuring data isolation and schema independence, which simplifies the management of data persistence in a distributed system.

## PostgREST for API Layer

PostgREST is a standalone web server that turns your PostgreSQL database directly into a RESTful API. The beauty of PostgREST lies in its ability to provide an instant, high-performance API layer without the need for custom backend development. By mapping each PostgreSQL schema to a RESTful endpoint, PostgREST enables microservices to communicate over HTTP with minimal latency, leveraging PostgreSQL's security and scalability. This direct mapping ensures that the data model is accurately and efficiently exposed to other services or front-end clients, adhering to the OpenAPI specifications for clear, interactive API documentation.

## Nginx as the Reverse Proxy

Nginx, known for its high performance, reliability, and scalability, acts as the gatekeeper in this architecture. It serves as a reverse proxy, routing incoming HTTP requests to the appropriate PostgREST instance based on the request URL. Nginx efficiently manages SSL termination, load balancing, and static content delivery, making it an indispensable tool for handling web traffic in a microservices ecosystem. By integrating Nginx, developers can ensure secure, fast, and reliable access to the microservices, while also simplifying the network configuration.

## Mapping Database Tables to Schemas Served as OpenAPI

The essence of this architecture lies in its ability to map individual database tables to dedicated PostgreSQL schemas, each of which is served as an OpenAPI through PostgREST. This approach not only encapsulates the data and operations of each microservice but also promotes a clean, organized structure for API endpoints. OpenAPI specifications offer a standard, language-agnostic interface to RESTful APIs, enabling both humans and computers to discover and understand the capabilities of the service without accessing the source code.

## Conclusion

The combination of PostgreSQL, PostgREST, and Nginx in a microservices architecture provides a compelling solution for building modern, scalable web applications. This setup leverages the strengths of each component to offer a streamlined, efficient pathway from database tables to web-facing APIs, adhering to the principles of independence, scalability, and resilience. As applications grow and evolve, this architecture ensures that each microservice can be modified, scaled, or replaced independently, promoting agility and innovation in web development.

---

This text aims to introduce and explain the integration and functionalities of PostgreSQL, PostgREST, and Nginx in creating a microservices architecture that maps database tables to schemas, further served as OpenAPI, offering a comprehensive, scalable, and efficient approach to modern web application development.

# Shell Script Automation: setup_microservices.sh

This script automates the setup process for microservices, including creating schemas and tables in PostgreSQL, configuring PostgREST instances, setting up Nginx server blocks, and securing connections with SSL certificates via Certbot.
```
#!/bin/bash
echo "Fountain Microservices Setup Automation"

# Gather PostgreSQL credentials and base domain information
read -p "Enter PostgreSQL database name: " dbname
read -p "Enter PostgreSQL user: " dbuser
echo -n "Enter PostgreSQL password: "
read -s dbpass
echo
read -p "Enter base domain (e.g., benedikt-eickhoff.de): " basedomain

# Service names representing tables and corresponding schemas
services=("playwright" "metadata" "script" "act" "scene" "character" "dialogue" "action" "transition" "parenthetical" "note" "centeredtext" "pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship" "musicsound" "props" "revisionhistory" "formattingrules" "crossreferences" "extendednotesresearch" "scenelocation")

# Path to the SQL bootstrap file
sql_path="/path/to/fountain_microservices_bootstrap.sql"

# Loop to set up schemas and tables, and configure PostgREST and Nginx
for i in "${!services[@]}"; do
  schema="${services[$i]}_schema"

  # Create schema and import table structure
  PGPASSWORD=$dbpass psql -h localhost -U $dbuser -d $dbname <<EOF
CREATE SCHEMA IF NOT EXISTS $schema;
\set ON_ERROR_STOP on
\i $sql_path
EOF

  echo "Schema and tables for $schema created in $dbname."

  # PostgREST configuration
  port=$((3000 + i))
  domain="api-$((i + 1)).$basedomain"

  # PostgREST config file creation
  cat <<EOF > "/etc/postgrest/${schema}.conf"
db-uri = "postgres://$dbuser:$dbpass@localhost:5432/$dbname"
db-schema = "$schema"
db-anon-role = "web_anon"
server-port = $port
EOF

  # Nginx reverse proxy configuration
  cat <<EOF > "/etc/nginx/sites-available/$domain"
server {
    listen 80;
    server_name $domain;
    
    location / {
        proxy_pass http://localhost:$port;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF
  ln -s /etc/nginx/sites-available/$domain /etc/nginx/sites-enabled/

  # Start PostgREST for the schema
  postgrest "/etc/postgrest/${schema}.conf" &

  # Enable HTTPS with Certbot
  certbot --nginx -d $domain --non-interactive --agree-tos -m your-mail@benedikt-eickhoff.de --redirect
done

# Reload Nginx to apply the new configurations
nginx -t && systemctl reload nginx

echo "Fountain backend setup with microservices architecture completed."
```
