import os
from pathlib import Path

# Define the root path
root_path = r"d:\Skill\skill-g-code"

# Define the five modules
modules = [
    "program-g-code",
    "sync-g-code",
    "spiritual-g-code",
    "psychological-g-code",
    "physiological-g-code"
]

# Define subdirectories for each module
subdirs = [
    "scripts",
    "references",
    "assets"
]

# Create all directories
print(f"Creating directory structure at: {root_path}\n")

for module in modules:
    module_path = os.path.join(root_path, module)
    for subdir in subdirs:
        full_path = os.path.join(module_path, subdir)
        Path(full_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {full_path}")

print("\n" + "="*80)
print("Directory structure created successfully!")
print("="*80 + "\n")

# Verify the structure
print("Verifying directory structure:\n")
for root, dirs, files in os.walk(root_path):
    level = root.replace(root_path, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for dir_name in sorted(dirs):
        print(f'{subindent}{dir_name}/')
