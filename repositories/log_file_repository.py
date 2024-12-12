import json
import os

from domain import entities, value_objects
from interfaces import repository_interface as repo
from tools import enums


class LogFileRepository(repo.IRepository):
    """
    Репозиторий для файлов логов
    """

    def __init__(self, file_dir_path: str) -> None:
        """
        Инициализировать переменные
        :param file_dir_path: путь до директории сохранения
        """

        self.file_dir_path = file_dir_path

    def create(self, file_name: str, stats: value_objects.Stats) -> None:
        """
        Создать JSON-файл
        :param file_name: имя файла
        :param stats: статистика по логам
        """

        save_path = os.path.join(self.file_dir_path, f"{file_name.rstrip(".log")}.json")

        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(stats.to_dict(), file)

    def retrieve(self) -> list[entities.LogFile]:
        """
        Получить логи
        :return: объекты entity, содержащие логи
        """

        file_names: list[str] = []
        log_files: list[entities.LogFile] = []

        for file in os.listdir(self.file_dir_path):
            if file.endswith(".log"):
                file_names.append(file)


        for name in file_names:
            file_path = os.path.join(self.file_dir_path, name)
            log_file = entities.LogFile(name=name)

            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    msg_type, time = line.split()

                    log_file.add_entry(
                        value_objects.Entry(
                            msg_type=enums.MessageType[msg_type],
                            time=int(time)
                        )
                    )

            log_files.append(log_file)

        return log_files
