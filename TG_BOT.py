import random
import webbrowser

def hi(): # ПРИВЕТСТВИЕ
    print()
    print()
    print()
    print(' ' * 40, 'ВАС ПРИВЕТСТВУЕТ АВТОМАТИЗИРОВАННЫЙ')
    print(' ' * 47, 'БоТ-Imperia Pizza!!!')
    name = input('Введите ваше имя: ')
    print('-' * 104)
    print(' ' * 35, f'ДОБРО ПОЖАЛОВАТЬ В IMPERIA PIZZA, {name}!!!')
    return name

def commands(): # КОМАНДЫ
    print('-' * 104)
    print(' ' * 44, '<-> СПИСОК КОМАНД <->')
    print()
    print(' ' * 14, '/start, /stop, /help, /menu, /price, /weight, /buy, /rebuy, /basket, /check, /url')
    print('-' * 104)

def start(): # ЗАПУСК
    print('-' * 104)
    print('Бот-Imperia Pizza начал свою работу...')

def stop(): # СТОП
    print('-' * 104)
    print('Бот-Imperia Pizza остановил свою работу.')
    print()
    print(f'P.S. Обращайтесь ещё {name}, будем рады! :)')
    print()

def menu(): # МЕНЮ
    print('-' * 104)
    print(' ' * 40, '<-  СПИСОК ПИЦЦ  ->')
    print()
    list = ['->  4 Сыра', '->  Барбекю', '->  Вегетарианская',
     '->  Гасконская', '->  Детская', '->  Итальянка',
     '->  Мексиканка', '->  Пепперони']
    for i in list:
        print(' ' * 42, i)
    print('-' * 104)

def price(): # ПРАЙС
    print('-' * 104)
    print(' ' * 42, '<-  ЦЕНЫ  ->')
    print()
    list = ['4 Сыра = 588 cом', 'Барбекю = 488 cом', 'Вегетарианская = 438 cом', 
    'Гасконская = 498 cом', 'Детская = 438 cом', 'Итальянка = 598 cом', 
    'Мексиканка = 478 cом', 'Пепперони = 408 cом']
    for i in list:
        print(' ' * 40, i)
    print('-' * 104)

def weight(): # ВЕС
    print('-' * 104)
    print(' ' * 42, '<-  ВЕС  ->')
    print()
    list = ['4 Сыра = 560 г', 'Барбекю = 520 г', 'Вегетарианская = 500 г', 
    'Гасконская = 740 г', 'Детская = 650 г', 'Итальянка = 720 г', 
    'Мексиканка = 640 г', 'Пепперони = 570 г']
    for i in list:
        print(' ' * 40, i)
    print('-' * 104)

def help(): # ПОМОЩНИК
    print('-' * 104)
    print(' ' * 40, '<- ПОМОЩНИК В КОМАНДАХ ->')
    print()
    list = ['/start -> запускает бот', '/stop -> останавливает бот', 
    '/help -> помощник в командах', '/menu -> выводит меню', 
    '/price -> показывает цены', '/weight -> указывает вес', '/buy -> оформить заказ',
    '/rebuy -> переоформить заказ', '/basket -> корзина', '/check -> чек(квитанция)', '/url -> ОТКРЫВАЕТ ОФФ САЙТ']
    for i in list:
        print(' ' * 40, i)
    print('-' * 104)

def buy(): # ЗАКАЗ
    print('-' * 104)
    arr = []
    count = int(input('Сколько пицц вы хотите заказать: '))
    print()
    print('Введите название товара: ')
    for i in range(count):
        i = input(f'{i + 1}. ')
        arr.append(i)
    print()
    print(f'{name}, ваш заказ добавлен в корзину...')
    print('-' * 104)
    return arr
    
def rebuy(): # ПЕРЕОФОРМЛЕНИЕ ЗАКАЗА
    print('-' * 104)
    print(' ' * 45, '<- ТЕКУЩИЙ ЗАКАЗ ->')
    print()
    count = 1
    i = 0
    while i <= len(buy_list) - 1:
        print(' ' * 45, f'{count}. {buy_list[i]}')
        i += 1
        count += 1
    print('-' * 104)
    print()
    bool_food = input('Вы хотите удалить или добавить товар к заказу? : ')
    if bool_food == 'удалить':
        size = int(input('Какое количество позиции нужно удалить: '))
        print('Введите название: ')
        for i in range(size):
            i = input(f'{i + 1}. ')
            buy_list.remove(i)
    elif bool_food == 'добавить':
        size2 = int(input('Какое количество позиции нужно добавить: '))
        print('Введите название: ')
        for i in range(size2):
            i = input(f'{i + 1}. ')
            buy_list.append(i)
    print()
    print(f'{name}, Ваш заказ успешно переоформлен...')
    print('-' * 104)

def basket(): # КОРЗИНА
    print('-' * 104)
    print(' ' * 45, '<- КОРЗИНА ->')
    print()
    count = 1
    i = 0
    while i <= len(buy_list) - 1:
        print(' ' * 45, f'{count}. {buy_list[i]}')
        i += 1
        count += 1
    print('-' * 104)

def check(): # КВИТАНЦИЯ
    dic = {
        '4 Сыра' : 588,
        'Барбекю' : 488,
        'Вегетарианская' : 438,
        'Гасконская' : 498,
        'Детская' : 438,
        'Итальянка' : 598,
        'Мексиканка' : 478,
        'Пепперони' : 408
    }

    check_num = (random.randint(1, 100))
    trans = 200
    sum = 0

    for i,j in dic.items():
        for k in buy_list:
            if k == i: sum += j
    
    print('-' * 104)
    print(' ' * 35, '<- ТЕКУЩИЙ СПИСОК ЗАКАЗАННОГО ТОВАРА ->')
    print()

    count = 1
    i = 0

    while i <= len(buy_list) - 1:
        print(' ' * 45, f'{count}. {buy_list[i]}')
        i += 1
        count += 1
    print()
    print(f'Общая сумма оплаты: {sum} сом')
    print('-' * 104)
    print()
    check_num = (random.randint(1, 100))
    print('IMPERIA PIZZA предлагает Вам доставку заказа!!!')
    print('Доставка по городу стоит 200 сом!')
    delivery = input(f'{name}, Вам оформить заказ с доставкой? -> ')
    if delivery == 'Да': print(f'Общая сумма с доставкой, составляет: {trans + sum} сом')
    elif delivery =='Нет': print(f'Общая сумма оплаты: {sum} сом')
    res = input('Подтвердить заказ с доставкой? -> ')
    if res == 'Нет': 
        print('-' * 104)
        print(' ' * 45, 'ЗАКАЗ УСПЕШНО ПРИНЯТ!')
        print('-' * 104)
        print(' ' * 30, f'Общая сумма оплаты: {sum} сом')
        print(' ' * 30, f'Ваш индивидуальный номер чека №{check_num}')
        print(' ' * 30, 'Вы можете забрать заказ по адресу "пер.Магнитогорский, дом 16, г.Бишкек"')
        print(' ' * 30, f'IMPERIA PIZZA благодарит Вас за покупку!!! {name} ждём Вас снова!!!')
        print('-' * 104)
    elif res == 'Да':
        addres = input('Укажите адрес доставки: ')
        print('-' * 104)
        print(' ' * 45, 'ЗАКАЗ УСПЕШНО ПРИНЯТ!')
        print('-' * 104)
        print(' ' * 30, f'Общая сумма оплаты: {sum + trans} сом')
        print(' ' * 30, f'Ваш индивидуальный номер чека №{check_num}')
        print(' ' * 30, f'Будет доставлено в течении часа, по адресу {addres}')
        print(' ' * 30, f'IMPERIA PIZZA благодарит Вас за покупку!!! {name} ждём Вас снова!!!')
        print('-' * 104)

def url(): # ОФФ САЙТ
    webbrowser.open_new_tab('https://mypizza.kg/ru/mypizza/menu/4358/')

name = hi()

while True: # зациклическая команда (бессконечный цикл) (ТЕЛО БОТА)
    commands()
    command = input(f'{name}, введите команду: ')
    if command == '/start': start()
    elif command == '/stop': 
        stop()
        break
    elif command == '/help': help()
    elif command == '/menu': menu()
    elif command == '/price': price()
    elif command == '/weight': weight()
    elif command == '/buy': buy_list = buy()
    elif command == '/rebuy': rebuy()
    elif command == '/basket': basket()
    elif command == '/check' : check()
    elif command == '/url' : url()
    else: print(f'Неопознанная команда!!! {name}, изучите инструкцию через /help')

