# QR-info

A Class 12 Computer Science investigatory project — a QR code information system with GUI, CLI, and web interfaces.

## Overview

QR-info is a multi-interface application that scans QR codes, stores information in a MySQL database, and provides both desktop (GUI/CLI) and web interfaces for managing QR-based data. It uses OpenCV for QR detection and can generate QR codes from stored data.

## Features

- **QR scanning** via webcam or image file (OpenCV)
- **QR generation** from text data
- **MySQL database** for persistent storage
- **Three interfaces:**
  - Desktop GUI (Tkinter + Eel)
  - Command-line interface
  - Web interface (Flask)
- **AI-powered description** — uses OpenAI to generate descriptions from QR data

## Tech Stack

- **Language:** Python
- **QR:** OpenCV, qrcode[pil]
- **Database:** MySQL (mysql-connector-python)
- **GUI:** Tkinter, Eel
- **AI:** OpenAI API
- **Web:** Flask

## Setup

```bash
pip install -r requirements.txt
```

Configure MySQL connection in `mysqlConfig.py` and run:

```bash
python main.pyw.py    # GUI
python main-cli.py    # CLI
python website.py     # Web
```

## Project Structure

```
├── main.pyw.py          # GUI entry point (Eel + Tkinter)
├── main-cli.py          # CLI entry point
├── gui.py               # GUI implementation
├── cli.py               # CLI implementation
├── website.py           # Web interface + OpenAI integration
├── qr.py                # QR code detection and generation
├── sql.py               # MySQL database operations
├── setup.py             # Initial setup and config
├── mysqlConfig.py       # MySQL connection config
└── requirements.txt     # Python dependencies
```

## License

MIT
