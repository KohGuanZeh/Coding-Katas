import os
import create_exercise


def test_create_exercise_items() -> None:
    mock_file_name = "base_file_name"
    create_exercise.create_exercise_items(-1, mock_file_name)
    directory = "./exercises/exercise-1"
    assert os.path.exists(directory)
    assert os.path.exists(f"{directory}/__init__.py")
    assert os.path.exists(f"{directory}/{mock_file_name}.py")
    for file in os.listdir(directory):
        os.remove(f"{directory}/{file}")
    os.rmdir(directory)


def test_create_test_exercise_items() -> None:
    mock_file_name = "some_other_name"
    create_exercise.create_test_exercise_items(-1, mock_file_name)
    directory = "./tests/test_exercise-1"
    assert os.path.exists(directory)
    assert os.path.exists(f"{directory}/test_{mock_file_name}.py")
    for file in os.listdir(directory):
        os.remove(f"{directory}/{file}")
    os.rmdir(directory)
