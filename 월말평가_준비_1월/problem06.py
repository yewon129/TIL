def is_id_valid(user_data):
    id = user_data.get('id')
    result = list(id)
    my_list = ['0','1','2','3','4','5','6','7','8','9']
    for char in my_list:
        if result[-1] == char :
            return True
    return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False