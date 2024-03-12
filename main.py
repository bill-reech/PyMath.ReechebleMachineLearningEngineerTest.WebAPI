from reecheble_finance.domain.utilities.logger import LogManager
from reecheble_finance.distribution.api import AppManager


logger = LogManager().logger


def main():
    logger.info('Starting microservice...')

    # Start API
    app_manager = AppManager()
    app_manager.start()

    logger.info("Microservice stopped")


if __name__ == '__main__':
    main()
