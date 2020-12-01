import os
import argparse
import datetime
# from datetime import date
import stat

class DirectoryWalk:
    def __init__(self):
        self.path = ''

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Scan all magic files ")
        parser.add_argument("path", help="Path to folder ")

        return parser.parse_args()

    def scan_path(self):
        with os.scandir(self.path) as iter_path:
            for entry in iter_path:
                try:
                    if entry.is_file():
                        print(entry.name)
                        file_info = os.stat(entry)
                        print("Perms")
                        print(stat.filemode(file_info.st_mode))
                        print("Timestamp")
                        print("Access {} ".format(datetime.datetime.fromtimestamp(file_info.st_atime)))
                        print("Modify {} ".format(datetime.datetime.fromtimestamp(file_info.st_mtime)))
                        print("Create {} ".format(datetime.datetime.fromtimestamp(file_info.st_ctime)))
                        print("\n")
                except IOError:
                    print("File not accessible")

    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_path()


if __name__ == '__main__':
    walk_instance = DirectoryWalk()
    walk_instance.main()