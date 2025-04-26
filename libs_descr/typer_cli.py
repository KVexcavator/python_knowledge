# pip install typer
# https://typer.tiangolo.com/#installation
# Создание многоуровневого CLI-интерфейса на базе Typer
# Зачем?
# Внутренние CLI-инструменты для команды
# DevOps-скрипты, CI/CD, деплой
# Утилиты для обработки данных, генерации отчётов
# Обёртки над скриптами, которые хочется запускать красиво

import typer

app = typer.Typer()
user_app = typer.Typer()
app.add_typer(user_app, name="user")

@user_app.command()
def create(name: str, admin: bool = False):
    typer.echo(f"Создан пользователь: {name}, Админ: {admin}")

@user_app.command()
def delete(name: str):
    typer.echo(f"Удалён пользователь: {name}")

@app.command()
def export(format: str = typer.Option("json", help="Формат экспорта")):
    typer.echo(f"Экспорт данных в формате: {format}")

if __name__ == "__main__":
    app()

# python3 typer_cli.py user create Vasiliy
# python3 typer_cli.py user delete Bobik
# python3 typer_cli.py export
# python3 typer_cli.py export --format txt