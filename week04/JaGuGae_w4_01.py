"""
리스트: 유한한 수의 항목들이 순서를 이루어 나열되어 있는 논리적 선형 구조
-C나 JAVA에서는 정적 배열이 존재한다.(Static Array)
-Python에서는 리스트의 정적 배열이 존재한다. JAVA의 ArrayList와 유사(Dynamic Array)
-단순 연결 리스트, 이중 연결 리스트, 환형 연결 리스트가 존재한다.
"""
"""
*단순 연결 리스트(Singly Linked List)
리스트의 항목들을 (1) 메모리에 분산하여 저장하고(즉, 메모리에 연속적으로 저장할 필요가 없고)
               (2) 각 항목은 다음 순서의 항목이 저장된 위치를 가리키는 링크를 가짐으로써 순서를 유지
               
구성 단위: 노드
-각 항목들은 기본 단위인 노드(사용자 정의 데이터 타입)에 저장
-리스트의 각 항목에 대한 노드는 동적으로 메모리를 할당받으며, 해당 항목을 저장하기 위한 데이터 필드(data field)와,
 다음 순서 노드의 참조를 위한 링크 필드(link field)로 구성
 
리스트의 각 항목을 저장하고 있는 노드를 링크 필드의 참조를 이용하여 다음 순서의 노드를 가리키도록 만들어서(마지막 노드의 링크 필드는 None)
모든 노드들을 한 줄로 연결시킨 구조

단순 연결 리스트 ADT
-데이터: (1) 순차(Sequential)방식으로만 접근 가능한 노드들의 집합과
        (2) 단순 연결 리스트의 시작을 가리키는(첫 번째 노드의 참조를 저장하는) 변수인 head
"""