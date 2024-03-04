# The single moment of truth

Merging multiple OpenAPI specifications into one document manually allows for precise control over the final combined spec. This process can be especially useful when dealing with specs that have unique `servers` declarations, different paths, or shared components. Below is a step-by-step tutorial on how to manually merge multiple OpenAPI specs using a JSON editor.

### Prerequisites
- **OpenAPI Specs**: Ensure all your OpenAPI specs are in JSON format for ease of editing. If they are in YAML, convert them to JSON.
- **JSON Editor**: Use a JSON editor that supports syntax highlighting and structure validation, such as Visual Studio Code, to simplify the process.

### Step 1: Prepare the Base Document
Select one of your OpenAPI specs as the base document to which you will add content from the other specs. This is usually the spec that contains the most comprehensive information or serves as the primary API.

### Step 2: Merge `openapi` and `info` Sections
- **`openapi`**: Ensure that all your specs are using the same version of the OpenAPI Specification. If not, update them to be consistent.
- **`info`**: The `info` section from your base document will remain. If there are relevant pieces from the other specs (like version numbers, titles, or descriptions that need to be combined), manually integrate them into the base document's `info` section.

### Step 3: Combine `servers` Declarations
Each OpenAPI spec might declare its own set of servers. Combine all unique server objects into the base document’s `servers` array. Ensure no duplicates unless they serve a different purpose (e.g., different environments).

### Step 4: Merge Paths
- Go through the `paths` section of each spec. For each path, check if it exists in your base document.
- If a path does not exist in the base document, copy it directly.
- If a path exists but has different operations (GET, POST, etc.), merge the operations under the same path.
- Resolve any conflicts or duplications manually, ensuring that each operation's parameters, responses, and descriptions are accurately represented.

### Step 5: Merge `components`
The `components` section (schemas, responses, parameters, examples, requestBodies, headers, securitySchemes, links, and callbacks) often contains shared definitions used across multiple paths.
- Carefully combine the components from each spec into the base document’s `components` section.
- Watch out for components with the same name but different structures. You might need to rename and update references or reconcile the differences manually.

### Step 6: Integrate Tags, ExternalDocs, and Security
- **Tags**: Merge the `tags` arrays, removing duplicates.
- **ExternalDocs**: Decide which external documentation references to keep if they differ between specs.
- **Security**: Merge security definitions if they are not identical, ensuring that all referenced security schemes are included in the combined `components/securitySchemes` section.

### Step 7: Validate the Merged Document
Use an OpenAPI validation tool to ensure that your merged document adheres to the OpenAPI specification. Resolve any reported issues.

### Step 8: Save and Use Your Merged OpenAPI Spec
Once validated, save your merged OpenAPI spec. You can now use it as a single source of truth for your combined API services.

### Tips for a Successful Merge
- **Back Up Original Specs**: Always keep a copy of your original specs before starting the merge process.
- **Incremental Merging**: Consider merging specs incrementally (one by one) and validating each step to manage complexity.
- **Custom Tooling**: For repetitive merging tasks, consider developing scripts or tools that automate parts of this process, especially around combining `servers` and resolving component conflicts.

Merging OpenAPI specs manually requires attention to detail and a good understanding of the OpenAPI specification. This process ensures that the final document is coherent, avoids duplication, and accurately represents the combined capabilities of your APIs.