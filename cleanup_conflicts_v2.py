import os
import re

def clean_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception:
        return False
    
    new_lines = []
    in_conflict = False
    in_theirs = False
    modified = False
    
    for line in lines:
        if line.startswith('<<<<<<<'):
            in_conflict = True
            in_theirs = False
            modified = True
            continue
        if line.startswith('======='):
            in_theirs = True
            continue
        if line.startswith('>>>>>>>'):
            in_conflict = False
            in_theirs = False
            continue
        
        if in_conflict:
            if not in_theirs:
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
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
