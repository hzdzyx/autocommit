import argparse
import json
import os

import requests
import prompt
import git
import apikey

config = {}
# 创建解析器
parser = argparse.ArgumentParser()

# 添加参数
parser.add_argument('-f', '--file', required=True, help='生成commit的文件')
parser.add_argument('-k', '--key', required=False, help='使用的key')
# 解析参数
args = parser.parse_args()

# 获取并打印出文件的绝对路径
abs_path = os.path.abspath(args.file)
key = apikey.get_key_from_file()
if not key:
    if args.key:
        key = args.key
        apikey.save_key_to_file(key)
    else:
        raise ValueError("初次运行时必须提供 '--key' 参数")


def main():
    file_name = abs_path
    diff = git.get_git_diff(file_name)

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        'key': key,
    }
    prompt_text = prompt.generate_prompt('en', 50, 'conventional')
    json_data = {
        'contents': [
            {"role": "user",
             "parts": [{
                 "text": prompt_text}]},
            {"role": "model",
             "parts": [{
                 "text": "please give me the git diff"}]},
            {"role": "user",
             "parts": [{
                 "text": diff}]},
        ],
    }
    response = requests.post(
        url=url,
        params=params,
        headers=headers,
        json=json_data,
    )
    commit_msg = json.loads(response.text)['candidates'][0]['content']['parts'][0]['text']
    print(commit_msg)


if __name__ == "__main__":
    main()
