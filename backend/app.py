import subprocess
import time
from flask import Flask, jsonify, request
from flask_cors import CORS
from threading import Thread

app = Flask(__name__)
CORS(app)

pipeline_data = {
    "stages": [
        {"name": "Build", "status": "pending", "duration": 0},
        {"name": "Test", "status": "pending", "duration": 0},
        {"name": "Deploy", "status": "pending", "duration": 0}
    ],
    "output": ""  # Поле для хранения результата выполнения кода
}

# Функция для выполнения Python кода
def run_python_script(code):
    try:
        # Эмулируем компиляцию
        pipeline_data["stages"][0]["status"] = "running"
        start_time = time.time()

        # Выполнение кода
        result = subprocess.run(
            ["python", "-c", code],
            check=True,
            capture_output=True,
            text=True
        )
        duration = time.time() - start_time
        pipeline_data["stages"][0]["status"] = "success"
        pipeline_data["stages"][0]["duration"] = round(duration, 4)
        pipeline_data["output"] = result.stdout
    except subprocess.CalledProcessError as e:
        pipeline_data["stages"][0]["status"] = "failure"
        pipeline_data["stages"][0]["duration"] = 0
        pipeline_data["output"] = e.stderr
        return  # Останавливаем процесс, если компиляция не удалась

    # Переход к тестированию
    start_time = time.time()
    run_tests(code)
    pipeline_data["stages"][1]["duration"] = round(time.time() - start_time, 4)

    # Переход к деплою
    time.sleep(1)
    pipeline_data["stages"][2]["status"] = "running"

    start_time = time.time()
    deploy_result = deploy_code(code)
    pipeline_data["stages"][2]["status"] = "success" if deploy_result else "failure"
    pipeline_data["stages"][2]["duration"] = round(time.time() - start_time, 4)
    pipeline_data["output"] += "\n" + deploy_result

def run_tests(code):
    try:
        exec(code, globals())  # Выполняем пользовательский код
        function_name = code.split('def ')[1].split('(')[0]  # Получаем имя функции

        with open('test.txt', 'r') as f:
            lines = f.readlines()

        all_tests_passed = True  # Флаг успешности всех тестов

        for line in lines:
            parts = line.split()
            input_value = int(parts[0])  # Первое значение — входное
            expected_output = list(map(int, parts[1:]))  # Ожидаемые значения — массив

            if function_name in globals():
                actual_output = globals()[function_name](input_value)
            else:
                raise ValueError(f"Function '{function_name}' is not defined.")

            # Адаптивная проверка (скаляр или список)
            if isinstance(actual_output, list) and actual_output == expected_output:
                pipeline_data["output"] += f"\nTest passed for input {input_value}: {actual_output}"
            elif isinstance(actual_output, int) and [actual_output] == expected_output:
                pipeline_data["output"] += f"\nTest passed for input {input_value}: {actual_output}"
            else:
                all_tests_passed = False
                pipeline_data["output"] += (
                    f"\nTest failed for input {input_value}: {actual_output} != {expected_output}"
                )

        # Устанавливаем статус стадии
        pipeline_data["stages"][1]["status"] = "success" if all_tests_passed else "failure"
    except Exception as e:
        pipeline_data["stages"][1]["status"] = "failure"
        pipeline_data["output"] += f"\nTest failed: {e}"


# Функция для деплоя
def deploy_code(code):
    try:
        filename = f"deployed_code_{int(time.time())}.py"
        with open(filename, 'w') as f:
            f.write(code)
        return "Code deployed successfully."
    except Exception as e:
        return f"Deploy failed: {e}"

@app.route('/api/pipeline', methods=['GET'])
def get_pipeline():
    return jsonify(pipeline_data)

@app.route('/api/start_compile', methods=['POST'])
def start_compile():
    code = request.json.get("code")
    if not code:
        return jsonify({"status": "error", "message": "No code provided"}), 400
    thread = Thread(target=run_python_script, args=(code,))
    thread.start()
    return jsonify({"status": "Compilation started"})

if __name__ == "__main__":
    app.run(debug=True)
