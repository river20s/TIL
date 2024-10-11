# StringBuilder란 무엇인가

- Object 클래스를 상속한다.
- `Serializable`, `CharSequence`를 구현한다.
- 문자열을 늘릴 때마다 메모리를 재할당하고 복사하는 대신 내부적으로 연속 메모리 블록을 사용한다.
- 대부분의 경우 `StringBuffer`보다 빠르다.

## 주요 작업
### `append` 메소드
주어진 데이터를 문자열로 변환한 후 변환한 문자열의 문자를 빌더의 **끝에** 추가한다.
### `insert` 메소드
주어진 데이터를 문자열로 변환한 후 변환한 문자열의 문자를 빌더의 **지정된 위치에 추가한다.**

예를 들어, `z`가 현재 내용이 "start"인 `StringBuilder` 객체를 참조하는 경우 `z.append("le")`를 호출하면 빌더는 "startle"를 포함한다. 다음으로 `z.insert(4, "le")`를 호출하면 빌더는 "sarlet"으로 변경된다.

`sb`가 `StringBuilder`의 인스턴스를 참조한 경우, `sb.append(x)`는 `sb.insert(sb.length(), x)`와 동일한 효과를 가진다.

## 용량
모든 `StringBuilder`는 용량을 가지고 있다. `StringBuilder`에 포함된 문자 시퀀스의 길이가 용량을 초과하지 않는 한 새로 내부 버퍼를 할당할 필요는 없다. 만약 내부 버퍼가 초과되면 자동으로 확장된다.

## 스레드
`StringBuilder` 인스턴스는 여러 스레드에서 동시에 사용할 경우 안전하지 않다. 동기화가 필요한 경우에는 `StringBuffer`를 사용하는 것이 낫다.

## null 예외
별도로 명시되지 않은 한, 이 클래스의 생성자 또는 메소드에 `null` 인수를 전달하면 `NullPointerException`이 발생한다.

---

참고: [Class StringBuilder](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html)





