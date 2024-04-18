# running troubleshoot_this_setup.sh 
```
#!/bin/bash

# Ask for PostgreSQL credentials and database name interactively
read -p "Enter PostgreSQL database name: " DB_NAME
read -p "Enter PostgreSQL user: " DB_USER
echo -n "Enter PostgreSQL password: " && read -s DB_PASSWORD && echo
read -p "Enter base domain (e.g., example.com): " BASEDOMAIN
echo -n "Enter your email for SSL certificates: " && read EMAIL

# Array of services from the setup script
services=("playwright" "metadata" "script" "act" "scene" "character"
"dialogue" "action" "transition" "parenthetical" "note" "centeredtext"
"pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship"
"musicsound" "props" "revisionhistory" "formattingrules" "crossreferences"
"extendednotesresearch" "scenelocation")

# Check PostgreSQL service status
echo "Checking PostgreSQL service status..."
sudo systemctl is-active --quiet postgresql && echo "PostgreSQL service is active." || echo "PostgreSQL service is NOT active."

# Loop through services to check PostgREST service status
for schema in "${services[@]}"; do
    echo "Checking PostgREST service for $schema..."
    sudo systemctl is-active --quiet postgrest-$schema.service && echo "PostgREST $schema service is active." || echo "PostgREST $schema service is NOT active."
done

# Validate Nginx configuration
echo "Validating Nginx configuration..."
sudo nginx -t && echo "Nginx configuration is valid." || echo "Nginx configuration is NOT valid."

# Check SSL certificates for each domain
echo "Checking SSL certificates..."
for schema in "${services[@]}"; do
    domain="api-$schema.$BASEDOMAIN"
    echo "Checking SSL certificate for $domain..."
    sudo certbot certificates -d $domain
done

# Test database connection
echo "Testing database connection for $DB_USER..."
PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -d $DB_NAME -c '\conninfo' && echo "Database connection successful." || echo "Database connection FAILED."

# Check GoAccess dashboard accessibility
GOACCESS_DOMAIN="logs.$BASEDOMAIN"
echo "Verifying GoAccess dashboard accessibility at https://$GOACCESS_DOMAIN..."
if curl -s --head  --request GET https://$GOACCESS_DOMAIN | grep "200 OK" > /dev/null; then
    echo "GoAccess dashboard is accessible."
else
    echo "GoAccess dashboard is NOT accessible."
fi

echo "Verification completed."
```
resulting in

```
sudo ./troubleshoot_this_setup.sh
Enter PostgreSQL database name: fountain
Enter PostgreSQL user: play
Enter PostgreSQL password: 
Enter base domain (e.g., example.com): fountain.coach
Enter your email for SSL certificates: mail@benedikt-eickhoff.de
Checking PostgreSQL service status...
PostgreSQL service is active.
Checking PostgREST service for playwright...
PostgREST playwright service is NOT active.
Checking PostgREST service for metadata...
PostgREST metadata service is NOT active.
Checking PostgREST service for script...
PostgREST script service is NOT active.
Checking PostgREST service for act...
PostgREST act service is NOT active.
Checking PostgREST service for scene...
PostgREST scene service is NOT active.
Checking PostgREST service for character...
PostgREST character service is NOT active.
Checking PostgREST service for dialogue...
PostgREST dialogue service is NOT active.
Checking PostgREST service for action...
PostgREST action service is NOT active.
Checking PostgREST service for transition...
PostgREST transition service is NOT active.
Checking PostgREST service for parenthetical...
PostgREST parenthetical service is NOT active.
Checking PostgREST service for note...
PostgREST note service is NOT active.
Checking PostgREST service for centeredtext...
PostgREST centeredtext service is NOT active.
Checking PostgREST service for pagebreak...
PostgREST pagebreak service is NOT active.
Checking PostgREST service for sectionheading...
PostgREST sectionheading service is NOT active.
Checking PostgREST service for titlepage...
PostgREST titlepage service is NOT active.
Checking PostgREST service for casting...
PostgREST casting service is NOT active.
Checking PostgREST service for characterrelationship...
PostgREST characterrelationship service is NOT active.
Checking PostgREST service for musicsound...
PostgREST musicsound service is NOT active.
Checking PostgREST service for props...
PostgREST props service is NOT active.
Checking PostgREST service for revisionhistory...
PostgREST revisionhistory service is NOT active.
Checking PostgREST service for formattingrules...
PostgREST formattingrules service is NOT active.
Checking PostgREST service for crossreferences...
PostgREST crossreferences service is NOT active.
Checking PostgREST service for extendednotesresearch...
PostgREST extendednotesresearch service is NOT active.
Checking PostgREST service for scenelocation...
PostgREST scenelocation service is NOT active.
Validating Nginx configuration...
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
Nginx configuration is valid.
Checking SSL certificates...
Checking SSL certificate for api-playwright.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:















  Certificate Name: api-playwright.fountain.coach
    Domains: api-playwright.fountain.coach
    Expiry Date: 2024-05-28 05:31:39+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-playwright.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-playwright.fountain.coach/privkey.pem








- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-metadata.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:










  Certificate Name: api-metadata.fountain.coach
    Domains: api-metadata.fountain.coach
    Expiry Date: 2024-05-28 05:31:55+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-metadata.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-metadata.fountain.coach/privkey.pem













- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-script.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:




















  Certificate Name: api-script.fountain.coach
    Domains: api-script.fountain.coach
    Expiry Date: 2024-05-28 05:32:07+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-script.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-script.fountain.coach/privkey.pem



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-act.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:
  Certificate Name: api-act.fountain.coach
    Domains: api-act.fountain.coach
    Expiry Date: 2024-05-28 05:32:19+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-act.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-act.fountain.coach/privkey.pem























- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-scene.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:


















  Certificate Name: api-scene.fountain.coach
    Domains: api-scene.fountain.coach
    Expiry Date: 2024-05-28 05:32:32+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-scene.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-scene.fountain.coach/privkey.pem





- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-character.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:




  Certificate Name: api-character.fountain.coach
    Domains: api-character.fountain.coach
    Expiry Date: 2024-05-28 05:32:44+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-character.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-character.fountain.coach/privkey.pem



















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-dialogue.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:







  Certificate Name: api-dialogue.fountain.coach
    Domains: api-dialogue.fountain.coach
    Expiry Date: 2024-05-28 05:32:57+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-dialogue.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-dialogue.fountain.coach/privkey.pem
















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-action.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:

  Certificate Name: api-action.fountain.coach
    Domains: api-action.fountain.coach
    Expiry Date: 2024-05-28 05:33:09+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-action.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-action.fountain.coach/privkey.pem






















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-transition.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:























  Certificate Name: api-transition.fountain.coach
    Domains: api-transition.fountain.coach
    Expiry Date: 2024-05-28 05:33:25+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-transition.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-transition.fountain.coach/privkey.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-parenthetical.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:














  Certificate Name: api-parenthetical.fountain.coach
    Domains: api-parenthetical.fountain.coach
    Expiry Date: 2024-05-28 05:33:38+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-parenthetical.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-parenthetical.fountain.coach/privkey.pem









- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-note.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:












  Certificate Name: api-note.fountain.coach
    Domains: api-note.fountain.coach
    Expiry Date: 2024-05-28 05:33:51+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-note.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-note.fountain.coach/privkey.pem











- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-centeredtext.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:



  Certificate Name: api-centeredtext.fountain.coach
    Domains: api-centeredtext.fountain.coach
    Expiry Date: 2024-05-28 05:34:03+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-centeredtext.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-centeredtext.fountain.coach/privkey.pem




















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-pagebreak.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:













  Certificate Name: api-pagebreak.fountain.coach
    Domains: api-pagebreak.fountain.coach
    Expiry Date: 2024-05-28 05:34:16+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-pagebreak.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-pagebreak.fountain.coach/privkey.pem










- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-sectionheading.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:





















  Certificate Name: api-sectionheading.fountain.coach
    Domains: api-sectionheading.fountain.coach
    Expiry Date: 2024-05-28 05:34:29+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-sectionheading.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-sectionheading.fountain.coach/privkey.pem


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-titlepage.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:






















  Certificate Name: api-titlepage.fountain.coach
    Domains: api-titlepage.fountain.coach
    Expiry Date: 2024-05-28 05:34:41+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-titlepage.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-titlepage.fountain.coach/privkey.pem

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-casting.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:


  Certificate Name: api-casting.fountain.coach
    Domains: api-casting.fountain.coach
    Expiry Date: 2024-05-28 05:34:58+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-casting.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-casting.fountain.coach/privkey.pem





















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-characterrelationship.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:





  Certificate Name: api-characterrelationship.fountain.coach
    Domains: api-characterrelationship.fountain.coach
    Expiry Date: 2024-05-28 05:35:11+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-characterrelationship.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-characterrelationship.fountain.coach/privkey.pem


















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-musicsound.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:











  Certificate Name: api-musicsound.fountain.coach
    Domains: api-musicsound.fountain.coach
    Expiry Date: 2024-05-28 05:35:24+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-musicsound.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-musicsound.fountain.coach/privkey.pem












- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-props.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:
















  Certificate Name: api-props.fountain.coach
    Domains: api-props.fountain.coach
    Expiry Date: 2024-05-28 05:35:34+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-props.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-props.fountain.coach/privkey.pem







- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-revisionhistory.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:

















  Certificate Name: api-revisionhistory.fountain.coach
    Domains: api-revisionhistory.fountain.coach
    Expiry Date: 2024-05-28 05:35:46+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-revisionhistory.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-revisionhistory.fountain.coach/privkey.pem






- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-formattingrules.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:









  Certificate Name: api-formattingrules.fountain.coach
    Domains: api-formattingrules.fountain.coach
    Expiry Date: 2024-05-28 05:35:59+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-formattingrules.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-formattingrules.fountain.coach/privkey.pem














- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-crossreferences.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:






  Certificate Name: api-crossreferences.fountain.coach
    Domains: api-crossreferences.fountain.coach
    Expiry Date: 2024-05-28 05:36:12+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-crossreferences.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-crossreferences.fountain.coach/privkey.pem

















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-extendednotesresearch.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:








  Certificate Name: api-extendednotesresearch.fountain.coach
    Domains: api-extendednotesresearch.fountain.coach
    Expiry Date: 2024-05-28 05:36:24+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-extendednotesresearch.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-extendednotesresearch.fountain.coach/privkey.pem















- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Checking SSL certificate for api-scenelocation.fountain.coach...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Found the following matching certs:



















  Certificate Name: api-scenelocation.fountain.coach
    Domains: api-scenelocation.fountain.coach
    Expiry Date: 2024-05-28 05:36:41+00:00 (VALID: 89 days)
    Certificate Path: /etc/letsencrypt/live/api-scenelocation.fountain.coach/fullchain.pem
    Private Key Path: /etc/letsencrypt/live/api-scenelocation.fountain.coach/privkey.pem




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Testing database connection for play...
psql: error: FATAL:  Peer authentication failed for user "play"
Database connection FAILED.
Verifying GoAccess dashboard accessibility at https://logs.fountain.coach...
GoAccess dashboard is NOT accessible.
Verification completed.

```

