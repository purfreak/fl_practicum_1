## Постановка задачи:
Даны α, буква x и натуральное число k. Вывести, есть ли в языке L слова,
содержащие кратное k число букв x.

## Описание алгоритма, решающего эту задачу:
Будем посимвольно обрабатывать регулярное выражение, записанное в обратной польской записи, используя стек (в нашем случае список) для хранения операнд, к которым потом будут применяться операции. Вместо букв и выражений мы будем хранить множества, которые будут символизировать остатки от деления количества букв x в подслове, которое мы рассматриваем. Используем множества потому, что порядок перечисления остатков не важен, и при этом очень удобно избавляться от повторов.

### Для каждого символа регулярного выражения может быть несколько различных случаев:
символ может быть:
- буквой x
- какой-либо буквой алфавита, не являющейся буквой x
- пустым словом
- оператором + (оператором OR)
- оператором * (оператором REPEAT)
- оператором . (оператором CONCAT)

Если символ - буква x, мы добавляем на стек множество {1}, так как из выражения мы умеем получать только подслово с количеством букв x, равным 1.

Если символ - какая-либо другая буква алфавита или пустое слово, мы добавляем на стек множество {0}, так как эти символы никак не влияют на количество букв x в слове.

Если символ - оператор OR, то результатом применения этого оператора к двум операндам-множествам будет их объединение, так как мы можем получить все варианты остатков.

Если символ - оператор CONCAT, то результатом применения этого оператора к двум операндам-множествам будет множество, строящееся следующим образом: к каждому остатку из первого множества прибавляется каждый остаток из второго множества.

Если символ - оператор REPEAT, то результатом применения этого оператора к операнду-множеству будет множество, строящееся следующим образом: фактически мы конкатенируем строку саму с собой до тех пор, пока результат от предыдущей конкатенации не совпадет с результатом от текущей.

В конце на стеке остается одно множество (если регулярное выражение было корректным), тогда если в этом множестве есть элемент 0, то ответом будет YES, так как это будет значить, что мы умеем получать слово, количество букв x в котором кратно k.
