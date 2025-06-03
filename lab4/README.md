# Версионированние данных DVC
lab4 демонстрирует использование DVC (Data Version Control) для отслеживания изменений в наборе данных Titanic и сохоранении его в отдельном хранилище, т.к. хранить данные на **git** может быть проблематично при большом объеме

# Ссылка на google drive
[Google Drive](https://drive.google.com/drive/folders/14BqriGp0xzr83qK3r5Kw5A7FJ2aBk2_s?usp=sharing) на который сохранялись версии
* Доступ к хранилищу осуществлялся при помощи сервисного ключа
```
gdrive_service_account_json_file_path = key.json
```
# Структура работы
* lab4/** - корневая директория
* titanic.csv - набор данных, подвергавшийся изменениями и версионированию (не сохраняетя в git)
* Скрипты *.py - используются для создания и изменения набора данных
* titanic.csv.dvc - мета-данные текущего состояния датасета
* dvc_logs.txt - логи коммитов dvc
* git_logs.txt - логи коммитов git

# Алогритм использования dvc
1. Изменение данных;
2. dvc add /измененные данные;
3. git add /мета-данные набора данных;
4. dvc push;
5. git commit;


# Обработка данных
Были выполнены следующие шаги обработки данных, каждый из которых зафиксирован как отдельная версия с помощью Git и DVC:
- Загрузка данных:

  Действие: из библиотеки sns был загружен набор данных titanic
  
  Скрипт: load_data.py
  
  Лог коммита: 
  ```
  commit 4c9e184c0655175f30f9f529aaefca8b521da02d
      Initial data
  diff --git a/lab4/titanic.csv.dvc b/lab4/titanic.csv.dvc
  new file mode 100644
  index 0000000..83a6baa
  --- /dev/null
  +++ b/lab4/titanic.csv.dvc
  @@ -0,0 +1,5 @@
  +outs:
  +- md5: 6a7a2ed01936ef56e903ba2bb2f6fbc6
  +  size: 57910
  +  hash: md5
  +  path: titanic.csv
  ```

- Удаление признаков:

  Действие: из набора данных были удалены признаки "embarked" и "embark_town"
  
  Скрипт: first_modification.py
  
  Лог коммита: 
  ```
  commit 4568369ff75bd7ac9633a3b52f1a33252c0b9978
      first modification
   diff --git a/lab4/titanic.csv.dvc b/lab4/titanic.csv.dvc
  index 83a6baa..f12eb34 100644
  --- a/lab4/titanic.csv.dvc
  +++ b/lab4/titanic.csv.dvc
  @@ -1,5 +1,5 @@
   outs:
  -- md5: 6a7a2ed01936ef56e903ba2bb2f6fbc6
  -  size: 57910
  +- md5: 0d42d12f22afa8d2f85fbc7fa7cc50b4
  +  size: 45852
     hash: md5
     path: titanic.csv
  ```

- Заполнение признаков:

  Действие: числовые признаки были заполнены медианным значением
  
  Скрипт: second_modification.py
  
  Лог коммита: 
  ```
  commit 9f8f5867c7a5b92a09c19973a413400ef371d558
      second modification
  diff --git a/lab4/titanic.csv.dvc b/lab4/titanic.csv.dvc
  index f12eb34..7f66f04 100644
  --- a/lab4/titanic.csv.dvc
  +++ b/lab4/titanic.csv.dvc
  @@ -1,5 +1,5 @@
   outs:
  -- md5: 0d42d12f22afa8d2f85fbc7fa7cc50b4
  -  size: 45852
  +- md5: 10ef4ae9645fffd98d2d4bc3e80cba81
  +  size: 53688
     hash: md5
     path: titanic.csv
  ```

- Кодирование категориальных признаков:

  Действие: кодирование признаков "sex" и "class"
  
  Скрипт: third_modification.py
  
  Лог коммита: 
  ```
  commit 7aebd4033ff48f5ddecef409189022606c1b7b43
      Final change
  diff --git a/lab4/titanic.csv.dvc b/lab4/titanic.csv.dvc
  index 7f66f04..47e6536 100644
  --- a/lab4/titanic.csv.dvc
  +++ b/lab4/titanic.csv.dvc
  @@ -1,5 +1,5 @@
   outs:
  -- md5: 10ef4ae9645fffd98d2d4bc3e80cba81
  -  size: 53688
  +- md5: 33de64d20d893132ab225004b30f8c15
  +  size: 53791
     hash: md5
     path: titanic.csv
  ```

# Переключение между версиями

Чтобы переключиться между различными версиями данных, использовались команды Git и DVC:

``` bash
# Переключиться на коммит с исходными данными
git checkout 4c9e184
dvc pull

# Переключиться на коммит с удаленными "embarked" и "embark_town"
git checkout 4568369 
dvc pull

# Переключиться на коммит с заполненными числовыми пропусками
git checkout 9f8f586  
dvc pull

# Переключиться на последнюю версию с One-Hot Encoding
git checkout 7aebd40
dvc pull
```


