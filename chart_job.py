import  pymongo

client = pymongo.MongoClient('localhost', 27017)
zhipin = client['zhipin']
zhipin_java = zhipin['zhipin_java']
zhipin_python = zhipin['zhipin_python']

from collections import  Counter
from pyecharts import Bar,Line,Pie,Scatter, EffectScatter, Grid
from json import dumps
import  re

#Java岗位
for item in zhipin_java.find({},{'_id':0}).limit(5):
    print(item)
def get_zone():
    '''获取地区'''
    zone_list = []
    real_list = []
    for item in zhipin_java.find():
        text = item['person_info'][3:6]
        zone_list.append(text)
    for i in zone_list:
        j = re.sub(r' \d-', '', i)
        real_list.append(j)
        while '' in real_list:
            real_list.remove('')
    return real_list


def get_pyzone():
    '''获取地区'''
    zone_list = []
    real_list = []
    for item in zhipin_python.find():
        text = item['person_info'][3:6]
        zone_list.append(text)
    for i in zone_list:
        j = re.sub(r' \d-', '', i)
        real_list.append(j)
        while '' in real_list:
            real_list.remove('')
    return real_list



from collections import Counter
zone = dict(Counter(get_zone()))
print(zone)

def get_job():
    '''获取岗位情况'''
    job_list = []
    for i in zhipin_java.find():
        job = i['job_title']
        job_list.append(job)
    return dict(Counter(job_list))


job_dict = get_job()

def del_key_1():
    '''删除招聘次数为1的岗位'''
    li = []
    for key in job_dict.keys():
        if job_dict[key] == 1:
            li.append(key)
    for i in li:
        del job_dict[i]
    print(job_dict)

del_key_1()

bar = Bar("java岗位情况", "来自：Python绿洲")
bar.add("岗位", list(key for key in job_dict.keys()), list(value for value in job_dict.values()),mark_line=['min', 'max'], xaxis_interval=5,xaxis_rotate=10,is_toolbox_show = True,is_more_utils=True)
bar


from pyecharts import Pie
pie = Pie("java岗位占比", "来自：chengfei",title_pos='center' )
pie.add("岗位", list(key for key in job_dict.keys()), list(value for value in job_dict.values()),radius=[40, 75],is_random=True,is_label_show=True)
pie.use_theme("dark")
pie


def get_company():
    '''获取公司情况'''
    com_list = []
    for i in zhipin_java.find():
        com = i['company']
        com_list.append(com)
    return dict(Counter(com_list))

com_list = get_company()


def del_com():
    '''删除招聘次数小于2的公司'''
    li = []
    for key in com_list.keys():
        if com_list[key] <= 2:
            li.append(key)
    for i in li:
        del com_list[i]
    print(com_list)

del_com()

bar = Bar("公司招聘java岗位情况", "来自：chengfei")
bar.add("岗位次数", list(key for key in com_list.keys()), list(value for value in com_list.values()),mark_line=['min', 'max'], xaxis_interval=0,xaxis_rotate=25, is_toolbox_show = True,is_more_utils=True)
bar

def get_salary():
    '''获取招聘的工资'''
    min_list = [] #起步工资
    max_list = [] #最高工资
    job_title = [] #岗位
    for item in zhipin_java.find():
        job_title.append(item['job_title'])
        salary = item['salary']
        min_list.append(int(salary.split('-')[0][:-1]))
        max_list.append(int(salary.split('-')[1][:-1]))
    return min_list,max_list,job_title


min_list,max_list,job_title = get_salary()

line = Line("薪水柱状图","单位：/k")
line.add("起步薪水", job_title, min_list, is_stack=True, mark_line=["average"], mark_point=["max", "min"],is_toolbox_show = True,is_more_utils=True)
line.add("最高薪水", job_title, max_list, is_stack=True, mark_line=["average"],mark_point=["max", "min"], is_toolbox_show = True,is_more_utils=True)
line

# 查看数据
for item in zhipin_python.find({},{'_id':0}).limit(5):
    print(item)


import re
def get_py_zone():
    ''' 获取地区'''
    zone_py_list = []
    real_py_list = []
    for item in zhipin_python.find():
        text = item['person_info'][3:6]
        zone_py_list.append(text)
    for i in zone_py_list:
        j = re.sub(r' \d-','',i)
        real_py_list.append(j)
        while '' in real_py_list:
            real_py_list.remove('')
    return real_py_list

py_zone = dict(Counter(get_py_zone()))
print(py_zone)


del py_zone[' 经验']
py_zone

bar = Bar("pyton岗位地区分布", "来自：chengfei")
bar.add("zone", list(key for key in py_zone.keys()), list(value for value in py_zone.values()),mark_line=['min', 'max'], is_toolbox_show = True,is_more_utils=True)
bar



bar = Bar("java和python岗位地区分布")
bar.add("java", list(key for key in zone.keys()), list(value for value in zone.values()),mark_line=['min', 'max'], is_toolbox_show = True,is_more_utils=True)
bar.add("python", list(key for key in py_zone.keys()), list(value for value in py_zone.values()),mark_line=['min', 'max'], is_toolbox_show = True,is_more_utils=True)
bar


def get_py_job():
    '''获取python岗位情况'''
    job_list = []
    for i in zhipin_python.find():
        job = i['job_title']
        job_list.append(job)
    return dict(Counter(job_list))

py_job_dict = get_py_job()

def del_py_key_1():
    '''删除招聘次数为1的岗位'''
    li = []
    for key in py_job_dict.keys():
        if py_job_dict[key] == 1:
            li.append(key)
    for i in li:
        del py_job_dict[i]
    print(py_job_dict)
del_py_key_1()

bar = Bar("python岗位情况")
bar.add("python", list(key for key in py_job_dict.keys()), list(value for value in py_job_dict.values()),mark_line=['min', 'max'], xaxis_interval=5,xaxis_rotate=10,is_toolbox_show = True,is_more_utils=True)
bar


pie = Pie("python岗位占比", "来自：Python绿洲",title_pos='center' )
pie.add("岗位", list(key for key in py_job_dict.keys()), list(value for value in py_job_dict.values()),radius=[40, 75],is_random=True,is_label_show=True)
pie.use_theme("dark")
pie


def get_py_company():
    '''获取公司情况'''
    com_list = []
    for i in zhipin_python.find():
        com = i['company']
        com_list.append(com)
    return dict(Counter(com_list))

py_com_list = get_py_company()

def del_py_com():
    '''删除招聘次数小于2的公司'''
    li = []
    for key in py_com_list.keys():
        if py_com_list[key] <= 2:
            li.append(key)
    for i in li:
        del py_com_list[i]
    print(py_com_list)


del_py_com()


bar = Bar("公司招聘python岗位情况", "来自：chengfei")
bar.add("岗位次数", list(key for key in py_com_list.keys()), list(value for value in py_com_list.values()),mark_line=['min', 'max'], xaxis_interval=0,xaxis_rotate=25, is_toolbox_show = True,is_more_utils=True)
bar


def get_py_salary():
    '''获取招聘的工资'''
    py_min_list = [] #起步工资
    py_max_list = [] #最高工资
    py_job_title = [] #岗位
    for item in zhipin_python.find():
        py_job_title.append(item['job_title'])
        salary = item['salary']
        py_min_list.append(int(salary.split('-')[0][:-1]))
        py_max_list.append(int(salary.split('-')[1][:-1]))
    return py_min_list,py_max_list,py_job_title




py_min_list,py_max_list,py_job_title = get_py_salary()



line = Line("起步薪水对比图","单位：/k")
line.add("java起步薪水", job_title, min_list, is_stack=True, mark_line=["average"], mark_point=["max", "min"],is_toolbox_show = True,is_more_utils=True)
line.add("python最高薪水", py_job_title, py_min_list, is_stack=True, mark_line=["average"],mark_point=["max", "min"], is_toolbox_show = True,is_more_utils=True)
line


line = Line("最高薪水对比图","单位：/k")
print(max_list)
print(job_title)
print(py_max_list)
line.add("java最高薪水", job_title, max_list, is_stack=True, mark_line=["average"], mark_point=["max", "min"],is_toolbox_show = True,is_more_utils=True)
line.add("python最高薪水", py_job_title, py_max_list, is_stack=True, mark_line=["average"],mark_point=["max", "min"], is_toolbox_show = True,is_more_utils=True)
line


java_list = []
python_list = []
for i in zhipin_java.find():
    j = re.sub(r'(Java|java|JAVA)','',i['job_title'])
    java_list.append(j)
for i in zhipin_python.find():
    k = re.sub(r'(Python|python)','',i['job_title'])
    python_list.append(k)



java_dict = dict(Counter(java_list))
python_dict = dict(Counter(python_list))


from pyecharts import WordCloud
wordcloud = WordCloud("python岗位词云")
wordcloud.add("", list(key for key in python_dict.keys()), list(value for value in python_dict.values()), word_size_range=[20, 100])
wordcloud




wordcloud = WordCloud('java岗位词云')
wordcloud.add("java", list(key for key in java_dict.keys()), list(value for value in java_dict.values()), word_size_range=[20, 100])
wordcloud


if __name__ == '__main__':
    wordcloud = WordCloud('java岗位词云')
    wordcloud.add("java", list(key for key in java_dict.keys()), list(value for value in java_dict.values()),
                  word_size_range=[40, 75])

    wordcloud.render(path='wordcloud.html')

    line = Line("最高薪水对比图", "单位：/k")
    line.add("java最高薪水", job_title, max_list, is_stack=True, mark_line=["average"], mark_point=["max", "min"],
             is_toolbox_show=True, is_more_utils=True)
    line.add("python最高薪水", py_job_title, py_max_list, is_stack=True, mark_line=["average"], mark_point=["max", "min"],
             is_toolbox_show=True, is_more_utils=True)
    line.render(path='java_lind.html')

    bar = Bar("公司招聘java岗位情况", "来自：chengfei")
    bar.add("岗位次数", list(key for key in com_list.keys()), list(value for value in com_list.values()),
            mark_line=['min', 'max'], xaxis_interval=0, xaxis_rotate=25, is_toolbox_show=True, is_more_utils=True)
    bar.render(path='java_gangwei.html')

    pie = Pie("python岗位占比", "from:chengfei",title_pos='center' )
    pie.add("岗位", list(key for key in py_job_dict.keys()), list(value for value in py_job_dict.values()),radius=[40, 75],is_random=True,is_label_show=True)
    pie.use_theme("dark")
    pie.render(path='python_gangwei_duibi.html')


    grid = Grid(height=1720, width=2200)
    grid.add(bar, grid_bottom="60%", grid_left="60%")
    grid.add(line, grid_bottom="60%", grid_right="60%")
    grid.add(pie, grid_top="60%", grid_left="60%")
    grid.add(wordcloud, grid_top="60%", grid_right="60%")
    grid.render(path='4in1.html')

    # bar = Bar("公司招聘python岗位情况", "来自：chengfei")
    # bar.add("岗位次数", list(key for key in py_com_list.keys()), list(value for value in py_com_list.values()),
    #         mark_line=['min', 'max'], xaxis_interval=0, xaxis_rotate=25, is_toolbox_show=True, is_more_utils=True)
    # bar.render(path='java_gangwei.html')
    #
    # pie = Pie("python岗位占比", "from:chengfei",title_pos='center' )
    # pie.add("岗位", list(key for key in py_job_dict.keys()), list(value for value in py_job_dict.values()),radius=[40, 75],is_random=True,is_label_show=True)
    # pie.use_theme("dark")
    # pie.render(path='python_gangwei_duibi.html')
    #
    #
    #
    # pie = Pie("java岗位占比", "来自：chengfei",title_pos='center' )
    # pie.add("岗位", list(key for key in job_dict.keys()), list(value for value in job_dict.values()),radius=[40, 75],is_random=True,is_label_show=True)
    # pie.use_theme("dark")
    # pie.render(path='java_gangwei_duibi.html')
    #



# if __name__ == '__main__':
#     zone = dict(Counter(get_zone()))
#     py_zone = dict(Counter(get_pyzone()))
#
#     bar = Bar("java和python岗位地区分布")
#     bar.add("java", list(key for key in zone.keys()), list(value for value in zone.values()), mark_line=['min', 'max'],
#             is_toolbox_show=True, is_more_utils=True)
#     bar.add("python", list(key for key in py_zone.keys()), list(value for value in py_zone.values()),
#             mark_line=['min', 'max'], is_toolbox_show=True, is_more_utils=True)
#     bar.render(path='bar.html')




    # x = []
    # y = []
    # for key in zone.keys():
    #     x.append(key)
    #     y.append(zone.get(key))
    #
    # bar = Bar('岗位分布地区')
    # bar.add('Java', x, y, mark_line=["average"], mark_point=["max", "min"], word_size_range=[10, 100])
    # # bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    # # bar.render('charts.hmtl')
    # # get_zone()
    # bar.render(path='bar.html')
    #
    # pie = Pie('岗位分布地区')
    # pie.add('Java', x, y, mark_line=["average"], mark_point=["max", "min"], word_size_range=[10, 100])
    # # bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    # # bar.render('charts.hmtl')
    # # get_zone()
    # pie.render(path='pie.html')