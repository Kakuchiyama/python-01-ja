def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp = user_input = input("温度を入力してください(fまたはcで単位を記入):")

    #華氏の場合は、摂氏に変換
    if user_input[-1] == "c" :
        input_temp = int(user_input[:-1]) #文字列から整数に変換
        f_temp_change = (input_temp * 9 / 5) + 32
        f_temp = str(f_temp_change)
        print(f_temp + "f")

    elif user_input[-1] == "f":
        input_temp = int(user_input[:-1]) #文字列から整数に変換
        c_temp_change = 9 / 5 * (input_temp - 32)
        c_temp = str(c_temp_change)
        print(c_temp + "c")
    
    return temp



convert()
