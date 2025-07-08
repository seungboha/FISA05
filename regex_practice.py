import re

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식

# 이메일 형식을 판별하는 검사기를 만들어주세요. 반복문과 조건문, re 모듈을 사용합니다.

pattern = r'(\S+)+@[a-z.-]+\.[a-z]+$'
p = re.compile(pattern)

for email in emails:
    if p.match(email):
        print(f"valid - {email}")
    else:
        print(f"invalid - {email}")
print("====================================")
# ----------------------------------------------------
string = '신짱구 010-2222-3333'
# 010-2233-3333 / 신짱구

p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
print(p.sub(r'\2 / \1', string))


string0 = '신짱구 011-222-3333'
string1 = '신짱구 011-2222-3333'
patterns = r"(?P<name>^[가-핳])\s+(?P<phone_num>(\d+[-]\d+[-]\d+))"

p = re.compile(patterns)
print(p.sub(r"\g<phone_num> \/ \g<name>", string1))
print("====================================")
# ----------------------------------------------------

## f-string
print(f"Filling with x upto 4 digits: {10:{'x'}>4}")