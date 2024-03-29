#まずは、userに操作を選択してもらう
choise = input("ようこそ電子書棚へ！\n以下から選択したい項目の数字で入力してください。\n 1:本の追加、2:本の編集、3:本の検索、4:本の削除、5:ブックシェルフの統計情報の表示 \n your choice is :")



#本棚と辞書(keyはid,title,read_status)を作成
book_list = [{"id" : "1", "title": "赤毛のアン", "read_status" :"read"},
             {"id" : "2", "title": "ハリーポッターと賢者の石", "read_status" :"read"},
             {"id" : "3", "title": "魔女の宅急便", "read_status" :"unread"},
             {"id" : "4", "title": "オズの魔法使い", "read_status" :"unread"},
             {"id" : "5", "title": "星の王子さま", "read_status" :"unread"}]


#「1:本の追加」を選択した場合
if int(choise) == 1:
    add_book = input("追加したい本のタイトルを記入してください：")
    read_status = input("上記で追加したい本のステータスを選んでください。\n1:既読、2:未読\nyour choise is: ")
    if int(read_status) == 1:
         input_status = "read"
    elif int(read_status) == 2:
         input_status = "unread"
    add_list = {"id" : "5", "title": add_book, "read_status" :input_status}
    book_list.append(add_list)
    print(book_list)

#「2:本の編集」を選択した場合
elif int(choise) == 2:
    surch_book = input("編集したい本のタイトルを記入してください：")
    x = book_list.index(surch_book) #編集したい本のリストのインデックスを取得する
    re_title = input("修正後のタイトルを記入してください：")
    book_list[x] = re_title
    print(book_list)

#「3:本の検索」を選択した場合
elif int(choise) == 3:
    surch_book = input("検索したい本のタイトルを記入してください：")
    if surch_book in book_list and True:
            print("この本は本棚にあります")
    else :
            print("この本は本棚にありません")

#「4:本の削除」を選択した場合
elif int(choise) == 4:
    remove_book = input("本棚から削除したい本のタイトルを記入してください：")
    book_list.remove(remove_book)
    print(book_list)

#「5:ブックシェルフの統計情報の表示」を選択した場合
elif int(choise) == 5:
    user_choise = input("閲覧したい統計情報の番号を選択してください：\n1:本の総数、2:既読の本の数、3:未読の本の数\nyour choise is :")
    if int(user_choise) == 1:
         book_count = len(book_list)
         print("本棚に格納されている本の数は、" + str(book_count) + "冊です")

    elif int(user_choise) == 2:
         book_count = len(book_list)
         
         
    elif int(user_choise) == 3:
         book_count = len(book_list)
         
         

# 選択肢にない番号を入力している場合
elif (0 < int(choise) <= 5) == False:
     print("入力エラー：選択肢の番号を確認し、入力してください")
    
