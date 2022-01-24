def is_user_data_valid(user_data):
    info = ['id','password']
    for key in info:
        user_data.get(key)
        if bool(user_data.get(key)) == 0:
            return False
        else:
            return True
    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True