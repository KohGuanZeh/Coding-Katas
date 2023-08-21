import os, argparse, json

EXERCISE_CONFIGS_PATH = "./exercise_configs.json"


def create_exercise_items(index: int, base_file_name: str) -> None:
    directory = f"./exercises/exercise{index}"
    os.mkdir(directory)
    init_py = open(f"{directory}/__init__.py", "x")
    init_py.close()
    main_py = open(f"{directory}/{base_file_name}.py", "x")
    main_py.close()


def create_test_exercise_items(index: int, base_file_name: str) -> None:
    directory = f"./tests/test_exercise{index}"
    os.mkdir(directory)
    main_py = open(f"{directory}/test_{base_file_name}.py", "x")
    main_py.close()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run to create exercises and test files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--index",
        "-i",
        type=int,
        help="Creates exercise of that index. Fails if already exists.",
    )
    parser.add_argument("name", type=str, help="Base file name for next exercise.")

    args = parser.parse_args()

    index = args.index
    if index is None:
        with open(EXERCISE_CONFIGS_PATH, "r+") as configs_file:
            configs = json.loads(configs_file.read())
            assert "next_exercise_index" in configs
            index = configs["next_exercise_index"]
            configs["next_exercise_index"] = index + 1
            configs_file.seek(0)
            configs_file.truncate()
            configs_file.write(json.dumps(configs, indent=2))

    create_exercise_items(index, args.name)
    create_test_exercise_items(index, args.name)

    print(f"Exercise {index}, {args.name}, and test folder created.")


if __name__ == "__main__":
    main()
