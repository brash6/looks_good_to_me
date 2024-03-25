import requests
import json
import numpy as np
import base64
from openai import OpenAI


def get_tree_from_github_repo_api(tree, depth=0):
    repo_tree = ""
    for item in tree:
        len_prev = depth
        if item['type'] == 'tree':
            repo_tree = repo_tree + '│    ' * depth + \
                '├── ' + item['path'].split("/")[-1] + "\n"
            depth = len_prev = depth + 1
        else:
            cur_path_length = len(item['path'].split("/"))
            if cur_path_length < len_prev:
                depth = depth - np.abs(cur_path_length - (len_prev + 1))
            repo_tree = repo_tree + '│    ' * depth + \
                '├── ' + item['path'].split("/")[-1] + "\n"
            len_prev = cur_path_length

    print(repo_tree)
    return repo_tree


def get_repository_tree(repo_url, branch_to_review='main'):
    # Parse GitHub repository URL to get owner and repository name
    owner, repo = repo_url.split("/")[-2:]
    # Send GET request to GitHub API to retrieve repository tree
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch_to_review}?recursive=1"
    response = requests.get(url)
    tree_dict = json.loads(response.content)
    tree = get_tree_from_github_repo_api(tree_dict['tree'])
    return tree, repo


def get_package_review(repo_url, branch_to_review, client):
    # Retrieve repository tree
    tree, repo = get_repository_tree(
        repo_url, branch_to_review=branch_to_review)

    input_prompt = f"Here is the folders and files structure of a python package called {repo} \n"
    input_prompt += f"{tree}\n"
    input_prompt += f"If you think this package folders and files structure can be improved, can you suggest another structure by keeping the same tree format ?"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in software engineering in python."},
            {"role": "user", "content": f"{input_prompt}"},
        ])

    return response.choices[0].message.content


def get_file_content(repo_url, file_path, client):
    owner, repo = repo_url.split("/")[-2:]
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")

        input_prompt = f"Here is a python file {file_path} of a github repository called {repo} \n"
        input_prompt += f"{content}\n"
        input_prompt += f"Can you refactor this file to make it cleaner, better structured and matching industry programming quality standards (docstrings, relevant comments, strongtyping)?"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in software engineering in python."},
                {"role": "user", "content": f"{input_prompt}"},
            ])

        return response.choices[0].message.content
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


if __name__ == "__main__":

    client = OpenAI(
        api_key='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')

    repo_link = "https://github.com/hi-paris/deepdespeckling"
    suggestions = get_package_review(repo_link, client=client)

    print(suggestions)
