"""
# data =
# Router# show logging
# Syslog logging: enabled
#      Console logging: disabled
#      Monitor logging: level debugging, 266 messages logged.
#      Trap logging: level informational, 266 messages logged.
#      Logging to 192.180.2.238
# SNMP logging: disabled, retransmission after 30 seconds
#     0 messages logged
#
# {
#     "Syslog logging": {
#         "Console logging": "disabled",
#         "Monitor logging": "level informational, 266 messages logged",
#         "Trap logging": "level informational, 266 messages logged",
#         "ip": "192.180.2.238"
#     },
#     "SNMP logging": "disabled, retransmission after 30 seconds"
# }
#
# c = "     "
#
#
# def parse_log(string):
#     # Clean data
#     data_lines = string.split("\n")
#     data_lines = list(filter(None, data_lines))
#     data_lines = list(filter(lambda x: '#' not in x, data_lines))
#     data_lines = list(filter(lambda x: ':' in x, data_lines))
#     # print(data_lines)
#     return data_lines
#
#
# def form_dict(data):
#     data_dict = {}
#
#     for each in data:
#         print(each)
#         print(each.split(":"))
#         k, v = each.split(":")
#         data_dict.update({k: v})
#
#     print(data_dict)
#     return data_dict
#
# def form_dict_2(dict_1):
#     parent_dict = {}
#
#     for k, v in dict_1.items():
#         if "    " not in k:
#             parent_dict.update(k,v)
#
# lines = parse_log(data)
# data = form_dict(lines)
#
# k, v = "Syslog logging: enabled".split(":")
# print(k)
# print(v)


# class myClass:
#     arg = 0
#     def __inti__(self):
#         i = 10
#
# myObj = myClass
# print(myObj.i)

def f1():
    print(1)

def f2():
    print(2)

# res1 = f1() and f2()
res1 = f2() and f1()

# res2 = 0 or "5"
# print(f"res1 : {res1}")
# print(res2)

# def some_exception():
#     try:
#         return "try"
#     except:
#         return 'except'
#     finally:
#         return 'finally'
#
# print(some_exception())

# def foo(char, list_=[]):
#     list_.append(char)
#     print(list_)
#
# foo('test')
# foo('test')
# foo('test')
"""