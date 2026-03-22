import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Simple regex to find and remove conflict markers, keeping the 'ours' (local) version
    # This pattern handles:
    # <<<<<<< HEAD
    # [LOCAL CONTENT]
    # =======
    # [REMOTE CONTENT]
    # >>>>>>> [COMMIT_ID]
    
    new_content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> [a-f0-9]+', r'\1', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

root_dir = '.'
for root, dirs, files in os.walk(root_dir):
    if '.git' in dirs:
        dirs.remove('.git')
    for file in files:
        if file.endswith(('.py', '.js', '.json', '.txt', '.env', '.md')):
            path = os.path.join(root, file)
            if clean_file(path):
                print(f"Cleaned: {path}")
