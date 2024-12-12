from domain import entities
from interfaces import domain_interface as domain


class ServiceLogs(domain.IRoot):
    """
    Объект root для логов сервиса
    """

    def __init__(self) -> None:
        """
        Инициализировать переменные
        """

        self.log_files: list[entities.LogFile] = []


    def add_log_file(self, log_file: entities.LogFile) -> None:
        """
        Добавить файл логов
        :param log_file: файл логов
        """

        self.log_files.append(log_file)

    def calc_stats(self, name: str) -> None:
        """
        Посчитать статистику для файла логов
        :param name: имя файла логов
        """

        for log_file in self.log_files:
            if log_file.name == name:
                log_file.calc_stats()
