# Radio Panel

A lightweight Python application for streaming online radio stations through a simple GUI. Built with FreeSimpleGUI and VLC, it provides nine preset station buttons, play/pause/stop controls, volume adjustment, and a minimized "mini-player" mode.
---

## Description

Radio Panel reads a list of station names, images, and stream URLs from a text file, then displays an on-screen panel with:

- Nine station buttons
- Play/Pause toggle
- Stop (exit) button
- Minimize toggle (switch between full and compact view)
- Volume slider

Clicking the "external player" button will launch your default browser or media player with the current stream URL and then exit the app. 

The project started out of a personal need – a desire to make it easier to listen to radio stations on a computer. The inspiration was car radio systems, where changing stations is done with a single button press.


---

## Requirements

- Python 3.7 or newer
- VLC media player
- Python packages:
  - **FreeSimpleGUI**: https://github.com/timofurrer/FreeSimpleGUI
  - **python-vlc**: https://pypi.org/project/python-vlc/

---

## Installation

1. Clone or download this repository.
2. Install the required Python libraries:
   ```bash
   pip install FreeSimpleGUI python-vlc
   ```
3. Ensure VLC is installed on your system and accessible via your PATH.

---

## Directory Structure

Place files exactly as shown:

```
radio-panel/
├── source.txt            # station definitions: image_filename,stream_url
├── imgs/                  # station-image files, control icons for play/pause, stop, minimize
│   ├── pause.png
│   ├── close.png
│   └── minimize.png
└── radio_panel.py         # main application script
```

---

## Configuration

Edit `source.txt`, adding one station per line in the form:

```
<image_filename>,<stream_url>
```

**Example:**

```
classic_rock.png,http://stream.example.com:8000/rock
jazz_vibes.png,http://stream.example.com:8000/jazz
```

- `<image_filename>` must match a file under the `imgs/` directory
- `<stream_url>` is the direct URL to the audio stream

All images must be .png or .gif format. for the first six stations logos must have maximum resolution of 84x84 and others are 60x60.(Oversized images will only have the top left corner displayed)

---

## Usage

1. From the `radio-panel/` folder, run:
   ```bash
   python radio_panel.py
   ```

2. **Controls:**
   - Click a station button to start streaming
   - Click the pause button to toggle playback
   - Click stop to halt playback and close the app
   - Use minimize to collapse into the compact control bar
   - Adjust the volume slider as needed
   - Click the "external player" button to open the stream URL in your default browser or media player

---

## Tested System

- Windows 11
- Python 3.13.5
- VLC media player installed and in your system PATH

---