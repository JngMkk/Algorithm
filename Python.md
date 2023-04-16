# Python

> 새롭게 알게 된 사실들 정리

## Class


- static method

  ```
  인스턴스 메서드가 객체의 인스턴스 필드를 self를 통해 액세스할 수 있는 반면,
  정적 메서드는 이러한 self 파라미터를 갖지 않고 인스턴스 변수에 액세스할 수 없음.
  따라서, 정적 메서드는 보통 객체 필드와 독립적이지만 로직상 클래스 내에 포함되는 메서드에 사용됨.
  ```

- class method

  ```
  객체 인스턴스를 의미하는 self 대신 cls라는 클래스를 의미하는 파라미터를 전달받음.
  클래스 메서드는 이렇게 전달받은 cls 파라미터를 통해 클래스 변수 등을 액세스할 수 있음.
  일반적으로 인스턴스 변수를 액세스할 필요가 없는 경우 클래스 메서드나 정적 메서드를 사용하는데,
  이때 보통 클래스 변수를 액세스할 필요가 있을 때는 클래스 메서드를, 이를 액세스할 필요가 없을 때는 정적 메서드를 사용함.
  ```

- 왈러스 연산자

  > 대입식에서는 왈러스 연산자(:=)를 사용해 하나의 식 안에서 변수 이름에 값을 대입하면서 이 값을 평가할 수 있고 중복을 줄일 수 있음
  >
  > Python 3.9 이상부터 지원

  ```python
  dic = {
      "baechu": 7,
      "pikachu": 0
  }
  
  cnt = dic.get("baechu", 0)
  if cnt > 2:
      lets_gimjang(cnt)
  else:
      nothing_to_do()
  
  # 왈러스 연산자를 사용해 중복을 줄이고 가독성 높임
  if (cnt := dic.get("baechu", 0)) > 2:
      lets_gimjang(cnt)
  else:
      nothing_to_do()
  ```

- 리스트 언패킹

  ```py
  items = [x for x in range(0, 10, 2)]
  
  lowest, second, *others = items
  print(lowest, second, others)
  >>> 0 2 [4, 6, 8]
  ```

- 정확도가 매우 중요한 경우에는 decimal 사용

  ```py
  from decimal import Decimal, ROUND_UP
  
  rate = 1.45
  seconds = 3*60 + 42
  cost = rate * seconds / 60
  
  # IEEE 754 부동소수점 수의 내부(이진) 표현법으로 인해 결과는 올바른 값보다 작음
  print(cost)
  
  
  rate = Decimal("1.45")
  seconds = Decimal(3*60 + 42)
  cost = rate * seconds / Decimal(60)
  
  # Decimal 클래스는 디폴트로 소수점 이하 28번째 자리까지 고정소수점 수 연산을 제공함.
  # 자릿수를 더 늘릴 수도 있음.
  # 이 기능을 활용하면 IEEE 754 부동소수점 수에 존재하는 문제를 우회할 수 있음.
  print(cost)
  
  
  # Decimal 생성자에 정수를 넘기는 경우는 문제가 되지 않지만
  # 소수를 넘기는 경우 오차가 발생할 수 있음
  # 정확한 답이 필요하다면 생성자에 str을 사용
  print(Decimal("1.45"))
  print(Decimal(1.45))
  print(Decimal("456"))
  print(Decimal(456))
  
  
  # 수가 매우 작을 때 반올림을 하는 경우 주의해야 할 필요 있음
  rate = Decimal("0.05")
  seconds = Decimal("5")
  small_cost = rate * seconds / Decimal("60")
  print(small_cost)
  >>> 0.004166666666666666666666666667
  
  # 수가 너무 작아서 0.00으로 계산될 우려가 있음.
  print(round(small_cost, 2))
  >>> 0.00
  
  # 원하는 소수점 이하 자리까지 원하는 방식으로 근삿값 계산
  rounded = small_cost.quantize(Decimal("0.01"), rounding=ROUND_UP)
  print(rounded)
  >>> 0.01
  
  """
  Decimal은 고정소수점 수에 대해서는 잘 작동하지만 여전히 정밀도에 한계가 있음
  예를 들어 1/3은 여전히 근사치를 사용해야 함.
  정밀도 제한 없이 유리수를 사용하고 싶다면 fractions 내장 모듈에 있는 Fraction 클래스를 사용
  """
  ```

- Package

  ```
  package는 폴더 안에 있는 모듈 모음. 패키지 이름은 폴더 이름.
  이 폴더가 디렉터리의 다른 폴더와 구별되는 패키지임을 알리려면 __init__.py 비어있는 파일을 두면 됨.
  
  실제로 파이썬에서 패키지를 사용할 수 있다고 가정하는 것은 그 패키지를 임포트할 수 있다는 것.
  패키지를 파이썬의 site-packages 폴더에 설치하거나
  PYTHONPATH 환경 변수에 설정해 임포트할 패키지나 모듈을 검색하려는 폴더를 파이썬에게 알릴 수 있음.
  ```

  - 전체로서의 패키지

    ```
    패키지 내의 모듈이 아닌 패키지에서 직접 온 것처럼 보이는 코드를 임포트할 수 있음.
    database.py products.py라는 두 개의 모듈 파일을 갖는 ecommerce 패키지가 있고,
    database 모듈에는 많은 위치에서 액세스되는 db 변수가 있음.
    
    디렉터리를 패키지로 정의하는 __init__.py 파일에 자주 사용하는 변수나 클래스 선언을 포함해 패키지의 일부로 사용할 수 있음.
    ecommerce/__init__.py 파일에 from .database import db를 넣으면
    from ecommerce import db로 임포트할 수 있음.
    ```

- 데이터 액세스 제어

  ```
  대부분의 객체지향 프로그래밍 언어에는 액세스 제어라는 개념이 있음. (추상화와 관련이 있음.)
  private, 즉 비공개로 표시된 객체의 속성과 메서드는 해당 객체만 액세스할 수 있음을 의미함.
  protected로 표시된 것은 해당 클래스와 그 하위 클래스만 액세스할 수 있음을 의미함.
  나머지는 public, 즉 공개이므로 다른 객체의 액세스가 허용됨.
  
  관례에 따라 일반적으로 내부 속성이나 내부 메서드 앞에는 밑줄 문자 _를 붙여야 함.
  파이썬 개발자는 이것을 내부 변수로 이해하고 직접 액세스하기 전에 생각할 것임.
  
  외부 객체가 프로퍼티나 메서드에 액세스하지 않도록 제안할 수 있는 또 다른 방법은 이중 밑줄 __ 사용.
  이것은 해당 속성에 대해 네임 맹글링(name mangling)을 수행함.
  본질적으로 네임 맹글링은 외부 객체가 정말로 원할 경우 여전히 메서드를 호출할 수 있지만
  그것을 위해서는 추가 작업이 필요하며 속성이 비공개로 유지돼야 한다는 강력한 표시임.
  
  이중 밑줄을 사용하면 프로퍼티 앞에 _<클래스이름>이 붙음.
  클래스의 메서드가 내부적으로 변수에 액세스하면 자동으로 맹글링이 해제됨.
  외부 클래스가 이 비공개 프로퍼티에 액세스하기를 원하면 그것은 스스로 네임 맹글링 처리를 해야만 함.
  따라서 네임 맹글링은 프라이버시를 보장하지 않으며 단지 강력하게 권할 뿐임.
  ```

- priority queue vs heapq

  ```
  내부 코드에서는 priority queue가 그냥 heapq를 그대로 가지고 사용함.
  하지만 priority queue는 thread-safe 하므로 공유 자원에 여러 스레드가 접근해도 프로그램 실행에 문제가 없음.
  그에 비해 heapq는 non-thread-safe 함.
  
  실행 시간은 heapq가 priority queue 보다 당연하게 현저히 빠름.
  ```

- in 연산자를 사용할 때 set을 쓰자.

  ```
  if in 할 때 list, tuple은 O(n), but set은 O(1)
  ```

- list comprehension vs generator

  ```
  list = [x for x in range(1000)]
  generator = (x for x in range(1000))
  
  메모리 사이즈 엄청 잡아 먹는다. 차이 큼.
  
  list = [x for x in range(10000)]
  generator = (x for x in range(10000))
  
  sys.getsizeof(list), sys.getsizeof(generator)
  
  (85176, 112)
  ```

- filter 함수

  ```
  filter(조건 함수, 순회 가능한 데이터)
  
  두번째 인자로 넘어온 데이터 중에서 첫번째 인자로 넘어온 조건 함수를 만족하는 데이터만을 반환합니다.
  ```