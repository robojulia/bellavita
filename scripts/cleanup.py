import os

BASE_DIR = "site-mirror"

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Basic cleanup placeholder
            content = content.replace("Click to edit", "")

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

print("Cleanup complete")
