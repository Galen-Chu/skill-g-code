const fs = require('fs');
const path = require('path');

const rootPath = 'd:\\Skill\\skill-g-code';

const modules = [
    'program-g-code',
    'sync-g-code',
    'spiritual-g-code',
    'psychological-g-code',
    'physiological-g-code'
];

const subdirs = ['scripts', 'references', 'assets'];

console.log(`Creating directory structure at: ${rootPath}\n`);

modules.forEach(module => {
    subdirs.forEach(subdir => {
        const fullPath = path.join(rootPath, module, subdir);
        fs.mkdirSync(fullPath, { recursive: true });
        console.log(`✓ Created: ${fullPath}`);
    });
});

console.log('\n' + '='.repeat(80));
console.log('Directory structure created successfully!');
console.log('='.repeat(80) + '\n');

console.log('Verifying directory structure:\n');
const walkDir = (dir, indent = '') => {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            console.log(`${indent}${file}/`);
            walkDir(fullPath, indent + '  ');
        }
    });
};

walkDir(rootPath);
