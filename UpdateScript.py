import os

rootDir = os.path.dirname(os.path.abspath(__file__))
readmeFile = os.path.join(rootDir, "README.md")

# 제외할 카테고리
excludeCategories = ["Books"]  

# 고정 내용 
fixedContent = """
# TIL
> Today I Learned

개인적으로 공부한 내용을 위키처럼 모아두는 저장소.

_총 {totalPosts}개의 글_

### 📖 Book
[독서 기록은 `/Books`에서 확인할 수 있다.](https://github.com/river20s/TIL/tree/main/Books)

"""

# 카테고리별 고정 내용
categoryTemplate = "### {category}\n{posts}\n"

def getPostLinks(category):
    categoryPath = os.path.join(rootDir, category)
    posts = []
    
    # 링크 목록 생성
    for post in os.listdir(categoryPath):
        postPath = os.path.join(categoryPath, post)
        if os.path.isfile(postPath):
            postName = os.path.splitext(post)[0]
            postLink = f"- [{postName}](https://github.com/river20s/TIL/blob/main/{category}/{post})"
            posts.append(postLink)
    
    return "\n".join(posts)

def countPostsAndUpdateReadme():
    categories = {}
    totalPosts = 0

    # 카테고리 폴더별로 파일 수 카운트
    for category in os.listdir(rootDir):
        categoryPath = os.path.join(rootDir, category)
        if os.path.isdir(categoryPath) and category not in excludeCategories:
            postLinks = getPostLinks(category)
            postCount = len(postLinks.splitlines())
            if postCount > 0:
                categories[category] = postLinks
                totalPosts += postCount

    # README 업데이트
    with open(readmeFile, "w", encoding="utf-8") as readme:
        # 고정 내용 작성
        readme.write(fixedContent.format(totalPosts=totalPosts))

        # 카테고리별 글 목록 작성
        for category, posts in categories.items():
            readme.write(categoryTemplate.format(category=category, posts=posts))

        # 고정된 하단 내용 작성
        readme.write("""
### 📖 Books

- [성공과 실패를 결정하는 1%의 네트워크 관리](https://github.com/river20s/TIL/tree/main/Books/HowNetworksWork#readme)
- [가상 면접 사례로 배우는 대규모 시스템 설계 기초](https://github.com/river20s/TIL/tree/main/Books/System%20Design%20Interview)

---
[참고한 til](https://github.com/jbranchaud/til)
""")


if __name__ == "__main__":
    countPostsAndUpdateReadme()
