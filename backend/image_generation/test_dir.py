import os
import pandas as pd

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])


print(df)


# Задаем относительный путь к папке images относительно расположения main.py
output_dir = "images"
# images = r"test.png"

# Сохраняем изображение в указанной директории
output_path = os.path.join(output_dir, "test.xlsx")

df.to_excel("test.xlsx")


print(output_path)