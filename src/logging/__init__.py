import os
import sys
import logging

log_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
filepath = os.path.join(log_dir,"dev.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO, 
                    format=log_str,
                    handlers=
                    [logging.FileHandler(filepath),
                     logging.StreamHandler(sys.stdout)]
                    )

logger = logging.getLogger("TextSummarizerLogger")
