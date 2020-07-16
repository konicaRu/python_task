# В этом разделе находяться решения небольших задач которые я решал изучая  Python
![](https://raw.githubusercontent.com/konicaRu/python_task/master/pictures/copy_python.jpg)
## Например:
### Оптимизация беспилотного трафика
Яндекс выпускает на улицы тысячи беспилотных автомобилей, и теперь появляется отличная возможность оптимизации трафика на дорогах.
Прежде всего требуется точно оценить время
прибытия машины в место назначения.
На дороге автомобиль постоянно встречает
светофоры, которые горят либо зелёным, либо
красным. Время горения зелёного и красного
света задаётся в секундах. Цикл переключения
цветов повторяется бесконечно и начинается с
красного цвета.
Так как скорость автомобиля известна,
положения светофоров на дороге определяются
временем, которое требуется, чтобы доехать до
этого светофора из начала дороги при условии,
что все предыдущие светофоры горят зелёным.
Каждый светофор также характеризуется
временем горения красного и зелёного цвета.

**Задача** -- определить, за какое время автомобиль
доберётся до конца дороги.

Например, имеется дорога длиной 10 единиц
времени.

Первый светофор расположен на
отметке 3 единицы времени и характеризуется
циклом 5 красный 5 зелёный. 

Второй светофор
расположен на отметке 5, и время показа
красного и зелёного для него 2 и 2.

Автомобиль стартует, через 3 единицы
добирается до первого светофора, на котором
горит красный. Он горит 5 единиц, то есть
движение начинается с 5-го момента.
Через две единицы автомобиль добирается до
второго светофора -- это абсолютный момент 7. 

В этот момент на светофоре горит зелёный, и
автомобиль проезжает его без остановвки. От
второго светофора до конца дороги остаётся ещё
5 моментов, таким образом суммарное время
автомобиля в пути равно 12 (7 + 5).

Функция
**int Unmanned(int L, int N, int [][3] track)**
получает на вход длину L дороги, количество
светофоров на ней N, и описание самой дороги,
где каждый элемент состоит из трёх значений:
момент времени относительно начала дороги,
когда в него прибудет автомобиль по свободной
дороге, время показа красного света и время
показа зелёного цвета.

Для примера выше параметры функции
**Unmanned()** будут такими: **10, 2, [ [3,5,5], [5,2,2] ]**
Функция возвращает реальное время, требуемое
для преодоления дороги.

## Код решения:
``` 
def Unmanned(L, N, track):    
    color = ''  
    dist_gen = 0    
    gen_count = 0  # общий счетчик ходов
    for k in range(len(track)):  # отрезков действия столько сколько светофоров
        time_light = 0  # счетчик горения светофора? обнуляем при переходе к след светофору
        wait_time = 0  # время ожидания на светофоре
        time_drive = 0
        while True:
            time_drive += 1
            gen_count += 1
            time_light += 1  # сначала загорается красный
            if time_light > track[k][1] + track[k][2]:  # зацикливаем бесконечное горение светоф
                time_light = 1
            if time_light <= track[k][1]:
                color = 'red'  # то горит красный
            if time_light > track[k][1] and time_light <= track[k][1] + track[k][2]:
                color = 'green'
            if color == 'green' and k == 0 and len(track) > 1:
                dist_gen = track[k][0] + wait_time + (track[k + 1][0] - track[k][0])
                break
            if gen_count > track[k][0] and color == 'red' and k == 0:  # k==0 заглушка для работы только на 1 светофоре
                wait_time += 1  # необходимо сделать чтобы было 2
            if time_drive > dist_gen and color == 'red' and k > 0:
                wait_time += 1
            if time_drive >= dist_gen and color == 'green' and k < len(track) - 1:
                dist_gen = dist_gen + wait_time + (track[k + 1][0] - track[k][0])
                break
            if time_drive >= dist_gen and color == 'green' and k == len(track) - 1 and len(track)>1:
                dist_gen = dist_gen + wait_time + (L - track[k][0])
                return dist_gen
            if color == 'green' and len(track) == 1:
                dist_gen = track[k][0] + wait_time + (L - track[k][0])
                return dist_gen
```
                
## Еще пример:
### Автоматизация отчётности о продажах.

Интернет-магазин "Платья и Сумки" быстро расширяется, и
его создатели заинтересованы в подробной аналитической
отчётности о продажах товара. 

К сожалению, первая версия
магазина была сделана очень криво, поэтому данные
хранятся в системе в виде, плохо подходящем для
обработки. 

Так, каждая запись о продаже представляет
собой строку формата

название-товара количество-проданных-штук 
например:  
платье1 5   
сумка32 2   
платье1 1   
сумка23 2   
сумка128 4   
Названия товаров могут повторяться.  
Ваша задача: сгруппировать продажи по названиям
товаров, расположив в результирующем списке товары,
отсортированные по количеству продаж.   Если эти
количества для каких-то товаров совпадут, названия
товаров должны следовать в порядке лексикографического
возрастания.  
Например, вышеприведённый пример преобразуется в
такой результат:  
платье1 6   
сумка128 4   
сумка23 2   
сумка32 2   
**Функция:    
string [] ShopOLAP(int N, string [] items)**             
 
ShopOLAPполучает на вход N >= 2 строк о товарах в
вышеприведённом формате, и выдаёт массив длиной M <=
N, содержащий сводку по продажам в сгруппированном
виде.

## Код решения:
```
def ShopOLAP(N, items):
    res_dic = {}
    res_arr = []
    name_good = ''
    name_dic = ''
    num_good = ''
    count = 0
    for i in range(len(items)):
        for j in range(len(items[i])):#перебираем строку до пробела
            if items[i][j] != ' ':
                name_good += items[i][j]#коктенируем стоки
            if items[i][j] == ' ':#если пробел
                name_dic = name_good#присваеваем строке отдельную переменную
                count += 1#флаг чтобы не задействовать верхний иф
            if count == 1 and '0' <= items[i][j] <= '9':#перебираем после пробела, только цифры
                num_good += items[i][j]#коктенируем стоку
        if name_dic in res_dic: #если строка(ключ) уже есть в словаре плюсуем значение переведенное в инт
            res_dic[name_dic] += int(num_good)
            name_good = ''
            num_good = ''
            count = 0
        if name_dic not in res_dic:#если строки нету в словаре загоняем в словарь
            res_dic[name_dic] = int(num_good)#добавляем новый ключ и значение
            name_good = ''
            num_good = ''
            count = 0
    for key, value in res_dic.items():#загоняем в массив переменные из словаря
        res_arr.append(key)
        res_arr.append(str(value))#преобразовываем значение в строку
    res_arr_1 = []
    sum = ''
    for i in range(0, len(res_arr), 2):#склеиваем строки попарно
        sum += res_arr[i] + ' ' + str(res_arr[i + 1])
        res_arr_1.append(sum)
        sum = ''
    res_arr_1.sort()#сортируем обычно
    res_arr_1.sort(reverse=True, key = lambda x: int(x.rsplit(' ',1)[1]))#сортируем по возрастанию знач массива
    return res_arr_1#по последнему значению в строке
    ```
