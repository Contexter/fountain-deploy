Managing system user rights in relation to PostgreSQL roles on Ubuntu 20.04 involves understanding the interaction between the operating system's user accounts and PostgreSQL's role-based access control. By default, PostgreSQL uses "peer" authentication for local connections, meaning it matches the connecting system user name with a PostgreSQL role of the same name for authentication. This tutorial will guide you through managing system user rights in relation to PostgreSQL roles, including necessary commands, examples, and editing PostgreSQL's configuration to utilize the default "peer" authentication method.

### Understanding "peer" Authentication

The "peer" authentication method is used by PostgreSQL to authenticate local connections. It relies on the operating system's user identity to authenticate a user to a PostgreSQL role. For this method to work, you must have a corresponding PostgreSQL role for each system user that needs database access.

### Installing PostgreSQL

First, ensure that PostgreSQL is installed on your Ubuntu 20.04 system:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### Configuring PostgreSQL for "peer" Authentication

The default configuration for local connections already uses "peer" authentication. You can verify this in the `pg_hba.conf` file:

1. Open the PostgreSQL Client Authentication Configuration File:

```bash
sudo nano /etc/postgresql/12/main/pg_hba.conf
```

2. Look for lines similar to:

```
# "local" is for Unix domain socket connections only
local   all             all                                     peer
```

This line configures PostgreSQL to use "peer" authentication for all local connections.

### Creating System Users and Corresponding PostgreSQL Roles

To demonstrate "peer" authentication, let's create a system user and a corresponding PostgreSQL role.

1. Create a new system user (replace `exampleuser` with your desired username):

```bash
sudo adduser exampleuser
```

2. Switch to the `postgres` user:

```bash
sudo -i -u postgres
```

3. Create a PostgreSQL role with the same name as the system user:

```bash
createuser --interactive
```

When prompted, enter the name of the new role (`exampleuser`) and whether it should have superuser permissions.

4. Optionally, you can also create a database owned by the new role:

```bash
createdb exampledb -O exampleuser
```

### Testing "peer" Authentication

1. Switch to the new system user:

```bash
su - exampleuser
```

2. Connect to PostgreSQL as the new role. Since the database name is the same as the username, you can simply use:

```bash
psql
```

You should be logged into the PostgreSQL console.

### Example: Granting Role Permissions

Within PostgreSQL, you can grant specific permissions to the role. For instance, to grant `SELECT` permissions on all tables in the `exampledb` database to `exampleuser`, use:

1. Connect to PostgreSQL as the `postgres` user:

```bash
sudo -i -u postgres psql
```

2. Grant permissions:

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA public TO exampleuser;
```

### Comments

- The "peer" authentication method is convenient for systems where database roles closely map to system user accounts.
- For production environments, consider more secure authentication methods like "md5" or "scram-sha-256" for network connections.
- Always ensure your `pg_hba.conf` file is correctly configured to prevent unauthorized access.

### Conclusion

This tutorial covered the basics of managing system user rights in relation to PostgreSQL roles on Ubuntu 20.04, focusing on the default "peer" authentication setting. By following these instructions, you can create system users and corresponding PostgreSQL roles, allowing for secure local connections to your databases.