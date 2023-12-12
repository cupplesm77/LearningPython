# mylog.txt
import logging


mode = "development"
log_file = "mylog.txt"
log_format = "%(levelname)s - On %(day)s, I'm taking my %(species)s to %(destination)s"

# This "with" line resets the log file to be empty,
# each time you run the test:
with open(log_file, 'w'): pass



if mode == "production":
    log_level = logging.DEBUG
    log_mode = "w"
else:
    log_level = logging.INFO
    log_mode = "a"
logging.basicConfig(level=log_level,
                    filename=log_file,
                    filemode=log_mode
                    )

def pet_log(pet_dict):
    # print(pet_dict)
    logging.critical(pet_dict["day"],
                     pet_dict["species"],
                     pet_dict["destination"]
                     )


logging.debug("debug message")
logging.warning("look out!")
logging.critical("we have a problem here")

pet_log({ "day": "Tuesday", "species": "dog", "destination": "Central Park"})
