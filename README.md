# Инструкция

Используется python3

Для запуска тестов выполнить python tests.py. Примерное время выполнения 2 часа. 1:40 на первый алгоритм, 0:20 на второй

# Для ввода своих файлов в первый алгоритм выполнить: 

python -c "import main; print (main.algo1('PATH_TO_YOUR_GRAPH', 'PATH_TO_YOUR_GRAMMAR'))" > output.txt

Например, для выполнения первого простого теста

python -c "import main; print (main.algo1('data/simple1.dot', 'data/simple1'))" > t.txt

# Для ввода своих файлов во второй алгоритм выполнить: 

python -c "import main; print (main.algo2('PATH_TO_YOUR_GRAPH', 'PATH_TO_YOUR_GRAMMAR'))" > output.txt

Например, для выполнения второго простого теста

python -c "import main; print (main.algo2('data/simple2.dot', 'data/simple2'))" > t.txt

# Для ввода своих файлов в третий алгоритм выполнить: 

python -c "import main; print (main.algo3('PATH_TO_YOUR_GRAPH', 'PATH_TO_YOUR_GRAMMAR'))" > output.txt

Например, для выполнения четвертого простого теста

python -c "import main; print (main.algo3('data/simple4.dot', 'data/simple4'))" > t.txt
