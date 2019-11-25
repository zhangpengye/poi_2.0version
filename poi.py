#coding=utf-8
from urllib import request
import json

def read_http_data(url, data, header, method):
    jdata = None
    if data is not None:
        jdata = json.dumps(data)                  # 对数据进行JSON格式化编码
        jdata=bytes(jdata,'utf8')       #发送json数据需要添加这句
    requests = request.Request(url, jdata, headers = header)
    requests.get_method = method         # 设置HTTP的访问方式
    requests = request.urlopen(requests)
    return requests.read()


def fetchUrl():
    file = open('url18.txt')
    lines = file.readlines()
    #print(lines)
    aa = []
    with open("result18.txt","a+") as result_txt:
        for line in lines:
            page = 1
            #print(line)
            temp = line.replace('\n','')
            #print(temp)
            #print('1')
            while True:
                #print('2')
                url = temp+ "&page=%s"%page
            
                print(url)
            
                the_page = read_http_data(url, None, {}, lambda:"GET")

                #print(the_page)

                result_json_data = json.loads(str(the_page,  encoding = "utf-8"))  #结果转成json数据
                #print(result_json_data)
                pois = result_json_data["pois"]  #获取pois
                #print("count = %s"%count)
                #print(len(pois))
                for i in range(len(pois)):
                    result_name = pois[i]['name'];
                    result_typecode = pois[i]['typecode']
                    result_address = pois[i]['address']
                    #print(type(result_address))
                    #print(result_address)
                    if len(result_address) != 0:
                    
                        result_address = result_address.replace(',',' ')
                        #print(key)
                        #if ',' in result_address:
                            #result_address.remove(',')
                    #print(result_address)
                    result_location = pois[i]['location']
                    result_tel = pois[i]['tel']
                    if len(result_tel) != 0:
                        result_tel = result_tel.replace(',',' ')
                    result_type = pois[i]['type']
                    result_txt.write("%s , %s , %s , %s , %s , %s , \n"%(result_name,result_typecode,result_address,result_location,result_tel,result_type))
                if int(len(pois)) > 1:
                    page = page + 1
                else:
                    break
    print('suc')
fetchUrl()