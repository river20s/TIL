# fatal: not a git repository는 무슨 의미인가
> 이 오류는 Git 명령을 실행하려고 했지만 현재 위치가 Git 저장소 내부가 아니라는 것을 의미한다. Git 명령은 특정 저장소에서 실행해야 한다.
### Git 저장소 내부에서 명령어를 사용하지 않았을 때
- `ls` 명령어를 이용해 현재 디렉토리를 확인한다.
- 작업 디렉토리가 맞는지 확인한다.
- `cd <경로>`를 사용해 올바른 디렉토리로 이동한다.
작업 디렉토리에 있다면 Git 저장소로 설정되었는지 확인해야 한다.
### Git 저장소가 초기화되지 않았을 때
- `.git` 폴더가 존재하지 않으면 저장소가 초기화되지 않은 것이다.
- `git init` 명령어를 사용하여 Git 저장소를 새롭게 설정할 수도 있다.
> **Git 저장소**란 `.git` 폴더가 위치한 디렉토리이다. `.git` 폴더에는 변경사항의 기록, 현재 작업 중인 브랜치, Git이 추적하는 기타 모든 정보 등이 들어 있다.
> Git 명령을 실행하면 가장 먼저 Git이 하는 일은 `.git` 폴더를 찾아 유효한 Git 저장소에서 작업 중인지 확인하는 것이다.
> 해당 폴더를 찾으면 다음 단계로 넘어가지만, 해당 폴더를 찾을 수 없으면 Git은 프로젝트에 대해 아무것도 모르기 때문에 *화를 낸다.*
## Git 저장소에 있는지 확인하는 방법 - `-laf` 플래그
`.git`폴더는 리포지토리의 루트에 있어야 한다. 폴더 앞의 마침표 `.`는 숨겨진 폴더라는 것을 의미하므로, 스크립트나 OS 수준 명령만 접근할 수 있다.
`ls` 명령에 숨겨진 폴더를 표시하도록 요청하는 플래그 `-laf`를 추가하면 실제로 확인할 수 있다.
루트 디렉토리에서 해당 명령을 실행했을 때 `.git`폴더가 보인다면, Git 저장소에 있음을 확인할 수 있다.
## HEAD 파일 확인하기
위에서 확인한 모든 내용에 문제가 없다면 **HEAD 파일이 손상되었을 수도 있다.**
**HEAD 파일**은 `.git` 디렉토리에 있는 파일로, 현재 작업 중인 브랜치를 Git에게 알려주는 정보가 들어있다. 이 파일이 없어지거나 손상되면 올바르게 초기화된 저장소에 있더라도 `fatal: not a git repository` 오류가 표시된다.
HEAD파일을 확인하려면 다음과 같이 입력한다.
```
$ cat .git/HEAD
```
파일에 문제가 없다면 다음과 같이 보일 것이다.
```
$ cat .git/HEAD
ref: refs/heads/main
```
만약 편집이 필요하다면 `git symbolic-ref` 명령어를 사용하면 된다. 예를 들어 `main` 브랜치인 경우:
```
$ git symbolic-ref HEAD refs/heads/main
```
---
### 참고
- [Git error - Fatal: Not a git repository](https://www.datree.io/resources/git-error-fatal-not-a-git-repository)
- [Git의 내부 - Git Refs](https://git-scm.com/book/ko/v2/Git%ec%9d%98-%eb%82%b4%eb%b6%80-Git-Refs)
- [git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [git-init](https://git-scm.com/docs/git-init)
