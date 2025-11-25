from . import tasks


def main():
    result = tasks.add.delay(4, 4)

    output = result.get(timeout=10)
    print(f"Task result: {output}")


if __name__ == "__main__":
    main()
