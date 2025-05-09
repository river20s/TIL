# 해시 테이블(Hash Table)

해시 테이블은 대부분의 언어에 있는 자료구조임(해시, 맵, 딕셔너리, 연관 배열 등등…).
해시테이블은 쌍으로 이루어진 값들의 리스트인데
첫 번째 항목을 키(key), 두 번째 항목을 값(value)이라고 함.

이 자료구조를 쓰면 좋은 이유: 룩업 효율성이 매우 좋음!
평균적으로 O(1), 상수에 가까운 효율을 지님.
딱 한 단계면 룩업이 끝나기 때문이다.

해시 테이블을 이해하려면 해싱이 뭔지 알아야 함.


## 해시 함수, 해싱

이런 식으로 글자와 숫자 쌍이 있다고 가정하자.
```
A = 1

B = 2

C = 3

D = 4

E = 5

…
```

이 규칙에 따르면

`ACE → 135`

`CAB → 312`

`BAD → 214`

로 변환이 가능함.
이런 것이 해싱(hasing)임.
여기에서 글자를 숫자로 변환하는데 사용한 규칙들을 해시 함수(hash function)라고 함.
해시 함수는 여러 종류가 있는데 예를 들어 숫자를 곱해서 반환하는 것으로 정의할 수 있음.

`BAD → 2*1*4 → 8`

동일한 문자열을 항상 동일한 숫자로 변환하는 유일성이 만족될 때 해시 함수로 쓸 수 있음.
