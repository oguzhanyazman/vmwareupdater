from datetime import datetime
import time




while True:
    tarihzaman = datetime.now()
    aa = tarihzaman.strftime('%H:%M')  # hourly
    print(aa)
    time.sleep(10)
