import json
import jsonschema
from jsonschema import validate

with open('../schema/agent-schema-v0.1.json') as schema_file:
    schema = json.load(schema_file)

with open('../examples/sample-agent.json') as data_file:
    data = json.load(data_file)

validate(instance=data, schema=schema)
print("Validation passed.")
