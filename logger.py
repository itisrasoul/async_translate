import os
import logging

def config_logger(log_file):
    if not os.path.exists(os.path.split(log_file)[0]) and os.path.split(log_file)[0] != "":
        os.makedirs(os.path.split(log_file)[0])
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=20, filename=log_file, filemode='a',
                        format="\n\n%(asctime)s   %(levelname)s: %(message)s\n")

def logger(msg, mode='warning'):
    if mode == 'warning':
        logging.warning(msg, exc_info=False)
    elif mode == 'exception':
        logging.exception(msg, exc_info=True)
        print("\n", msg)
    elif mode == 'info':
        logging.info(msg)
        print("\n", msg)