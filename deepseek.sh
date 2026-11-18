#!/bin/bash
setsid -f google-chrome-stable --app="https://chat.deepseek.com" >/dev/null 2>&1
sleep 4
wtype -M ctrl -k v -m ctrl
sleep 2
wtype -k Return
