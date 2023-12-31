from enum import Enum

class MessageType(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERR = "ERR"

class Logger:
    def __init__(self):
        self.file = open('log.txt', "a")

    def __del__(self):
        """
        Close the file stream on deletion of Logger object
        """
        self.file.close()

    def log(self, msg: str, type: MessageType = "INFO", write_only = False) -> None:
        """


        Parameters:
            msg (str): 
            type (MessageType): 

        Returns:
            None

        Example:
            
        """
        msg = f"[{str(MessageType(type.upper())).replace('MessageType.', '')}] - {msg}"

        if not write_only:
            print(msg)

        self.file.write(msg + '\n')
