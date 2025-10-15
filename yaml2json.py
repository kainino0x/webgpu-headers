#!/usr/bin/env python3
import yaml
import json
with open("webgpu.yml", 'r') as yaml_in, open("webgpu.json", "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, json_out, indent=2)

