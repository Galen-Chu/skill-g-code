@echo off
cd d:\Skill

REM Create root directory
if not exist skill-g-code mkdir skill-g-code
cd skill-g-code

REM Create program-g-code module
if not exist program-g-code\scripts mkdir program-g-code\scripts
if not exist program-g-code\references mkdir program-g-code\references
if not exist program-g-code\assets mkdir program-g-code\assets

REM Create sync-g-code module
if not exist sync-g-code\scripts mkdir sync-g-code\scripts
if not exist sync-g-code\references mkdir sync-g-code\references
if not exist sync-g-code\assets mkdir sync-g-code\assets

REM Create spiritual-g-code module
if not exist spiritual-g-code\scripts mkdir spiritual-g-code\scripts
if not exist spiritual-g-code\references mkdir spiritual-g-code\references
if not exist spiritual-g-code\assets mkdir spiritual-g-code\assets

REM Create psychological-g-code module
if not exist psychological-g-code\scripts mkdir psychological-g-code\scripts
if not exist psychological-g-code\references mkdir psychological-g-code\references
if not exist psychological-g-code\assets mkdir psychological-g-code\assets

REM Create physiological-g-code module
if not exist physiological-g-code\scripts mkdir physiological-g-code\scripts
if not exist physiological-g-code\references mkdir physiological-g-code\references
if not exist physiological-g-code\assets mkdir physiological-g-code\assets

echo.
echo Directory structure created successfully!
echo.
tree /f

pause
