# Drafting a fastAPI reverse proxy API Gateway
---
### Draft 1 - The Lean Router 
---
(...lean but with problems in expressivity: the resulting openAPI of this fastAPI app will only tell a story of "well, you can send somthing there and will get back something" which defies the openAPI purpose of informing a custom GPT about how to act on calling this particular API. - BUT: we can build on it and that's why it is considered a first draft)

---

...  a shell script that automates the generation of a FastAPI application designed to serve as a reverse proxy for multiple services, with a maximum limit of 5 services. This application aims to simplify the integration of various services into a single, manageable API gateway, enhancing the ease of access and interaction with these services. 

The script will prompt the user for the names and base URLs of the services they wish to proxy, generating the necessary FastAPI code to route requests to these services accordingly.

### Shell Script for Generating FastAPI Reverse Proxy App

```bash
#!/bin/bash

echo "Automating FastAPI Reverse Proxy App Generation"
echo "------------------------------------------------"

# Initialize Python file
APP_FILE="main.py"
echo "from fastapi import FastAPI, Request
import httpx
from starlette.responses import Response

app = FastAPI()

" > $APP_FILE

# Function to add services to the FastAPI app
add_service() {
    echo "async def proxy_request(request: Request, base_url: str):
    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method=request.method,
            url=f'{base_url}' + request.url.path,
            headers={k: v for k, v in request.headers.items() if k.lower() not in ['host', 'user-agent']},
            params=request.query_params,
            content=await request.body(),
            follow_redirects=True
        )
        return Response(content=resp.content, status_code=resp.status_code, headers=dict(resp.headers))

@app.route('/$1/{proxy_path:path}', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
async def $1_proxy(request: Request):
    return await proxy_request(request, '$2')
" >> $APP_FILE
}

# Collect user inputs for up to 5 services
for i in {1..5}
do
    read -p "Enter service name (or press enter to skip): " service_name
    if [[ -z "$service_name" ]]; then
        break
    fi
    read -p "Enter base URL for $service_name: " base_url
    add_service $service_name $base_url
done

echo "FastAPI app generation complete. See $APP_FILE."
```

### Instructions:
1. Save this script to a file, e.g., `generate_fastapi.sh`.
2. Make it executable: `chmod +x generate_fastapi.sh`.
3. Run the script: `./generate_fastapi.sh`.
4. Follow the prompts to input up to 5 services.

This script generates a `main.py` FastAPI application, creating a reverse proxy for each service entered. Each service gets a dedicated route in the app, which proxies requests to the specified base URL.