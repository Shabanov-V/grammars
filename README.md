# Инструкция

Используется python3

Для запуска тестов выполнить python tests.py. Примерное время выполнения 2 часа. 1:40 на первый алгоритм, 0:20 на второй

Для ввода своих файлов в первый алгоритм выполнить: 

python -c "import main; print (main.solver('path/graph.dot', 'path/grammar'))" > output.txt

Например, для выполнения первого теста

python -c "import main; print (main.solver('data/skos.dot', 'data/grammar1CNF'))" > t.txt

Для ввода своих файлов во второй алгоритм выполнить: 

python -c "import main; print (main.algo2('path/graph.dot', 'path/grammar'))" > output.txt

Например, для выполнения первого теста

python -c "import main; print (main.algo2('data/skos.dot', 'data/grammar1CNF'))" > t.txt
