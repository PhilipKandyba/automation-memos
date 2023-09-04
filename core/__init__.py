from faker import Faker
from selenium.webdriver.common.by import By
from core.teardown_queue import TeardownQueue
from core.loggers.core_logger import core_logger

by = By

faker = Faker()

teardown_queue = TeardownQueue()

core_logger = core_logger
