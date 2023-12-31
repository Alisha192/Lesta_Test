def Lesta_is_Even(num: int) -> bool:
    return num % 2 == 0
### Плюсы реализации 1:
- Читаемость и понятность: Использование оператора остатка от деления делает функцию более понятной для большинства читателей, поскольку это стандартный подход к определению четности числа.
- Естественность: Для большинства программистов подход с использованием оператора остатка от деления является более естественным и привычным способом определения четности числа.

### Минусы реализации 1:
- Сниженная производительность: В случае больших чисел нахождение остатка от деления может быть производительно более накладным, чем использование битовой операции "И".



def my_is_Even(num: int) -> bool:
    return num & 1 == 0

### Плюсы реализации 2:
- Высокая производительность: Битовые операции имеют быстрое выполнение на уровне процессора, что обеспечивает высокую производительность функции.
- Простота: Использование битовой операции "И" позволяет коротко и ясно выразить логику определения четности числа.

### Минусы реализации 2:
- Сложность понимания: Для людей, не имеющих опыта работы с битовыми операциями, может потребоваться дополнительное время для понимания и анализа данной реализации.


### Заключение:
Обе реализации обеспечивают функциональную аналогию определения четности числа, но обладают различными характеристиками. Реализация с использованием битовой операции "И" обеспечивает высокую производительность на уровне процессора, но может быть менее понятной для некоторых читателей. В то время как реализация с использованием оператора остатка от деления обеспечивает более естественное и понятное обозначение четности числа, но может обладать сниженной производительностью для больших чисел.
