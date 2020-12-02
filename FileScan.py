import os
import argparse
from datetime import date
import stat

class FileScan:
    def __init__(self):
        self.path = ''

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Utilites scan all files in a path ")
        parser.add_argument("path", help="Path to file you want to scan ")

        return parser.parse_args()

    def scan_files(self):
        file_info = os.stat(self.path)
        print("Perms")
        print(stat.filemode(file_info.st_mode))
        print("Timestamp")
        print("Access {} ".format(date.fromtimestamp(file_info.st_atime)))
        print("Modify {} ".format(date.fromtimestamp(file_info.st_mtime)))
        print("Create {} ".format(date.fromtimestamp(file_info.st_ctime)))


    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_files()

if __name__ == '__main__':
    file_instance = FileScan()
    file_instance.main()