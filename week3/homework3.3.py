import re
def validate_id_card(id_card):
    # 定义身份证号的正则表达式
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}(\d|X)$'

    # 使用正则表达式匹配身份证号
    if re.match(pattern, id_card):
        return True
    else:
        return False

# 测试函数
id_card = "222426200404160313"  # 替换成要验证的身份证号
if validate_id_card(id_card):
    print("身份证号合法")
else:
    print("身份证号不合法")
