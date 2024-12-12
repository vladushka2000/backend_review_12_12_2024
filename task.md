Есть некоторое число сервисов, которые генерируют логи о выполненных задачах. Лог-файл каждого сервиса имеет следующий формат:

START 1
END 5
START 6
END 10
START 11
START 14
START 15

Есть два вида сообщений START и END , рядом с каждым сообщением указывается timestamp , указывающий, когда сервис либо начал обрабатывать задачу (START), 
либо завершил (END) ее выполнение. Иногда сервис начинает выполнять задачу, но не завершает ее выполнение из-за ошибки, 
в таком случае в логе можно видеть несколько подряд идущих сообщений START .

Каждый сервис может генерировать множество лог-файлов, которые сохраняются на диск под с именем servicename-timestamp.log,  
например: service1-1716916620.log , service1-1716916625.log , service2-1716916650.log .

Вашей задачей является для каждого лог-файла собрать следующие метрики:

total  - общее число задач
success  - число успешно выполненных задач
errors  - число незавершенных задач
success_mean_time  - среднее время выполнения задачи на сервисе

и сохранить в json-файле с тем же именем, что и у лог-файла, но расширением *.json :

{"total": 5, "errors": 3, "success": 2, "success_mean_time": 4}




Статистика по лог-файлу из примера выше:

общее число задач - 5
число успешно выполненных задач - 2
число незавершенных задач - 3
среднее время выполнения задачи - 4




Создание тестовых файлов:

from pathlib import Path


def create_test_log_files(log_dir: Path) -> None:
    with (log_dir / "service1-1716916620.log").open(mode="w") as logfile:
        logfile.write("""START 1
END 5
START 6
END 10
START 11
START 14
START 15""")

    with (log_dir / "service1-1716916625.log").open(mode="w") as logfile:
        logfile.write("""START 21
END 25
START 26
END 30
START 31
START 34
END 35""")

    with (log_dir / "service2-1716916650.log").open(mode="w") as logfile:
        logfile.write("""START 1
END 5
START 6
END 10
START 11
START 14
START 15""")


if __name__ == "__main__":
    create_test_log_files(Path("."))