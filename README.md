# Инструкция

Используется python3

1) git clone git@github.com:Shabanov-V/grammars

2) cd grammars/

# Запуск всех тестов

python -m unittest -v tests.py

# Для ввода своих файлов в матричный алгоритм выполнить: 

python -c "import main; print (main.algo1('PATH_TO_YOUR_GRAPH', 'PATH_TO_YOUR_GRAMMAR'))" > PATH_TO_YOUR_OUTPUT

Например, для выполнения первого теста

python -c "import main; print (main.algo1('data/skos.dot', 'data/grammar1CNF'))" > t.txt

# Для ввода своих файлов в bottom up выполнить: 

python -c "import main; print (main.algo2('PATH_TO_YOUR_GRAPH', 'PATH_TO_YOUR_GRAMMAR'))" > PATH_TO_YOUR_OUTPUT

Например, для выполнения второго простого теста

python -c "import main; print (main.algo2('data/simple4.dot', 'data/simple4'))" > t.txt

# Для ввода своих файлов в top down выполнить: 

python -c "import main; print (main.algo3('PATH_TO_YOUR_GRAPH', 'PATH_TO_YOUR_GRAMMAR'))" > PATH_TO_YOUR_OUTPUT

Например, для выполнения третьего простого теста

python -c "import main; print (main.algo3('data/simple4.dot', 'data/simple4'))" > t.txt
