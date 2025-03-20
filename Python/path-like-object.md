# path-like object (경로류 객체)
파일 시스템 경로를 나타내는 `str`이나 `bytes` 객체 또는 `os.PathLike` 프로토콜을 구현하는 객체.
`os.PathLike` 프로토콜을 지원하는 객체는 `os.fspath()` 함수를 호출해서 `str`나 `bytes` 파일 시스템 경로로 변환될 수 있다. 
[PEP 519]([PEP 519 – Adding a file system path protocol | peps.python.org](https://peps.python.org/pep-0519/))로 도입되었다.

### 읽어보기
[용어집 — Python 3.13.2 문서](https://docs.python.org/ko/3.13/glossary.html#term-PEP)
