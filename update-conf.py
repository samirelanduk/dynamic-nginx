import os

for var in [v for v in os.environ if v.startswith("DYNAMIC_")]:
    
    hostname = var[8:].lower().replace("_", ".")
    filename = os.environ[var]
    
    with open("template.conf") as f:
        contents = f.read()
    
    with open(f"/etc/nginx/sites-enabled/{hostname}", "w" ) as f:
        f.write(contents.replace("$1", hostname).replace("$2", filename))