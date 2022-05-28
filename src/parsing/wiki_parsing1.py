import time
import requests
import os.path
from typing import List
from bs4 import BeautifulSoup
from src.maps.tree_map import TreeMap
from validators import url as working_url
import uuid #проверка на то, что ссылка рабочая
import concurrent.futures
WIKI_DOMAIN = "https://ru.wikipedia.org"
WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
PATH = r"/Users/amir/PycharmProjects/inf-practic/src/parsing"

def get_code(url):
    '''
    получаем код страницы из вики по url
    '''
    # из ссылки извлекаем данные
    response = requests.get(url)
    # переводим данные в байт код
    code = response.content
    return code

def create_soup(code):
    '''
    достаем html код
    '''
    soup = BeautifulSoup(code, 'lxml')
    return soup

def get_url(soup):
    '''
    из кода страницы достаем валидные url
    '''
    # поиск по атрибуту и отсеивание лишнего
    new_soup = soup.select('div[class="mw-parser-output"]')
    # список для ссылок
    data = []
    if len(new_soup) == 0:
        return data
    # выбираем из списка ссылки
    links = new_soup[0].findAll('a')
    for elem in links:
        # берем ссылки без тегов
        link = str(elem.get('href'))
        url = ''.join([WIKI_DOMAIN, link])
        # проверка на вики ссылку и что ссылка рабочая
        if '/wiki/' in link and working_url(url):
            data.append(url)
    return data

def get_text(soup, obj):
    '''
    получение текста
    '''
    # создается объект класса
    object = obj()
    # достаем текст со страниц вики с тэгами
    text = soup.find('div', class_ = "mw-parser-output")
    # проверяем, что на странице есть текст
    if text is None:
        return object
    # достаем сам текст
    text = text.text
    # делим этот текст на слова
    words = list(map(lambda s: s.lower().strip(), filter(lambda s: s.isalpha(), text.split())))
    # проходимся по словам
    for elem in words:
        # проверяем на наличие слова в мапе
        if elem in object:
            # увеличиваем кол-во если есть
            object[elem] = object[elem] + 1
        else:
            #добавляем одно если нет
            object[elem] = 1
    return object


def wiki_parser(url:str, path = PATH,  use_map: type = TreeMap) -> List[str]:
    """
    парсим страницу вики
    """
    # директория куда будут записываться папки
    this_path = ''.join([path, '/url'])
    # если папки нет в директории
    if not os.path.exists(this_path):
        # создаем папку
        os.mkdir(this_path)
    # директория для обработанных ссылок
    main_path = ''.join([this_path, '/', uuid.uuid4().hex])
    # если эта ссылка еще не обработана
    if not os.path.exists(main_path):
        # создаем для нее папку
        os.mkdir(main_path)
    # если в папке ссылки нет файла с байт кодом
    if not os.path.exists(''.join([main_path, '/content.xml'])):
        # создаем байт код
        byte_code = get_code(url)
        with open(''.join([main_path, '/content.xml']), 'wb') as file:
            # записываем байт код
            file.write(byte_code)
    else:
        # открываем файл с байт кодом
        with open(''.join([main_path, '/content.xml']), 'rb') as file:
            # достаем байт код
            byte_code = file.read()
    # достаем содержимое по байт коду
    soup = create_soup(byte_code)
    # через мапу обрабатываем слова
    data = get_text(soup, use_map)
    # записываем результат
    data.write(''.join([main_path, '/words.txt']))
    list_of_url = get_url(soup)
    return list_of_url

def get_file(name):
    '''
    достаем слово - перевод
    '''
    with open(name, 'r') as i:
        strochka = i.readline()
        while len(strochka) > 1 :
            # достаем слово - кол-во
            key, value = strochka.split()
            value = int(value)
            yield key, value
            strochka = i.readline()

def two_iterators(name1 , name2):
    '''
    сливаем 2 итератора в один
    '''
    result = []
    a = next(name1, None)
    b = next(name2, None)
    while a is not None and b is not None:
        if a[0] < b[0]:
            result.append(a)
            a = next(name1, None)
        elif a[0] > b[0]:
            result.append(b)
            b = next(name2, None)
        elif a[0] == b[0]:
            # если ключи равны, то складываем и переходим дальше
            result.append((a[0], a[1]+b[1]))
            a = next(name1, None)
            b = next(name2, None)
    while a is not None:
        result.append(a)
        a = next(name1, None)
    while b is not None:
        result.append(b)
        b = next(name2, None)
    return iter(result)

def rec_sort(iters_list):
    '''
    рекурентная сортировка
    '''
    # если один файл
    if len(iters_list) == 1:
        return iters_list[0]
    else:
        # медиана
        med = len(iters_list) // 2
        # рекурсивно разделяем массив итераторов, потом по два сливаем
        return two_iterators(rec_sort(iters_list[:med]),rec_sort(iters_list[med:]))

def merge(path = PATH):
    '''
    мерджим все файлы в один
    '''
    # Директория, где лежат обработанные ссылки
    path = PATH + '/url/'
    # Словарь, где будут все слова
    data = []
    # Достаем список названий всех папок в папке url
    with os.scandir(path) as counts:
        # Проходимся по каждой папке
        for count in counts:
            # Прописываем путь к папке
            file_name = ''.join([path, count.name, '/words.txt'])
            data.append(get_file(file_name))
    # Путь, где будет хранится результат
    path = PATH+'/result.txt'
    # Записываем результат
    result = rec_sort(data)
    with open(path, 'w', encoding='utf8') as i:
        for key, value in result:
            i.write(str(key) + " " + str(value) + "\n")

def multithreading(url:str, path:str, depth = 2):
    '''
    многопоточность
    '''
    # убираем дубликаты множеством)
    list_of_url = set(wiki_parser(url, path))
    list_end = []
    # цикл потоков
    for i in range(depth - 1):
        with concurrent.futures.ThreadPoolExecutor(4) as executor:
            # cписок новых ссылок
            list_of = executor.map(wiki_parser, list_of_url)
            for url_in in list_of:
                list_end += url_in
            # добавляются ссылки и удаляются дубликаты
            list_end = list(set(list_end) - list_of_url)
            list_of_url = list_end
if __name__ == "__main__":
    start = time.time()
    multithreading(WIKI_RANDOM, PATH)
    # wiki_parser(WIKI_RANDOM, "/Users/amir/PycharmProjects/inf-practic")
    print(time.time() - start)
    start = time.time()
    merge()
    print(time.time()- start)
