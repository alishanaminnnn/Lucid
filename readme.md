# Lucid

Send your clipboard (text or an image) to DeepSeek chat with one command or one key combo.

Lucid is two small files:

| File | Purpose |
| --- | --- |
| `deepseek.sh` | Opens DeepSeek in its own Chrome window, pastes your clipboard, and sends it |
| `keyBindings.lua` | A keybinding that runs the script with `SUPER + ALT + PRINT` |

## How it works

1. Opens `https://chat.deepseek.com` as a standalone Chrome app window (no tabs or address bar).
2. Waits 4 seconds for the page to load.
3. Presses `Ctrl+V` to paste the clipboard into the chat bar.
4. Waits 2 seconds so an image has time to upload.
5. Presses `Enter` to send.

Pasting instead of typing means multi-line text arrives in one piece and images work too.

## Requirements

- A Wayland session (built for Omarchy / Hyprland)
- `google-chrome-stable`
- `wl-clipboard` (provides `wl-paste`)
- `wtype` (simulates keyboard input)
- `alacritty`, only if you keep the keybinding exactly as written below

Check that everything is installed:

```bash
which google-chrome-stable wl-paste wtype alacritty
```

## Installation

### 1. Install the script

```bash
cp deepseek.sh ~/.local/bin/deepseek
chmod +x ~/.local/bin/deepseek
```

`~/.local/bin` must be in your PATH. After this, typing `deepseek` in a terminal runs it.

### 2. Add the keybinding

Add this line anywhere in your Hyprland keybindings Lua file:

```lua
o.bind("SUPER + ALT + PRINT", "deepseek", "alacritty -e ~/.local/bin/deepseek")
```

Then reload your Hyprland config, or log out and back in, so the binding takes effect.

## Usage

1. Copy some text, or take a screenshot (Omarchy copies screenshots to the clipboard).
2. Press `SUPER + ALT + PRINT`, or run `deepseek` in a terminal.

DeepSeek opens and your clipboard is sent.

To see what is in your clipboard before sending:

```bash
wl-paste -l
```

`text/plain` means text, and `image/png` means an image.

## The files

### deepseek.sh

```bash
#!/bin/bash
setsid -f google-chrome-stable --app="https://chat.deepseek.com" >/dev/null 2>&1
sleep 4
wtype -M ctrl -k v -m ctrl
sleep 2
wtype -k Return
```

### keyBindings.lua

```lua
o.bind("SUPER + ALT + PRINT", "deepseek", "alacritty -e ~/.local/bin/deepseek")
```

## Known limitations

- **Timing is a guess.** The fixed `sleep` values assume the page loads in 4 seconds. On a slow connection, raise the first `sleep`. If it is too short, the keystrokes go to whichever window has focus, which may not be DeepSeek.
- **It sends immediately.** Anything in your clipboard, including passwords or tokens, is sent the moment the script runs. To review before sending, delete the last line (`wtype -k Return`) and press Enter yourself.
- **Focus matters.** `wtype` sends keys to the focused window. Do not click another window while the script is waiting.
- **A new window opens every run.** The script does not reuse an existing DeepSeek window.
- **A terminal window flashes open.** The keybinding runs the script inside Alacritty, which is not needed. See the tip below.
- **Image support depends on DeepSeek.** Pasting attaches the image, but how well DeepSeek understands it may vary.

## Customizing

| Change | How |
| --- | --- |
| Page loads slowly | Raise the first `sleep 4` to `6` or more |
| Large image not uploading in time | Raise `sleep 2` |
| Review before sending | Remove the `wtype -k Return` line |
| Use another browser | Replace `google-chrome-stable` with another Chromium-based browser (Firefox has no `--app` mode) |
| Different key combo | Change `"SUPER + ALT + PRINT"` in the keybinding line |

### Tip: skip the terminal

The script prints nothing, so it does not need a terminal. Pointing the keybinding straight at the script avoids the extra window:

```lua
o.bind("SUPER + ALT + PRINT", "deepseek", "~/.local/bin/deepseek")
```

Use whichever form works with your keybinding setup.

## License

MIT