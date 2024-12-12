from dataclasses import asdict, dataclass

from interfaces import domain_interface as domain
from tools import enums


@dataclass
class Stats(domain.IValueObject):
    """
    Объект value object для статистики
    """

    tasks_count: int = 0
    success_tasks: int = 0
    fail_tasks: int = 0
    mean_time: int = 0

    def to_dict(self):
        """
        Получить объект словаря на основе полей value object
        :return: словарь
        """

        return {k: str(v) for k, v in asdict(self).items()}


@dataclass
class Entry(domain.IValueObject):
    """
    Объект value object для одной записи лога
    """

    msg_type: enums.MessageType
    time: int

    def to_dict(self):
        """
        Получить объект словаря на основе полей value object
        :return: словарь
        """

        raise NotImplementedError
