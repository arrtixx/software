:: HTTP server running on port 19132
@echo off
title Arrtix_xSoftWare - HTTP server running on port 19132
mode con: cols=191 lines=51
echo [42m[97m[26;88HStarting server . . .[0m
echo [46m[97m[27;84Hhttp://188.167.101.092:19132/[0m
timeout 5 > nul
cls
python -m http.server 19132