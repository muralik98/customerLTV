import logging 
import os
from datetime import datetime

def writeLog(file_name, message): 
    
    log_file=f"{file_name}.log"
    log_path=os.path.join(os.getcwd(), "logs",file_name )
                          
    os.makedirs(log_path,exist_ok=True)
    log_file_path=os.path.join(log_path, log_file)  
                          
    logging.basicConfig(filename=log_file_path,format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)   # Kind of logger function definition 
    
    logging.info(message)  # Actaully writes logs 



