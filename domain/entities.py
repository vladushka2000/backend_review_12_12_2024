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

    def add_entry(self, entry: value_objects.Entry) -> None:
        """
        Добавить запись
        :param entry: запись
        """

        self.entries.append(entry)

    def calc_stats(self) -> None:
        """
        Посчитать статистику
        """

        success_tasks_count = 0
        fail_tasks_count = 0
        task_start_time = 0
        exec_times = []
        is_task_running = False

        # Расчет успешных и неуспешных тасок
        for entry_num, entry in enumerate(self.entries):
            if entry.msg_type == enums.MessageType.START and not is_task_running:
                is_task_running = True
                task_start_time = entry.time
            elif entry.msg_type == enums.MessageType.END:
                is_task_running = False
                success_tasks_count += 1
                exec_times.append(entry.time - task_start_time)
            else:
                fail_tasks_count += 1

            if entry.msg_type == enums.MessageType.START and entry_num == len(self.entries) - 1:
                fail_tasks_count += 1

        self.stats.tasks_count = success_tasks_count + fail_tasks_count
        self.stats.success_tasks = success_tasks_count
        self.stats.fail_tasks = fail_tasks_count
        self.stats.mean_time = int(sum(exec_times) / len(exec_times))
