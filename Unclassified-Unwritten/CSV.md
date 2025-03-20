# CSV(comma-sepatated values)

필드를 쉼표(,)로 구분한 파일 형식이다. 확장자는 `.csv`이다. 
쉼표 대신 탭으로 구분하는 'tab-separated values'(TSV)나 반각 스페이스로 구분하는 'space'


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
