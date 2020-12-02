import os
import argparse
import datetime
# from datetime import datetime
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

        rootdir = self.path
        for rootdir, dirs, files in os.walk(rootdir):
            for subdir in dirs:
                file = os.path.join(rootdir, subdir)
                try:
                    print(file)
                    file_info = os.stat(file)
                    print("Perms")
                    print(stat.filemode(file_info.st_mode))
                    print("Timestamp")
                    print("Access {} ".format(datetime.datetime.fromtimestamp(file_info.st_atime)))
                    print("Modify {} ".format(datetime.datetime.fromtimestamp(file_info.st_mtime)))
                    print("Create {} ".format(datetime.datetime.fromtimestamp(file_info.st_ctime)))
                    print("\n")
                except IOError:
                    print("File not accessible")

    def find_timestamp(self):
        search_date = datetime.datetime(2020, 5, 6, 9, 39)
        rootdir = self.path
        for rootdir, dirs, files in os.walk(rootdir):
            for subdir in dirs:
                file = os.path.join(rootdir, subdir)
                try:
                    file_info = os.stat(file)
                    # Pliki stworzone wcześniej niż search_date
                    if (datetime.datetime.fromtimestamp(file_info.st_ctime)) < search_date:
                    # Dostęp do pliku wcześniej niż search_date
                    # if (datetime.datetime.fromtimestamp(file_info.st_atime)) < search_date:
                    # Pliki modyfikowane wcześniej niż search_date
                    # if (datetime.datetime.fromtimestamp(file_info.st_mtime)) < search_date:
                        print(file)
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

        # self.scan_path()
        self.find_timestamp()


if __name__ == '__main__':
    walk_instance = DirectoryWalk()
    walk_instance.main()
