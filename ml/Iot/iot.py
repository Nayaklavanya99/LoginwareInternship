from ubidots import ApiClient
import time
token = "BBUS-VdlMZRqurVtHFGKxT1ZUwIeQSInXjq"

api = ApiClient(token=token)
# data = api.get_variables()
data = api.get_variable("6763f6d5208644415760863d")
data2 = api.get_variable("67640457d79ffe4844f51370")
data.save_value({'value': 99})
i=0
j=20
while True:
    data.save_value({'value': j})
    data2.save_value({'value': i})
    i += 10
    j+=10
    time.sleep(1)
    if i>100:
        i,j=0,0
# data2.save_value({'value': 30})
print(data.get_values(1))
