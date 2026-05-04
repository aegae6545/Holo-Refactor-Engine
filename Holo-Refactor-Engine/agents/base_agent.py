import abc
import logging
from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("HoloRefactor")

class BaseAgent(abc.ABC):
    def __init__(self, name):
        self.name = name
        self.config = Config()

    def log(self, message):
        logger.info(f"[{self.name}] {message}")

    @abc.abstractmethod
    async def run(self, input_data):
        pass