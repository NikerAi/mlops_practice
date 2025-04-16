# Отчет по лабораторной работе №4 "Версионирование датасетов"

**!Изменения датасета производились исключительно для наличия факта изменения данных!**

[Ссылка на Google Drive](https://drive.google.com/drive/folders/1viWbEFGHz-Qufv7V0EX6EyLtxoqHzYF4) на который сохранялись версии
* Доступ к хранилищу осуществлялся при помощи сервисного ключа
```
gdrive_service_account_json_file_path = key.json
```

## Изменение версий
Для подгрузки соответствующих версий данных использовалась следующая команда:
```
git checkout HEAD^1
dvc pull
```

Также можно было использовть commit id
- ﻿3bd4db9 Dataset_v3
- 1cd7287 Dataset_v2
- 767df0f Configure dvc

Чтобы вернуться на актуальную версию использовалась команда:
```
git checkout lab4
dvc pull
```
