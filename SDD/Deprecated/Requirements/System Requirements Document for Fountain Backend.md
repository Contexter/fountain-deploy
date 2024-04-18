# System Requirements Document for Fountain Backend

## Introduction

This document outlines the system requirements for the Fountain Backend, designed to manage and query relational data within a PostgreSQL database, leveraging the capabilities of postgREST for an efficient and sophisticated microservices architecture. The system is developed to run on Ubuntu 20.04 machines, optimized for both development and production environments.

## Simplest Development Setup

### Minimum Requirements

- **Operating System**: Ubuntu 20.04 LTS
- **CPU**: 1 vCPU
- **RAM**: 2 GB
- **Storage**: 20 GB SSD

This configuration is suitable for initial development and testing, allowing developers to run the Fountain Backend with a lightweight setup. It supports basic database operations, development of microservices managed by postgREST schemata, and local testing.

## Development Setup

As the project evolves from a simple development setup to a more robust development environment, system requirements will adjust to accommodate increased load, complexity, and the need for more intensive testing.

### Recommended Requirements

- **Operating System**: Ubuntu 20.04 LTS
- **CPU**: 2 vCPUs
- **RAM**: 4 GB
- **Storage**: 40 GB SSD

This setup is recommended for developers working on more complex functionalities, involving advanced database operations and higher concurrency needs. It provides a more realistic environment for testing the backend's performance under conditions more closely resembling production.

## Production Environment

Moving from development to a production environment necessitates a significant upgrade in system specifications to ensure reliability, performance, and scalability.

### System Requirements

- **Operating System**: Ubuntu 20.04 LTS
- **CPU**: 4 vCPUs (minimum)
- **RAM**: 16 GB (minimum)
- **Storage**: 160 GB SSD (minimum)

Additional considerations for the production environment include:

- **Load Balancing**: To distribute incoming traffic efficiently across multiple instances.
- **Redundancy and High Availability**: Essential for minimizing downtime and data loss.
- **Security Measures**: Including firewalls, encryption, and regular security updates.
- **Backup and Recovery Solutions**: To protect against data loss and ensure quick recovery in case of failure.

## Conclusion

This document provides a structured approach to scaling the Fountain Backend from a simple development setup to a full-fledged production environment. By adhering to these system requirements, the backend infrastructure can be optimized for performance, security, and scalability, supporting the sophisticated management and querying of relational data as envisioned.