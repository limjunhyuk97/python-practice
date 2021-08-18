# Package
  - .를 이용하여 계층적으로 모듈을 관리하게 해준다.
  - 디렉터리와 파이썬 모듈로 이루어져 있다. (**directory > directory > .. > module >> function / class / variable**)
  - 간단한 프로그램이 아닌경우 패키지를 구성하여 유지보수, 및 공동작업 수행.
  - 패키지 구조를 통해 이름이 같은 서로 다른 모듈을 구분할 수 있게 된다.

## Package import

### 1. from A import B
  - **A : package** 안에서, **B : package, module을 import** 할 수 있다.
  - **A : module** 안에서, **B : function, class, variable을 import** 할 수 있다.
  - B. 으로 B 하위의 대상들에게 직접 접근이 가능하다.

### 2. import A
  - **A : package, module을 import**한다. (**funcion, class, variable은 import의 대상이 아니다.**)
  - A. 에서 시작하여 하위 대상들을 직접 지칭해주어야 한다.

### 3. import directory
  - directory를 import하면, **directory.A로 A에 접근하는 경우, directory 내에 있는 \_\_init__ module 내의 A라는 속성에 접근하는 것이다.**

### 
























