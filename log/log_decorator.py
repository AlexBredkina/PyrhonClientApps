import logging


logger = logging.getLogger('DECORAT_LOG')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

fh = logging.FileHandler("declog.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)


# Добавляем в логгер новый обработчик событий и устанавливаем уровень логгирования
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаём потоковый обработчик логгирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    # В логгирование передаем имя текущей функции и имя вызвавшей функции
    logger.info('Тестовый запуск логгирования')