# goit-algo2-hw-02
# 1. Застосування алгоритму максимального потоку для логістики товарів
Максимальний потік склав **65**

**Таблиця потоків**
| Terminal   | Store     | Actual Flow (units) |
|------------|-----------|---------------------|
| Terminal 1 | Store 1   | 15                  |
| Terminal 1 | Store 2   | 10                  |
| Terminal 1 | Store 4   | 10                  |
| Terminal 1 | Store 7   | 15                  |
| Terminal 2 | Store 10  | 15                  |

**1. Які термінали забезпечують найбільший потік товарів до магазинів?**<br>
**Висновок:**<br>
Термінал 1 забезпечує більший загальний потік товарів до магазинів (загалом 50 одиниць), у порівнянні з Терміналом 2 (15 одиниць).

**2. Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік?**<br>
Найменші пропускні здатності спостерігаються:
Store 13: 5 одиниць
Store 14: 10 одиниць

**3. Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів?**<br>

Магазини з найменшими потоками:
Store 2: 10 одиниць
Store 4: 10 одиниць
Store 10: 15 одиниць

**4. Вузькі місця:**<br>
Склад 4 має багато з'єднань із магазинами з низькими пропускними здатностями, наприклад, Store 13 (5 одиниць) і Store 14 (10 одиниць).
Пропускна здатність від Терміналів до Складів (наприклад, Термінал 2 → Склад 2, 10 одиниць) обмежує можливий потік.

**Рекомендації:**<br>
Збільшити пропускну здатність на вузьких маршрутах, наприклад, між Терміналами та Склади.
Оптимізувати потоки, перенаправивши товари до складів із кращою пропускною здатністю до магазинів.

# 2. Порівняння ефективності OOBTree і словника для діапазонних запитів

Total range_query time for **OOBTree**: *3.629260 seconds*<br>
Total range_query time for **Dict**: *0.749568 seconds*<br>