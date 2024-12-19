from ubidots import ApiClient
import time

token = "BBUS-VdlMZRqurVtHFGKxT1ZUwIeQSInXjq"

api = ApiClient(token=token)
# data = api.get_variables()
data = api.get_variable("6763f6d5208644415760863d")
data2 = api.get_variable("67640457d79ffe4844f51370")
# data.save_value({"value": 99})
# i = 0
# j = 20

# while True:
#     last_value = data.get_values()
#     print(last_value)


alldata = api.get_variables()
for variable in alldata:
    last_value = variable.get_values(1)
    print(last_value)