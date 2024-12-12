import json
import os

from domain import value_objects
from interfaces import repository_interface as repo
from tools import enums


class LogFileRepository(repo.IRepository):
    """
    Репозиторий для файлов логов
    """

    def create(self, file_name: str, file_dir_path: str, stats: value_objects.Stats) -> None:
        """
        Создать JSON-файл
        :param file_name: имя файла
        :param file_dir_path: путь до директории сохранения
        :param stats: статистика по логам
        """

        save_path = os.path.join(file_dir_path, f"{file_name}.json")

        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(stats.to_dict(), file)

    def retrieve(self, file_name: str, file_dir_path: str) -> list[value_objects.Entry]:
        """
        Получить лооги
        :param file_name: имя файла
        :param file_dir_path: путь до директории сохранения
        :return: объекты entity, содержащие логи
        """

        file_path = os.path.join(file_dir_path, f"{file_name}.log")
        entries = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                msg_type, time = line.split()

                entries.append(
                    value_objects.Entry(
                        msg_type=enums.MessageType[msg_type],
                        time=int(time)
                    )
                )

        return entries
