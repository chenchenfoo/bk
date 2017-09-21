def findResult(testcase):
                for index, item in enumerate(lines):
                #find match testcase in the report and return test result
                        result_list =  testcase.findall(item)
                        for list_item in result_list:
                                result = list_item.split("=")[1].replace("\"","").split()[0]
                                return result
import re
        p = re.compile(r'pass=\"\w+\"')
        for index, item in enumerate(lines):
                result_listP =  p.findall(item)
                for list_item in result_listP:
                        resultP = list_item.split("=")[1].replace("\"","")
