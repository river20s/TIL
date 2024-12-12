> Java에서 `HashMap`은 키-값(key-value) 쌍을 저장하는 데 사용된다. [해시 테이블](https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94)을 기반으로 하며, **데이터 검색, 삽입, 삭제**가 가능하다.

## 특징
1. **키-값 쌍 저장**: 각 키(key)에 하나의 값(value)을 매핑한다. 키는 고유해야 하지만 값은 중복될 수 있다.
2. **해시 테이블 기반**: 내부적으로 해시 테이블을 사용하여 데이터를 저장하므로, 평균적으로 `O(1)`의 시간 복잡도로 데이터에 접근할 수 있다.
3. **순서 없음**: HashMap은 요소의 삽입 순서를 보장하지 않는다.
4. **`null`키와 값 허용**: 하나의 `null`키와 여러 개의 `null` 값을 허용한다.
5. **동기화 되지 않음**: [멀티 스레드 환경](https://ko.wikipedia.org/wiki/%EB%A9%80%ED%8B%B0%EC%8A%A4%EB%A0%88%EB%94%A9)에서 사용할 경우 외부에서 동기화 처리를 해야 한다.

## 주요 메서드
### put(K key, V value)
지정된 키와 값을 맵에 추가. 동일한 키가 이미 존재하면 기존 값을 새 값으로 대체.
```java
HashMap<String, Integer> map = new HashMap<>();
map.put("apple", 1);
map.put("banana", 2);
```
### get(Object key)
지정된 키에 매팽된 값을 반환. 키가 존재하지 않으면 null 반환.
```java
int value = map.get("apple"); // value는 1
```
### remove(Object key)
지정된 키와 그 매핑된 값을 맵에서 제거.
```java
map.remove("banana");
```
### containsKey(Object key)
맵에 지정된 키가 있나 확인.
```java
boolean hasApple = map.containsKey("apple"); // true
```
### containsValue(Object value)
맵에 지정된 값이 있나 확인.
```java
boolean hasValue1 = map.containsValue(1); // true
```
### size()
맵에 저장된 키-값 쌍의 개수를 반환.
```java
int size = map.size(); // 1
```
### keySet()
맵에 저장된 모든 키를 Set으로 반환.
```java
Set<String> keys = map.keySet();
```
### values()
맵에 저장된 모든 값을 collection으로 반환.
```java
Collection<Integer> values = map.values();
```
### entrySet()
맵에 저장된 모든 키-값 쌍을 Set으로 반환.
```java
Set<Map.Entry<String, Integer>> entries = map.entrySet();
```
## 동작 방식
HashMap은 내부적으로 [버킷(bucket)배열](https://ko.wikipedia.org/wiki/%EB%B2%84%ED%82%B7_%EC%A0%95%EB%A0%AC)을 사용하여 데이터를 저장한다. 각 키의 hashCode를 기반으로 버킷 인덱스를 계산하고, 해당 버킷에 키-값 쌍을 저장한다. 해시 충돌이 발생하면 동일한 버킷에 링크드 리스트나 트리 구조(Java 8 이후: 트리 구조)로 저장된다.
## 주의
- **해시 코드 충돌**: 키 객체는 hashCode와 equals 메서드를 적절히 오버라이드 해서 해시 코드 충돌을 최소화 해야 한다. 동일한 해시 코드를 가진 키는 동일한 버킷에 저장되므로 성능 저하 가능성이 있다.
- **동기화**: 멀티스레드 환경에서 HashMap을 사용하는 경우, 동기화 되지 않은 상태로 인하여 [데이터 무결성](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%AC%B4%EA%B2%B0%EC%84%B1)이 깨질 수 있다.
---
### 더 읽어보기
- [HashSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashSet.html)
