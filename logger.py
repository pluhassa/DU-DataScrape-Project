import logging

logging.basicConfig(level=logging.INFO,filename='app.log', filemode= "w",
                   
            format='%(asctime)s - %(levelname)s - %(message)s')

#custom logger
# logger = logging.getLogger('test_logger')
# file handler
#handler = logging.FileHandler('test.log')
# # # Create a formatter and set it for the handler
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# handler.setFormatter(formatter)
# # # Add the handler to the logger
# logger.addHandler(handler)

#logger.info('This is an info message')