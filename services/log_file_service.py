from domain import root
from interfaces import service_interface
from repositories import log_file_repository as repo


class LogFileService(service_interface.IService):
    """
    Сервис для работы с лог файлами
    """

    def __init__(self, file_dir_path: str) -> None:
        """
        Инициализировать переменные
        :param file_dir_path: путь до директории с лог файлами
        """

        self.file_dir_path = file_dir_path
        self.service_logs = root.ServiceLogs()

    def get_metrics(self) -> None:
        """
        Собрать метрики с лог файлов сервиса
        """

        repository = repo.LogFileRepository(self.file_dir_path)
        log_files = repository.retrieve()

        for file in log_files:
            self.service_logs.add_log_file(file)
            self.service_logs.calc_stats(file.name)

            repository.create(file.name, file.stats)
