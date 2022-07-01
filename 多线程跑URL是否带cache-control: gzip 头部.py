# 多线程跑URL是否带gzip缓存数据

import os, sys
import time, threading
import subprocess
from queue import Queue

import logging
logging.basicConfig(level=logging.WARNING,
                    filename='./log.txt',
                    filemode='w',
                    format='%(message)s')

domain = "https://adsfs.abc.com"


def combine_full_url(path):
    return domain + '/' +  path


def check_url_whether_gzip(path):
    full_path = path

    cmd = "curl -I \"%(full_path)s\" --compressed" % {"full_path": full_path}

    res = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    print(res)

    if str(res).__contains__('gzip'):
        return full_path
    else:
        return None


def read_url_file_as_list():
    # data/URLS
    # r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\data\URLS'
    with open(r'data/URLS', 'r') as file:
        list_path = [line.rstrip('\n') for line in file]

        # [{'index':0, 'path': item}]
        list_path_return = []

        for index in range(len(list_path)):
            # print(index, list_path[index])
            list_path_return.append({'index': index, 'path': list_path[index]})

        return list_path_return

# queue取出数据取出
def q_get_data_deal_with(q, write_file_path):

    with open(write_file_path, 'a+', encoding='utf-8') as f:

        while not q.empty():
            path_kv = q.get()
            print(path_kv["path"])
            full_url = combine_full_url(path_kv["path"])
            index_url = path_kv["index"]

            if index_url >= 276:  # 19415

                try:
                    full_path = check_url_whether_gzip(full_url)
                    if full_path:
                        print(full_path, file=f)
                        print(full_path, "带gzip")
                        os.system("echo %(full_path)s >> 带gzip.txt" % ({"full_path": full_path}))
                        logging.log(logging.ERROR, full_path)

                    else:
                        print("%(index)d 没有结果" % {"index": index_url})
                except Exception as e:
                    pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url_list = read_url_file_as_list()

    # 创建queue
    q = Queue(42160)

    for item in url_list:
        q.put(item)

    t1 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result01'))
    t2 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result02'))
    t3 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result03'))
    t4 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result04'))
    t5 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result05'))
    t6 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result06'))
    t7 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result07'))
    t8 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result08'))
    t9 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result09'))
    t10 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result10'))

    t11 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result11'))
    t12 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result12'))
    t13 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result13'))
    t14 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result14'))
    t15 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result15'))
    t16 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result16'))
    t17 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result17'))
    t18 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result18'))
    t19 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result19'))
    t20 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result20'))


    t21 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result21'))
    t22 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result22'))
    t23 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result23'))
    t24 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result24'))
    t25 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result25'))
    t26 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result26'))
    t27 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result27'))
    t28 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result28'))
    t29 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result29'))
    t30 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result30'))

    t31 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result31'))
    t32 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result32'))
    t33 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result33'))
    t34 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result34'))
    t35 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result35'))
    t36 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result36'))
    t37 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result37'))
    t38 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result38'))
    t39 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result39'))
    t40 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result40'))

    t41 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result41'))
    t42 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result42'))
    t43 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result43'))
    t44 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result44'))
    t45 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result45'))
    t46 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result46'))
    t47 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result47'))
    t48 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result48'))
    t49 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result49'))
    t50 = threading.Thread(target=q_get_data_deal_with, args=(q, r'D:\Users\80361576.ADC\PycharmProjects\pythonProject2\result_dir\result50'))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()

    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()

    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()

    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()









