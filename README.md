# Lucid

Send your clipboard (text or an image) to DeepSeek chat with one command.

Lucid opens DeepSeek in its own Chrome window, pastes whatever you last copied into the chat bar, and presses Enter.

## Files

| File | What it is |
| --- | --- |
| `deepseek.sh` | The tool itself. Opens DeepSeek, pastes your clipboard, and sends it |
| `install.sh` | The installer. Copies `deepseek.sh` to `~/.local/bin` as the `deepseek` command and makes it executable |
| `keyBindings.lua` | Optional example of a Hyprland hotkey for the command |
| `README.md` | This file |

## Requirements

- A Wayland session (built for Omarchy / Hyprland)
- `google-chrome-stable`
- `wl-clipboard` (provides `wl-paste`)
- `wtype` (simulates keyboard input)

Check that they are installed:

```bash
which google-chrome-stable wl-paste wtype
```

## Installation

```bash
git clone https://github.com/alishanaminnnn/Lucid
cd Lucid
bash install.sh
```

The installer copies `deepseek.sh` to `~/.local/bin/deepseek` and gives it executable permission. It warns you if a requirement is missing or if `~/.local/bin` is not in your PATH.

Check that it worked:

```bash
which deepseek
```

It should print `~/.local/bin/deepseek`.

### Manual installation

If you prefer not to use the installer, put `deepseek.sh` and `install.sh` in the same folder and run `bash install.sh`, or do it by hand:

```bash
cp deepseek.sh ~/.local/bin/deepseek
chmod +x ~/.local/bin/deepseek
```

## Usage

1. Copy some text, or take a screenshot (Omarchy copies screenshots to the clipboard).
2. Run:

```bash
deepseek
```

DeepSeek opens and your clipboard is sent.

To see what is in your clipboard first:

```bash
wl-paste -l
```

`text/plain` means text, and `image/png` means an image.

## Optional: add a hotkey

Add a line like this to your own Hyprland keybindings file (see `keyBindings.lua` for the example):

```lua
o.bind("SUPER + ALT + PRINT", "deepseek", "~/.local/bin/deepseek")
```

The exact syntax depends on how your keybindings are set up, so adjust it to match your config. Change the keys if the combination is already taken. Do not copy `keyBindings.lua` over your own file, because it would replace your existing shortcuts.

## How it works

```bash
#!/bin/bash
setsid -f google-chrome-stable --app="https://chat.deepseek.com" >/dev/null 2>&1
sleep 4
wtype -M ctrl -k v -m ctrl
sleep 2
wtype -k Return
```

1. Opens DeepSeek as a standalone Chrome app window.
2. Waits 4 seconds for the page to load.
3. Presses `Ctrl+V` to paste the clipboard into the chat bar.
4. Waits 2 seconds so an image has time to upload.
5. Presses `Enter` to send.

## Known limitations

- **It sends immediately.** Anything in your clipboard, including passwords or tokens, is sent the moment you run it. To review before sending, remove the last line of `deepseek.sh` (`wtype -k Return`) and press Enter yourself.
- **Timing is a guess.** On a slow connection, raise the first `sleep`. If it is too short, the keystrokes go to whichever window has focus.
- **Do not click another window while it runs.** `wtype` sends keys to the focused window.
- **A new window opens every run.** It does not reuse an existing DeepSeek window.
- **Wayland only.** X11 is not supported.
- **Image support depends on DeepSeek.** Pasting attaches the image, but how well DeepSeek understands it may vary.

## Customizing

| Change | How |
| --- | --- |
| Page loads slowly | Raise the first `sleep 4` in `deepseek.sh` |
| Large image not uploading in time | Raise `sleep 2` |
| Review before sending | Remove the `wtype -k Return` line |
| Another browser | Replace `google-chrome-stable` with another Chromium-based browser (Firefox has no `--app` mode) |
| Different command name | Change `NAME="deepseek"` in `install.sh` before installing |

## Uninstall

```bash
rm ~/.local/bin/deepseek
```

## License

MIT
