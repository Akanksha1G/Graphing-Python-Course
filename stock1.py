import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
# quandl api explore
import quandl
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = "3EqmDkmVfcBhx79FTSbd"
end = datetime.now()
start = end - timedelta(days=20)

mydata2 = quandl.get('FSE/VOW3_X', start_date = start, end_date = end)
f = mydata2.reset_index()

plt.figure(1)
f = pd.Series(f.Close.values,f.Date)
f.plot()
plt.show()