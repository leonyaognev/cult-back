from pydantic_settings import BaseSettings
import sqlalchemy


class Settings(BaseSettings):
    """Настройки приложения.

    Все поля поддерживают загрузку из переменных окружения, кроме тех,
    где явно указано `env: None`.
    """

    model_config = {"env_file": ".env"}

    SQLALCHEMY_DRIVERNAME: str
    """Название драйвера SQLAlchemy для строки подключения."""

    DB_USERNAME: str | None = None
    """Имя пользователя для подключения к БД."""

    DB_PASSWORD: str | None = None
    """Пароль для подключения к БД."""

    DB_HOST: str | None = None
    """Адрес хоста для подключения к БД."""

    DB_PORT: int | None = None
    """Номер порта для подключения к БД."""

    DB_DATABASE: str
    """Название базы данных."""

    @property
    def SQLALCHEMY_CONNECTION_STRING(self) -> str:
        """Строка подключения к базе данных для SQLAlchemy."""
        return sqlalchemy.URL.create(
            drivername=self.SQLALCHEMY_DRIVERNAME,
            username=self.DB_USERNAME,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_DATABASE,
        ).render_as_string(hide_password=False)


settings = Settings()
