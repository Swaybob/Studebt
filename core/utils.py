from uuid import uuid4


def random_reg_num():
    random_reg = str(uuid4())[:4]
    random_reg = 'SCH' + random_reg
    return random_reg
