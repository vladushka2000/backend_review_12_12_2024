from dataclasses import dataclass

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


@dataclass
class Entry(domain.IValueObject):
    """
    Объект value object для одной записи лога
    """

    msg_type: enums.MessageType
    time: int
