import logging

logging.basicConfig(
    level=logging.CRITICAL,
)


def log():
    logging.debug('debug')
    logging.info('Info')
    logging.warning('Warning!')
    logging.error('Error')
    logging.critical('Critical error')


def main():
    log()


if __name__ == '__main__':
    main()
