# 해시(Hash)

해시(Hash)는 해시 함수(hash function) 또는 해시 알고리즘(hash algorithm)의 출력으로, 입력값의 크기와 상관없이 알고리즘에 정의된 고정 길이로 출력된다. 이렇게 입력값에 해시 함수를 적용하여 해시를 출력하는 과정을 해싱(Hashing)이라 한다.



## 해시 함수

### 입력값

'메시지'라고 부르기도 한다. 다양한 길이와 형태의 데이터가 사용된다. 복잡한 데이터 구조도 입력할 수 있다. 해시 함수는 이진수로 데이터를 처리하기 때문에 입력값을 이진수로 변환하고 해싱한다.

### 함수

입력값을 고정된 크기의 블록으로 나눈 다음 수학적 연산을 적용해 최종 해시를 출력한다. 

주어진 입력에 대해 항상 동일한 해시를 생성하과, 입력 데이터가 조금이라도 바뀌면 출력값은 크게 달라진다. 이런 특성 때문에 해시는 데이터 비교 및 무결성에 사용할 수 있다.

SHA-256, SHA-3, MD5, MurmurHash, CityHash 함수 등이 있다.

### 출력값

해시 함수의 출력은 '해시' 또는 '다이제스트'라고 한다. 출력값의 길이는 해시 함수에 따라 달라진다. 각 입력에 대해 고유한 출력값이 생성되므로 지문과도 같다.

해싱은 암호화와 달리 출력값을 원본 입력값으로 복호화할 수 없다. 출력값과 해싱 함수를 안다고 해도 대응하는 입력값을 찾는 것은 어렵다.

## 해싱의 활용

- **데이터 무결성 검증**: 예를 들어 파일을 다운로드 하면 파일과 함께 해시가 제공된다. 다운로드 파일을 해싱해서 나오는 출력값과 다운로드할 때 받은 해시를 비교하면 데이터 무결성을 확인할 수 있다.
- **디지털 서명**: 메시지의 해시를 암호화 해서 디지털 서명을 생성하고, 발신 후 다시 복호화 하여 수신 메시지의 해시와 비교하는 방법을 사용할 수 있다.
- **비밀번호 저장**: 대부분의 서비스는 사용자의 실제 비밀번호를 서버에 저장하지 않고, 비밀번호의 해시를 저장한다. 서버가 해킹되어도 실제 비밀번호가 노출되지 않기 때문에 비밀번호가 안전하게 보호된다. 사용자가 비밀번호를 입력하면 비밀번호를 해싱하고, 서버에 있는 해시와 비교하여 사용자의 신원을 확인한다.
- **해시 테이블**: 테이블의 인덱스로 해시를 사용하는 자료구조. 검색이 빠르지만 충돌이 일어날 수 있다는 위험이 있다.

---

**참고 자료**

- [해싱(Hashing) | 토스페이먼츠 개발자센터](https://docs.tosspayments.com/resources/glossary/hashing)
- [해시 함수 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%ED%95%A8%EC%88%98)
- [해시 (Hash) - MDN Web Docs 용어 사전: 웹 용어 정의](https://developer.mozilla.org/ko/docs/Glossary/Hash)