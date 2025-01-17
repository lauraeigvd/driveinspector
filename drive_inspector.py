import psutil
import time
import platform
from datetime import datetime
import subprocess

class DriveInspector:
    def __init__(self, interval=60):
        self.interval = interval

    def get_drive_info(self):
        drives = []
        partitions = psutil.disk_partitions(all=False)
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            drives.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            })
        return drives

    def get_smart_status(self, drive):
        try:
            output = subprocess.check_output(["wmic", "diskdrive", "get", "status"], shell=True).decode()
            lines = output.strip().split('\n')
            for line in lines[1:]:
                if drive in line:
                    return line.strip().split()[-1]
        except Exception as e:
            return f"Error retrieving SMART status: {e}"
        return "Unknown"

    def monitor_drives(self):
        while True:
            print(f"Drive status report at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            drives = self.get_drive_info()
            for drive in drives:
                print(f"Device: {drive['device']}")
                print(f"Mountpoint: {drive['mountpoint']}")
                print(f"Filesystem Type: {drive['fstype']}")
                print(f"Total Space: {drive['total'] / (1024**3):.2f} GB")
                print(f"Used Space: {drive['used'] / (1024**3):.2f} GB")
                print(f"Free Space: {drive['free'] / (1024**3):.2f} GB")
                print(f"Usage: {drive['percent']}%")
                print(f"SMART Status: {self.get_smart_status(drive['device'])}\n")
            time.sleep(self.interval)

if __name__ == "__main__":
    if platform.system() == "Windows":
        inspector = DriveInspector(interval=60)
        inspector.monitor_drives()
    else:
        print("DriveInspector currently supports only Windows OS.")