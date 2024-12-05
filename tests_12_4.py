import unittest
import logging
import traceback
from runner import Runner  # Импортируем класс Runner

# Настройка базового конфигурационного файла для логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Test Runner", speed=-5)  # Попытаться создать бегуна с отрицательной скоростью.
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.warning(traceback.format_exc())    # Логируем трейсбек для исключения
        else:
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, -5)  # Это должно быть изменено, логика не совсем верная.

    def test_run(self):
        try:
            runner = Runner(123, speed=10)  # Попытаться создать бегуна с неверным типом имени.
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(traceback.format_exc())    # Логируем трейсбек для исключения
        else:
            runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 20)  # Это тоже может быть изменено по логике вашего приложения.

if __name__ == '__main__':
    unittest.main()