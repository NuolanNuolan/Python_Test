import requests

# 执行api调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print('Status code:', r.status_code)
# 将api响应储存在一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys())

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(repo_dicts)

# 研究第一个仓库
repo_dict = repo_dicts[0]
print(len(repo_dict))

for key, value in sorted(repo_dict.items()):
    print("\n" + key + "\t" + str(value))
