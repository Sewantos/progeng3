class StackMax:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.max_stack: list[int] = []

    def push(self, x: int) -> None:
        """Добавляет целое число x в стек."""
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self) -> str | None:
        """Удаляет число c вершины стека."""
        if not self.stack:
            return "error"
        self.stack.pop()
        self.max_stack.pop()
        return None

    def get_max(self) -> int | str:
        """Возвращает максимальное число в стеке."""
        if not self.stack:
            return "None"
        return self.max_stack[-1]
