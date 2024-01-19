from github import Github

# 替换为你要查询的 GitHub 用户名
target_username = "slieb74"

# 替换为你的个人访问令牌
token = "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"

# 创建 Github 对象
g = Github(token)

# 获取目标用户
target_user = g.get_user(target_username)

# 获取目标用户的关注者
followers = target_user.get_followers()

# 遍历关注者并获取其仓库
for follower in followers:
    print(f"Follower: {follower.login}")
    repos = follower.get_repos()
    for repo in repos:
        print(f"  Repo: {repo.name}")
        # 在这里可以将仓库数据存储到本地，例如写入文件或数据库
