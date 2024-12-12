from pathlib import Path


def create_test_log_files(log_dir: Path) -> None:
    with (log_dir / "service1-1716916620.log").open(mode="w") as logfile:
        logfile.write(
        """
            START 1
            END 5
            START 6
            END 10
            START 11
            START 14
            START 15
        """
        )

    with (log_dir / "service1-1716916625.log").open(mode="w") as logfile:
        logfile.write(
        """
            START 21
            END 25
            START 26
            END 30
            START 31
            START 34
            END 35
        """
        )

    with (log_dir / "service2-1716916650.log").open(mode="w") as logfile:
        logfile.write(
        """
            START 1
            END 5
            START 6
            END 10
            START 11
            START 14
            START 15
        """
        )


if __name__ == "__main__":
    create_test_log_files(Path("."))
