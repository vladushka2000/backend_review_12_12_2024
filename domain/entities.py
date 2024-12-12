from domain import value_objects
from interfaces import domain_interface as domain
from tools import enums


class LogFile(domain.IEntity):
    """
    Объект entity для файла логов
    """

    def __init__(self, name: str) -> None:
        """
        Инициализировать переменные
        :param name: имя файла
        """

        self.name = name
        self.entries: list[value_objects.Entry] = []
        self.stats = value_objects.Stats()

    def calc_stats(self) -> None:
        """
        Посчитать статистику
        """

        self.stats.tasks_count = len(self.entries)

        success_tasks_count = 0
        fail_tasks_count = 0
        task_start_time = 0
        exec_times = []
        is_task_running = False

        # Расчет успешных и неуспешных тасок
        for entry in self.entries:
            if entry.msg_type == enums.MessageType.START and not is_task_running:
                is_task_running = True
                task_start_time = entry.time
            elif entry.msg_type == enums.MessageType.END:
                is_task_running = False
                success_tasks_count += 1
                exec_times.append(entry.time - task_start_time)
            else:
                is_task_running = False
                fail_tasks_count += 1

        self.stats.mean_time = sum(exec_times) / len(exec_times)
