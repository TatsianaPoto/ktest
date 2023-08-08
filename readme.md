Тестовое задание на позицию data scientist engineer

Дано:

Телекоммуникационная компания хочет снизить отток клиентов.
Вы получили набор данных, содержащий записи телефонных разговоров
некоторого количества клиентов.

Два основных бизнес-вопроса, которые необходимо решить с помощью этого набора данных, следующие:

1 Что является причиной оттока клиентов и что мы можем с этим сделать?

2 Как мы можем создать показатель склонности (или вероятность оттока) для каждого клиента?

На собеседовании необходимо представить ответы на эти вопросы, включая соответствующие 
статистические данные и/или визуализацию данных. 
Вас будут спрашивать о том, как вы решали задачу, поэтому не забудьте принести код и т.п., 
который вы использовали.

Dataset:

'churn.all.txt', 'churn.data.txt', 'churn.test.txt' - данные
'churn.names.txt' - наименование колонок

combine_files.py - Скрипт объединяет файлы 'churn.all.txt', 'churn.data.txt', 'churn.test.txt' 
в один файл combined_output.txt и удаляет дублирующие записи.
Т.к. в финальном combined_output.txt 5 тыс записей, можно сделать вывод, что data и test -
это разбитый датасет из файла all