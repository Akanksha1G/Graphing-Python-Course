import pandas as pd
import matplotlib.animation as animation
pd.core.common.is_list_like = pd.api.types.is_list_like

import quandl
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

end = datetime.now()
start = end - timedelta(days=15)
def stock(i,start,end):

    quandl.ApiConfig.api_key = "yHmZ_VPcFNq8iyPkyf9w"
    

    mydata2 = quandl.get('FSE/VOW3_X', start_date = start, end_date = end)
    f = mydata2.reset_index()

    plt.figure(1)
    f = pd.Series(f.Close.values,f.Date)
    f.plot()
ani = animation.FuncAnimation(fig, stock, fargs=(start, end), interval=1000)
plt.show()