from sqlalchemy import Column, Integer, Text, ForeignKey

from app.core.db import Base, ProjectMixin


class Donation(ProjectMixin, Base):
    """
    id — первичный ключ;
    user_id — id пользователя, сделавшего пожертвование. Foreign Key на поле user.id из таблицы пользователей;
    comment — необязательное текстовое поле;
    full_amount — сумма пожертвования, целочисленное поле; больше 0;
    invested_amount — сумма из пожертвования, которая распределена по проектам; значение по умолчанию равно 0;
    fully_invested — булево значение, указывающее на то, все ли деньги из пожертвования были переведены в тот
        или иной проект; по умолчанию равно False;
    create_date — дата пожертвования; тип DateTime; добавляется автоматически в момент поступления пожертвования;
    close_date — дата, когда вся сумма пожертвования была распределена по проектам; тип DateTime; добавляется
        автоматически в момент выполнения условия.
    """
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
