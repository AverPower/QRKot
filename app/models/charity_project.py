from sqlalchemy import Column, String, Text

from app.core.db import Base, ProjectMixin


class CharityProject(Base, ProjectMixin):
    """
    id — первичный ключ;
    name — уникальное название проекта, обязательное строковое поле; допустимая длина строки — от 1 до 100 символов
        включительно;
    description — описание, обязательное поле, текст; не менее одного символа;
    full_amount — требуемая сумма, целочисленное поле; больше 0;
    invested_amount — внесённая сумма, целочисленное поле; значение по умолчанию — 0;
    fully_invested — булево значение, указывающее на то, собрана ли нужная сумма для проекта (закрыт ли проект);
        значение по умолчанию — False;
    create_date — дата создания проекта, тип DateTime, должно добавляться автоматически в момент создания проекта.
    close_date — дата закрытия проекта, DateTime, проставляется автоматически в момент набора нужной суммы.
    """
    name = Column(String, unique=True)
    description = Column(Text)
