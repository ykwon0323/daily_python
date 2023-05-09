# 1 코딩블럭 들여쓰기 (Identation)
#     - 코딩블럭을 표시하기 위해 들여쓰기(Identation)을 사용
#     - 코딩블럭을 시작하는 문장들 if, for, def 문들의 끝에는 :을 사용한다
#     - 들여쓰기 = 4개의 공백 ( tab과 혼용하지 말것 )

# 2 파이썬 표준 라이브러리
#     - import 문 사용
#     math 라이브러리 예제
#     ~~~
#     import math
#     n = math.sqrt(9.0)
#     print(n)
#     ~~~

# 3 코멘트 
#     - 파운드 (#) 사용
#     - 파운드 사인 뒤 한칸의 공백을 두는것을 권장

# 코딩 스타일 규칙
# 코드 레이아웃 
#     - 들여쓰기를 할 때 Tab 대신 공백(Space)를 사용
#     - 특히 python3는 Tab과 공백을 혼용해서 사용하는 것을 허용하지 않는다
#     - 문법적으로 들여쓰기를 할 때는 4개의 공백을 사용한다
#     - 각 라인은 79자 이하로 한다. 라인이 길어서 다음 라인으로 넘어갈 때는 원래 들여쓰기 자리에서 4개 공백을 더 들여쓴다
#     - 함수나 클래스는 2개의 공백 라인을 추가하여 구분한다. 메서드는 한개의 공백 라인으로 구분한다
#     - import는 (여러 모듈을 콤마로 연결하지 말고) 한 라인에 하나의 모듈을 import 한다
#     - 컬렉션 인덱스나 함수 호출, 함수 파라미터 등에서 필요한 공백을 넣지 않는다
#     - 변수 할당시 할당자 앞뒤로 하나의 공백만 넣는다
# 명명 규칙
#     - 함수, 변수, Attribute는 소문자로 단어 간은 밑줄을 사용하여 연결한다 (ex : total_numbers)
#     - 클래스는 단어 첫 문자마다 대문자를 써서 연결하는 CapWords 포맷으로 명명한다(ex : CoreClass)
#     - 모듈명은 짧게 소문자로 사용하여 밑줄을 쓸 수 있다. 패키지명 역시 짧게 소문자를 사용하지만 밑줄은 사용하지 않는다
#     - 모듈 상수는 모두 대문자를 사용하고 단어마다 밑줄로 연결하는 ALL_CAPS 포맷으로 명명한다
#     - 클래스의 public attribute는 밑줄로 시작하지 말아야 한다
#     - 클래스의 protected instance attribute는 하나의 밑줄로 시작한다 (ex : _initialized)
#     - 클래스의 private instance attribute는 2개의 밑줄로 시작한다 (ex : __private_var)
#     - 인스턴스 메서드는 (객체 자신을 가리키기 위해) self를 사용한다 (ex : def copy(self, other):)
#     - 클래스 메서드는 (클래스 자신을 가리키기 위해) cls를 사용한다 (ex: def clone(cls, other):)
# 문장과 표현식
#     - if, for, while 블럭 문장을 한 라인으로 작성하지 말 것, 여러 라인을 걸쳐 사용하는 것이 더 명료함
#     - a는 b가 아니다를 표현할 때 a is not b를 사용한다. not a is b를 사용하지 말것 
#         (ex : [x]if not a is b / [o]if a is not b)
#     - 값이 비어있는지 아닌지를 검사하기 위해 길이를 체크하는 방식을 사용하지 말 것. 대신 if mylist와 같이 표현
#         (ex : [x]if len(mylist)>0 / [o]if mylist)
#     - import문은 항상 파일의 상단에 위치하며, 표준 라이브러리 모듈, 3rd Party모듈 그리고 자신의 모듈 순으로 import
#     - 모듈 import시 절대 경로를 사용할 것을 권장(단, 복잡한 패키지 경로를 갖는 경우 상대경로를 사용)
#         (ex : [x] import sibling
#               [o] import mypkg.sibling
#               [o] from mypkg import sibling
#               [o] from .import sibling <- 상대경로
#               [o] from .sibling import example
#          )