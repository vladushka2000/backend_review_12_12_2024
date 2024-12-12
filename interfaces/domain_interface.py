import abc


class IRoot(abc.ABC):
    """
    Интерфейс объекта root
    """

    pass


class IEntity(abc.ABC):
    """
    Интерфейс объекта entity
    """

    pass


class IValueObject(abc.ABC):
    """
    Интерфейс объекта value object
    """

    @abc.abstractmethod
    def to_dict(self) -> dict:
        """
        Получить объект словаря на основе полей value object
        :return: словарь
        """

        raise NotImplementedError
