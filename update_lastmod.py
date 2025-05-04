import os
import subprocess
import datetime
import frontmatter

# 修改为你 content 目录的路径
CONTENT_DIR = "C:\Users\62482\OneDrive\Desktop\my-blog\content\cn\posts"

def get_git_last_modified(filepath):
    try:
        output = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI", filepath],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        ).strip()
        return output
    except subprocess.CalledProcessError:
        return None

def update_lastmod_in_file(filepath):
    post = frontmatter.load(filepath)
    lastmod = get_git_last_modified(filepath)

    if lastmod:
        post['lastmod'] = lastmod
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        print(f"✅ Updated: {filepath}")
    else:
        print(f"⚠️ No git info for: {filepath}")

def walk_and_update():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                update_lastmod_in_file(full_path)

if __name__ == "__main__":
    walk_and_update()
