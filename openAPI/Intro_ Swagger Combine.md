# Intro: Swagger Combine

Using **Swagger Combine** can be an efficient way to merge multiple OpenAPI/Swagger specifications into one. Swagger Combine specifically addresses the need to combine and modify multiple Swagger files, making it suitable for creating a unified API documentation or generating client libraries from a single source of truth. Here's how you can get started with Swagger Combine:

### Step 1: Install Node.js and npm

Ensure that Node.js and npm (Node Package Manager) are installed on your system. You can download them from [https://nodejs.org/](https://nodejs.org/). Installing Node.js automatically installs npm.

### Step 2: Install Swagger Combine

Install Swagger Combine globally via npm to use it from the command line anywhere on your system:

```sh
npm install -g swagger-combine
```

### Step 3: Prepare Your Configuration File

Swagger Combine uses a configuration file (in JSON or YAML format) to define how your Swagger/OpenAPI files should be merged. Here's an example of a basic configuration file, `swagger-combine-config.json`:

```json
{
  "swagger": "2.0",
  "info": {
    "title": "Combined API",
    "version": "1.0.0"
  },
  "apis": [
    {"url": "path/to/your/https-::api-act.fountain.coach.json"},
    {"url": "path/to/your/https-::api-action.fountain.coach.json"}
    // Add other API specs here
  ],
  "output": {
    "type": "json",
    "filePath": "./combinedSpec.json"
  }
}
```

- Update the `"url"` fields to point to your actual OpenAPI spec file locations.
- The `"output"` section specifies the format (`"json"` or `"yaml"`) and the file path for the combined output.

### Step 4: Run Swagger Combine

Once your configuration file is ready, run Swagger Combine using the following command, specifying your configuration file:

```sh
swagger-combine swagger-combine-config.json -o combinedSpec.json -f json
```

- `-o combinedSpec.json` specifies the output file name.
- `-f json` specifies the output format. Use `-f yaml` for YAML output.

### Step 5: Validate and Use the Combined Spec

After combining your specs, validate the output to ensure it's a valid OpenAPI spec and that the merge has met your expectations. You can use online validators or Swagger UI for this purpose.

### Notes

- The paths to your individual OpenAPI spec files in the configuration file can be local file paths or URLs.
- Swagger Combine allows for advanced configurations, such as modifying paths, excluding certain paths or definitions, and adding custom transformations. Refer to the [Swagger Combine GitHub page](https://github.com/maxdome/swagger-combine) for detailed documentation on these features.

Using Swagger Combine simplifies the process of merging multiple OpenAPI specifications into one, facilitating better API documentation management and client library generation.