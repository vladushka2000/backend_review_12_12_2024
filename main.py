import os

from services import log_file_service

service = log_file_service.LogFileService(os.path.curdir)

if __name__ == "__main__":
    service.get_metrics()
