## Структура тестов

Тесты зеркалируют структуру каталога `tasks`. Для каждой задачи создавайте соответствующую иерархию директорий внутри `tests` и файл `test_solution.py` рядом.

Пример:
```
tasks/
  data_stuctures/
    tasks_list/
      task.md
      solution.py

tests/
  data_stuctures/
    tasks_list/
      test_solution.py
```

Импорт из тестов:
```python
from tasks.data_stuctures.tasks_list.solution import solution

def test_example():
    assert callable(solution)
```

Запуск:
```
pytest -q
```


