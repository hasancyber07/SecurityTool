@echo off
title SECURITY TOOL FINAL

cd /d "%~dp0"

echo =========================
echo   SECURITY TOOL START
echo =========================

echo.
echo [1] Compiling Server...
g++ server.cpp -o server.exe -lws2_32

echo.
echo [2] Starting Server...
start cmd /k server.exe

timeout /t 2

echo.
echo [3] Running Scanner...
start cmd /k python scanner.py

timeout /t 2

echo.
echo [4] Opening Dashboard...
start index.html

echo.
echo SYSTEM READY ✔
pause