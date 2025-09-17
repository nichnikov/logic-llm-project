# main.py

from prompts import PROMPT_TEMPLATE
from llm_translator import generate_code_from_puzzle, execute_solver_code

def main():
    # 1. Загрузка задачи на естественном языке из файла
    with open("puzzle.txt", "r", encoding="utf-8") as f:
        puzzle_text = f.read()
    
    print("--- 1. Исходная задача ---")
    print(puzzle_text)
    print("-" * 30)

    # 2. Генерация Python-кода с помощью симуляции LLM
    generated_code = generate_code_from_puzzle(puzzle_text, PROMPT_TEMPLATE)
    
    print("--- 2. Сгенерированный LLM код (для Z3) ---")
    print(generated_code)
    print("-" * 30)
    
    # Сохраняем сгенерированный код для проверки
    with open("generated_solver_code.py", "w", encoding="utf-8") as f:
        f.write(generated_code)
        
    # 3. Выполнение сгенерированного кода и получение результата
    print("--- 3. Результат выполнения кода солвером ---")
    solution = execute_solver_code(generated_code)
    print(solution)
    print("-" * 30)

if __name__ == "__main__":
    main()