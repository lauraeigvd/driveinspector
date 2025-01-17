# DriveInspector

DriveInspector is a Python-based tool designed to monitor the health and performance of hard drives and SSDs on Windows systems. It provides detailed information about the drives' usage and SMART status, helping you keep track of your storage devices' health.

## Features

- Monitors the space usage of all available drives.
- Retrieves and displays the SMART status for each drive.
- Provides a user-friendly, periodic report of drive health and performance.

## Requirements

- Python 3.6+
- `psutil` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DriveInspector.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DriveInspector
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:
   ```
   psutil
   ```

## Usage

Run the `drive_inspector.py` script:

```bash
python drive_inspector.py
```

The program will run indefinitely, printing a drive status report every 60 seconds. To stop the program, use `Ctrl+C`.

## Note

- DriveInspector currently supports only Windows OS.
- Ensure that you have the necessary permissions to execute WMIC commands on your system.

## Contributing

Contributions are welcome! Please submit a pull request or create an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License.