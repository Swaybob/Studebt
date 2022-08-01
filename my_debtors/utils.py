from uuid import uuid4


def random_reg_num():
    random_reg = str(uuid4())[:8]
    random_reg = 'STU' + random_reg
    return random_reg
