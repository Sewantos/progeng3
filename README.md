## Как решать задания

Этот репозиторий содержит учебные задачи по алгоритмам и структурам данных. Для каждой задачи есть файл описания `task.md`, а рядом с ним следует размещать файл с решением на Python.

### Структура проекта
```
software_engineering_algo_tasks/
  tasks/
    <раздел>/
      <подраздел>/
        task.md            # условие задачи
        solution.py        # ваше решение (этот файл создаёте вы)
  tests/
    <раздел>/
      <подраздел>/
        test_solution.py   # тесты к задаче, структура зеркалирует tasks
  pyproject.toml           # настройки форматтеров/линтеров
  .pre-commit-config.yaml  # автопроверки перед коммитом
```

### Требования
- Python ≥ 3.9
- Рекомендуется использовать Poetry
- Типы: используйте встроенные типы (`list`, `dict`, `set`, `tuple`) вместо `typing.List/Dict/...`

### Минимальный объём заданий
- data_stuctures: выполнить не менее 3 задач
- sorts: выполнить не менее 2 задач
- recursion: выполнить 1 задачу

### Как добавлять решение
1. Откройте нужную задачу в `tasks/.../task.md`.
2. Создайте рядом файл `solution.py` и реализуйте решение.
3. Соблюдайте типы (используйте встроенные `list`, `dict`, и т.д.), документируйте публичные функции краткими докстрингами.

### Как писать тесты
1. В `tests/` создайте зеркальную структуру директорий задачи.
2. Название файла тестов: `test_solution.py` (или другое, начинающееся с `test_`).
3. В тестах импортируйте решение из `tasks/.../solution.py`.

Пример:
```python
from tasks.data_stuctures.tasks_list.solution import solution

def test_basic():
    assert callable(solution)
```

### Быстрый старт (Poetry)
```
poetry install
poetry run pre-commit install

# тесты
make test            # или: poetry run pytest -q

# линтеры/форматирование
make lint-all        # или: poetry run pre-commit run --all-files
```



