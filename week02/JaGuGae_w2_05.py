"""
*알고리즘의 효율성 분석
연산횟수가 더 작을수록 효율적이라고 말할 수 있다.
ex) n vs n^2 -> n이 더 효율적임.
하지만, 100n과 n^2이라면? -> n의 값이 10000 이상이냐 이하냐에 따라 결과가 달라짐.

*알고리즘의 점근적 복잡도
간단히 말하면, n의 값이 무한히 클 때의 시간 복잡도
이럴 경우 일단 차수가 더 중요한 영향을 미침, 상수는 중요하지 않음

*알고리즘의 점근표기법
알고리즘의 기본 연산 수행 횟수의 증가율은 입력 크기 n에 대한 함수로 표현 가능함
이 함수는 무한히 큰 입력 n에 대한 단순한 복잡도 함수로 표현하기 위해 점근표기법이 사용됨.
크게 Big-Oh, Big-Omega, Theta의 세 가지 방식이 존재한다. 이 정의법들은 그냥 외우는게 나음. 정의라서.

1. Big-Oh 표기법
모든 n >= n0에 대하여 f(n) <= c*g(n)이 성립하는 임의의 상수 c와 n0이 존재하면 f(n) = O(g(n))이다.
f(n): 알고리즘의 시간 복잡도, g(n): 복잡도 함수 - 상수를 제거한 단순 단항식
즉, n0보다 같거나 큰 모든 n에 대해서 기본 연산 횟수가 아무리 커봤자 c*g(n)보다는 같거나 작다는 의미(상한). 즉 이거보단 효율적이다.
이 g(n)이랑 c, n0의 값이 반드시 하나만 존재하는 것이 아니므로, 적당히 큰 c와 n0를 선택해야한다.
웬만해선 tight upper bound를 많이 사용한다.차수가 최대한 낮도록.
자주 사용되는 O표기를 확인하려면 수업 자료 참고.

2. Omega 표기법
모든 n >= n0에 대하여 f(n) >= c*g(n)이 성립하는 임의의 상수 c와 n0이 존재하면 f(n) = 오메가(g(n))이다.
Big-Oh 표기법의 반대버전이라고 생각하면 된다. 하한을 의미한다. 아무리 좋아봤자 이정도임을 나타내는 의미이다.

3. Theta 표기법
모든 n >= n0에 대하여 c1*g(n) <= f(n) <= c2*g(n)이 성립하는 양의 상수 c1, c2, n0가 존재하면 f(n) = 세타(g(n))이다.
세타 표기는 특정 알고리즘 시간 복잡도의 O 표기와 세타 표기가 동일한 경우에만 사용한다.
증가율의 유사하다는 것을 의미함. 최고차항과 높은 관련이 있음.
세타 표기법으로서의 Big-Oh 표기법을 많이 사용한다.
"""