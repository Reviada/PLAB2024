import json
import sys


def fill_values(test_data, values_dict):
    test_data['value'] = values_dict.get(test_data['id'], "")
    if 'values' in test_data:
        for sub_test in test_data['values']:
            fill_values(sub_test, values_dict)


def fill_report(test_data, values_data):
    values_dict = {value['id']: value['value'] for value in values_data['values']}
    for test in test_data['tests']:
        fill_values(test, values_dict)

    return test_data


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Запустите программу из консоли, например так: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    # Чтение данных из файлов values.json и tests.json
    with open(values_file_path, 'r') as values_file:
        values_data = json.load(values_file)

    with open(tests_file_path, 'r') as tests_file:
        test_data = json.load(tests_file)

    # Формирование отчёта
    report_data = fill_report(test_data, values_data)

    # Запись отчёта в файл report.json
    with open(report_file_path, 'w') as report_file:
        json.dump(report_data, report_file, indent=4)

    print("Отчёт успешно сформирован и сохранён в файл report.json")
