import json
import pandas as pd
import json

def excel_to_json(excel_file, json_file):
    try:
        # Читаем Excel-файл (первый лист по умолчанию)
        df = pd.read_excel(excel_file, usecols=[0, 1], header=None, dtype=str)  # Приводим все к строкам
        df.columns = ["key", "value"]  # Назначаем имена столбцам
        
        # Преобразуем данные в требуемый формат
        data = {"страница": {}}
        for index, row in df.iterrows():
            key = row["key"]
            if key not in data:
                data[key] = {}
            data[row["key"]] = row["value"]  # Используем значение из ячейки A как ключ
        # Записываем данные в JSON-файл
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Файл {json_file} успешно создан.")
    except Exception as e:
        print(f"Ошибка: {e}")


# Пример использования
excel_file = "номинал.xlsx"  # Укажите свой файл
json_file = "data2.json"
excel_to_json(excel_file, json_file)