import json

# 加载json文件数据
filename = 'population_data.json'
with open(filename, 'r') as object:
    pop_data = json.load(object)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        print(pop_dict['Country Name'] + ': ' + pop_dict['Value'])
