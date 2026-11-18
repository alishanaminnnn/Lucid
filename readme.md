# Lucid
 
Send whatever is on your clipboard (text or an image) to DeepSeek chat with one command.
 
Lucid is a small Bash script. It opens DeepSeek in its own Chrome app window, pastes your clipboard into the chat bar, and presses Enter.
 
## How it works
 
1. Opens `https://chat.deepseek.com` in a standalone Chrome window (no tabs or address bar).
2. Waits 4 seconds for the page to load.
3. Presses `Ctrl+V` to paste the clipboard into the chat bar.
4. Waits 2 seconds (time for an image to upload).
5. Presses `Enter` to send.
Because it pastes instead of typing, multi-line text arrives in one piece and images work too.
 
## Requirements
 
- A Wayland session (built and tested on Omarchy / Hyprland)
- `google-chrome-stable`
- `wl-clipboard` (provides `wl-copy` and `wl-paste`)
- `wtype` (simulates keyboard input)
Check that everything is installed:
 
```bash
which google-chrome-stable wl-paste wtype
```
 
## Installation
 
Save the script as `lucid` in a folder on your PATH, then make it executable:
 
```bash
mv lucid.sh ~/.local/bin/lucid
chmod +x ~/.local/bin/lucid
```
 
## Usage
 
1. Copy some text, or take a screenshot (Omarchy copies screenshots to the clipboard).
2. Run:
```bash
lucid
```
 
DeepSeek opens and your clipboard is sent.
 
To check what is in your clipboard before running it:
 
```bash
wl-paste -l
```
 
`text/plain` means text, and `image/png` means an image.
 
## The script
 
```bash
#!/bin/bash
setsid -f google-chrome-stable --app="https://chat.deepseek.com" >/dev/null 2>&1
sleep 4
wtype -M ctrl -k v -m ctrl
sleep 2
wtype -k Return
```
 
## Known limitations
 
- **Timing is a guess.** The fixed `sleep` values assume the page loads in 4 seconds. On a slow connection, increase the first `sleep`. If it is too short, the keystrokes go to whichever window has focus, which may not be DeepSeek.
- **It sends immediately.** Anything in your clipboard, including passwords or tokens, is sent as soon as the script runs. To review before sending, delete the last line (`wtype -k Return`) and press Enter yourself.
- **Focus matters.** `wtype` types into the focused window. Do not click another window while the script is waiting.
- **A new window opens each run.** The script does not reuse an existing DeepSeek window.
- **Image support depends on DeepSeek.** Pasting an image attaches it, but how well DeepSeek understands images may vary.
## Customizing
 
| Change | How |
| --- | --- |
| Page loads slowly | Raise the first `sleep 4` to `6` or more |
| Large image not uploading in time | Raise `sleep 2` |
| Review before sending | Remove the `wtype -k Return` line |
| Use another browser | Replace `google-chrome-stable` with another Chromium-based browser (Firefox has no `--app` mode) |
 
## License
 
MIT
 