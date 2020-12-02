from systemd import journal

class LogParse:

    def __init__(self):
        self.journal_reader = journal.Reader()

    def main(self):
        self.journal_reader.this_boot()
        try:
            for event in self.journal_reader:
                    if "error" in event['MESSAGE']:
                            # print(event["_HOSTNAME"])
                            print(event)
        except IOError:
            print("Bineary")


if __name__ ==  '__main__':
    log_instance = LogParse()
    log_instance.main()
