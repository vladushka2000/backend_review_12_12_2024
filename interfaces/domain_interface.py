import abc


class IRoot(abc.ABC):
    """
    Интерфейс объекта root
    """

    ...


class IEntity(abc.ABC):
    """
    Интерфейс объекта entity
    """

    ...


class IValueObject(abc.ABC):
    """
    Интерфейс объекта value object
    """

    ...
