import logging

from src import Unit4


def test_transactions():
    logging.info("start test transactions...")
    unit4 = Unit4()
    unit4.run()
    logging.info("finished test transactions!")


if __name__ == "__main__":
    test_transactions()
