import json

class PageAssemblyAgent:
    def save(self, data, path):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
