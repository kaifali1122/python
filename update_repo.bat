@echo off
cd /d "C:\Users\DELL\Desktop\project\Python"

echo ----------------------------------
echo   🌀 Updating GitHub Repository
echo ----------------------------------

:: Get current date and time for commit message
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (
    set today=%%a-%%b-%%c
)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
    set timeNow=%%a-%%b
)

:: Combine into a single commit message
set msg=Auto Update - %today%_%timeNow%

echo.
echo Commit Message: %msg%
echo.

git add .
git commit -m "%msg%"
git push

echo ----------------------------------
echo ✅ Successfully pushed changes to GitHub!
echo ----------------------------------

pause
 

@REM \update_repo.bat  to run