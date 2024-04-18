```
Testing database connection for play...
psql: error: FATAL:  Peer authentication failed for user "play"
Database connection FAILED.
```

The error message "FATAL: Peer authentication failed for user 'play'" typically indicates an issue with the PostgreSQL authentication method configured for the user attempting to connect to the database. This error often occurs when using local connections on Unix domain sockets (the default method for local connections in PostgreSQL) and the `pg_hba.conf` file is configured to use `peer` authentication for these connections.

Here's how to address this issue:

### Understanding `peer` Authentication
- The `peer` authentication method works by obtaining the client's OS username and using it to authenticate the database connection. If the OS username matches the requested PostgreSQL username, the connection is allowed.
- In your case, the OS user running the `psql` command might not match the PostgreSQL username "play", or the `peer` authentication configuration does not include this user correctly.

### Solutions

#### 1. Use `psql` with the Correct OS User
If possible, you can try connecting to the database using the `psql` command while logged in as the "play" user in your operating system, assuming such a user exists and matches the PostgreSQL username.

```bash
sudo -u play psql -d your_db_name
```

#### 2. Change Authentication Method in `pg_hba.conf`
1. Locate the `pg_hba.conf` file, usually found in the PostgreSQL data directory (e.g., `/etc/postgresql/12/main/pg_hba.conf` or `/var/lib/postgres/data/pg_hba.conf`, depending on the installation).
2. Open `pg_hba.conf` in a text editor (with root or the corresponding privileges).
3. Find the line(s) related to local connections for the "play" database or all databases and change the method from `peer` to `md5` or another method like `password` if plaintext password authentication is acceptable. For example:
   ```plaintext
   # TYPE  DATABASE        USER            ADDRESS                 METHOD
   local   all             play                                    md5
   ```
4. Save the changes and exit the editor.
5. Restart the PostgreSQL server to apply the changes. The command might vary depending on your system; for many systems, it's:
   ```bash
   sudo systemctl restart postgresql
   ```
6. Try connecting again with `psql`.

#### 3. Create a Matching OS User (If Applicable)
If you want to keep using `peer` authentication and the PostgreSQL username "play" does not match any OS user, you can create a matching OS user:
```bash
sudo adduser play
```
Then, try connecting to the database again using this OS user.

### Note
Be cautious when changing authentication methods and ensure that the changes do not inadvertently weaken the security of your PostgreSQL server. Always back up configuration files like `pg_hba.conf` before making changes.

Adjusting the `pg_hba.conf` file's authentication methods should resolve the issue, allowing you to connect to the database successfully.