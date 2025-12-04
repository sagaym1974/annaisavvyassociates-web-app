@echo off
start cmd /k "cd /d C:\Users\VIJAY\Desktop\Web Photo Stocks\public && python -m http.server 8000"
timeout /t 2 /nobreak > nul
start chrome "http://localhost:8000/index.html"
