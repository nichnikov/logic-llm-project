
#### `llm_translator.py` Этот модуль имитирует вызов LLM и безопасно выполняет сгенерированный код.
# llm_translator.py

import sys
from io import StringIO

def generate_code_from_puzzle(puzzle_text: str, prompt_template: str) -> str:
    """
    Имитирует вызов LLM для генерации кода.
    В реальном приложении здесь был бы API-запрос к OpenAI, Google AI и т.д.
    """
    # Полный промпт для LLM
    full_prompt = prompt_template.format(puzzle=puzzle_text)
    print("--- Отправка промпта в LLM (симуляция) ---\n")
    # print(full_prompt) # Раскомментируйте, чтобы увидеть полный промпт

    # --- СИМУЛЯЦИЯ ОТВЕТА LLM ---
    # Это тот код, который мы ожидаем получить от хорошо обученной LLM
    # на основе нашего промпта.
    generated_code = """
from z3 import *

# 1. Создание булевых переменных для каждого подозреваемого
alexey = Bool('Алексей')
boris = Bool('Борис')
victor = Bool('Виктор')

# 2. Создание экземпляра солвера
s = Solver()

# 3. Перевод условий в логические выражения Z3

# Условие 1: Если Алексей виновен, то у него был один сообщник.
# (один сообщник означает, что либо Борис виновен, либо Виктор, но не оба)
s.add(Implies(alexey, Xor(boris, victor)))

# Условие 2: Если Борис виновен, то Виктор не виновен.
s.add(Implies(boris, Not(victor)))

# Условие 3: Алексей и Борис не могли совершить преступление вместе.
s.add(Not(And(alexey, boris)))

# Условие 4: По крайней мере один из них виновен.
s.add(Or(alexey, boris, victor))

# 4. Проверка и вывод решения
if s.check() == sat:
    m = s.model()
    print("Решение найдено. Виновные:")
    guilty_suspects = []
    for d in m.decls():
        if is_true(m[d]):
            guilty_suspects.append(d.name())
    
    if guilty_suspects:
        for suspect in guilty_suspects:
            print(f"- {suspect}")
    else:
        # Этот случай не должен произойти при данных условиях
        print("Виновных нет, но модель найдена (противоречие в логике).")

else:
    print("Решение не найдено. Условия противоречивы.")

    return generated_code.strip()
"""

def execute_solver_code(code: str) -> str:
    """
    Безопасно выполняет сгенерированный код и возвращает его вывод.
    """
    # Сохраняем оригинальный stdout
    original_stdout = sys.stdout
    # Перенаправляем stdout в строку
    sys.stdout = new_stdout = StringIO()
    
    try:
        # Выполняем код. globals() предоставляет глобальную область видимости.
        exec(code, globals())
    except Exception as e:
        # В случае ошибки выполнения кода, возвращаем сообщение об ошибке
        sys.stdout = original_stdout  # Восстанавливаем stdout
        return f"Ошибка при выполнении сгенерированного кода: {e}"
    finally:
        # Убеждаемся, что stdout всегда восстанавливается
        sys.stdout = original_stdout
        
    # Возвращаем захваченный вывод
    return new_stdout.getvalue()