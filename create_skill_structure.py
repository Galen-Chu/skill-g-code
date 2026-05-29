#!/usr/bin/env python3
"""
skill-g-code Project Structure Generator
Creates the complete skill-g-code directory structure with all SKILL.md files
"""

import os
import sys
from pathlib import Path

# Define the project structure
MODULES = {
    'program-g-code': {
        'title': '💻 Software Engineering and Infrastructure',
        'description': 'Declaring Django, Docker, and Pytest Boundaries'
    },
    'sync-g-code': {
        'title': '🛰️ Core Scheduling and Life Data Stream Synchronization',
        'description': 'Declaring Aether-Kernel Data Pipeline Logic'
    },
    'spiritual-g-code': {
        'title': '🪐 Celestial Transits and High-Dimensional Geometric Decoding',
        'description': 'Declaring Astrological Calculations and Brand Manifesto Dialect'
    },
    'psychological-g-code': {
        'title': '🧠 Subconscious Debugging and Mind Refinement',
        'description': 'Declaring Dream Decoding and Latour Critique Philosophy Boundaries'
    },
    'physiological-g-code': {
        'title': '🏃‍♂️ Physical Hardware Maintenance and Grounding Practices',
        'description': 'Declaring Biometric Metrics and Somatic Telemetry'
    }
}

SUBDIRS = ['scripts', 'references', 'assets']

def create_directory_structure(base_path):
    """Create the complete directory structure"""
    
    print("🚀 Creating skill-g-code project structure...")
    print(f"📁 Base path: {base_path}\n")
    
    # Create root directory
    root_dir = Path(base_path) / 'skill-g-code'
    root_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created root directory: {root_dir}")
    
    # Create module directories
    for module_name, module_info in MODULES.items():
        module_dir = root_dir / module_name
        module_dir.mkdir(exist_ok=True)
        print(f"\n✅ Created module: {module_name}")
        
        # Create subdirectories
        for subdir in SUBDIRS:
            subdir_path = module_dir / subdir
            subdir_path.mkdir(exist_ok=True)
            print(f"   ├── {subdir}/")
    
    print("\n" + "="*60)
    print("✨ Project structure created successfully!")
    print("="*60)
    
    # Print structure
    print("\n📊 Directory Structure:")
    print_tree(root_dir, prefix="", is_last=True)
    
    return root_dir

def print_tree(path, prefix="", is_last=True):
    """Print directory tree structure"""
    
    if path.is_file():
        return
    
    # Get all items
    items = sorted(path.iterdir())
    dirs = [item for item in items if item.is_dir()]
    files = [item for item in items if item.is_file()]
    
    all_items = files + dirs
    
    for i, item in enumerate(all_items):
        is_last_item = (i == len(all_items) - 1)
        current_prefix = "└── " if is_last_item else "├── "
        print(f"{prefix}{current_prefix}{item.name}")
        
        if item.is_dir():
            next_prefix = prefix + ("    " if is_last_item else "│   ")
            print_tree(item, next_prefix, is_last_item)

def main():
    """Main entry point"""
    
    base_path = r"d:\Skill"
    
    # Check if path exists
    if not os.path.exists(base_path):
        print(f"❌ Error: Base path does not exist: {base_path}")
        print("Please create d:\\Skill directory first or provide a valid path.")
        sys.exit(1)
    
    try:
        root_dir = create_directory_structure(base_path)
        
        print("\n🎉 Setup complete!")
        print("\nNext steps:")
        print("1. Add SKILL.md files to each module directory")
        print("2. Add README.md to the root directory")
        print("3. Review PROJECT_SETUP_GUIDE.md for detailed information")
        print("\nQuick navigation:")
        for module_name, module_info in MODULES.items():
            print(f"  • {module_name}: {module_info['title']}")
        
    except Exception as e:
        print(f"\n❌ Error creating structure: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
