import time 
from datetime import datetime 
import click 


def sleep_and_print(seconds): 
    print(f"starting{seconds} sleep :)")
    time.sleep(seconds) 
    print(f"finished {seconds} sleep") 
    return seconds 



start = datetime.now()
print([sleep_and_print(3), sleep_and_print(6)])
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")