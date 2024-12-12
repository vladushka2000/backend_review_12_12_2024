import abc


class IRepository(abc.ABC):
    """
    Интерфейс репозитория
    """

    @abc.abstractmethod
    def create(self, *args, **kwargs) -> any:
        """
        Сделать запись
        """

        raise NotImplementedError

    @abc.abstractmethod
    def retrieve(self, *args, **kwargs) -> any:
        """
        Получить данные
        """

        raise NotImplementedError
