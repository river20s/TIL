# CSV(comma-sepatated values)

필드를 쉼표(,)로 구분한 파일 형식이다. 확장자는 `.csv`이다. 
쉼표 대신 탭으로 구분하는 'tab-separated values'(TSV)나 반각 스페이스로 구분하는 'space-separated values'(SSV) 등의 비슷한 포맷이 있다. 이들을 합쳐서 'character-separated values'(CSV), delimiter-separated values 라고 부르는 경우가 많다.
## RFC 4180
[RFC 4180]([RFC 4180 - Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180))은 CSV 포맷을 정의한다. 
## 형식
그러나 대중적으로 사용되는 "CSV"는 특별히 정의된 형식을 갖지 않기도 한다. 대체적으로 "CSV"는 다음과 같은 특징을 갖는다.
1. ASCII, 다양한 유니코드 문자 집합(UTF-8), EBCDIC, Shift JIS와 같은 문자 집합을 사용하는 플레인 텍스트
2. 레코드로 이루어져 있음 (줄 당 하나의 레코드)
3. 레코드는 여러 개의 필드로 나눔, 필드를 구별하는 구벼



## 예

|연도|제조사|모델|설명|가격|
|---|---|---|---|---|
|1997|Ford|E350|ac, abs, moon|3000.00|
|1999|Chevy|Venture "Extended Edition"||4900.00|
|1999|Chevy|Venture "Extended Edition, Very Large"||5000.00|
|1996|Jeep|Grand Cherokee|MUST SELL!  <br>air, moon roof, loaded|4799.00|
위와 같은 표를 CSV 형식으로 표현하면 다음과 같다.
```
연도,제조사,모델,설명,가격 1997,Ford,E350,"ac, abs, moon",3000.00 1999,Chevy,"Venture ""Extended Edition""","",4900.00 1999,Chevy,"Venture ""Extended Edition, Very Large""",,5000.00 1996,Jeep,Grand Cherokee,"MUST SELL!air, moon roof, loaded",4799.00
```
