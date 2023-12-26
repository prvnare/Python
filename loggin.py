from logging import *;

basicConfig(filename='abc.txt', level=DEBUG, filemode='a', format='%(asctime)s:%(levelname)s :%(message)s : %(name)s',
            datefmt='%d/%m/%Y %I:%M:%S %p %z %Z');
critical('critical message');
error('Error message');
warning('Warn message');
info('info message');
debug('debug message');

try:
    10/0;
except ZeroDivisionError as error:
    exception(error);



# creating custom logger
console_logger = getLogger('custome logger');
console_logger.setLevel(DEBUG);

# creating handler to write logs
console_handler = StreamHandler();
console_handler.setLevel(INFO);

# writes critical logs to the file
file_handler = FileHandler('sample.log', mode='w');
# writes critical logs to the file
file_handler.setLevel(CRITICAL);

# creating formatter
log_formatter = Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt= '%d/%m/%Y');

# adding formatter to the handler
console_handler.setFormatter(log_formatter);
file_handler.setFormatter(log_formatter);

# adding handler to logger , can be added multiple at the same time and logs will be written to the specific handler level
console_logger.addHandler(console_handler);
console_logger.addHandler(file_handler)

console_logger.critical('critical message 1234');
console_logger.error('error message');
console_logger.warning('warning message');
console_logger.info('info message');
console_logger.debug('debug message');


