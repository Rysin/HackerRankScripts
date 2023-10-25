# input - "India is my country I love india"
# output- India love I country my is India

# string = "India is my country I love india"
#
# _string = string.split(" ")
# _string = _string[::-1]
# print(_string)
# print(" ".join(_string))

var = {
    "1030.3712.3004": {
        "pathIds": {
            "23": {
                "status": "pathFound",
                "details": {
                    "lastUpdatedTime": 8946997.41940961,
                    "refreshRespSeq": 1,
                    "changeCount": 3,
                    "refreshReqSeq": 1,
                },
                "constraint": {"excludeIntf": "Port-Channel2"},
                "sysIds": [{"sysId": "1030.3712.3003", "hostname": "bla1-spn01"}],
            },
            "34": {
                "status": "pathNotFound",
                "details": {
                    "lastUpdatedTime": 8946977.655294351,
                    "refreshRespSeq": 1,
                    "changeCount": 1,
                    "refreshReqSeq": 1,
                },
            },
        }
    }
}


print(var["1030.3712.3004"]["pathIds"]["23"]["status"])

# list_1 = ['Sourabh', 'Vishwajit', 'Amey', 'Jyoti']
#
# # list_1.sort(key=lambda x: x[-1])
# # list_1.sort()
# # print(list_1)
#
# print(list_1[2:])
