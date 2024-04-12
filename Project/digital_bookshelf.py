#操作メニューの表示
def opening():
     print("================================================")
     print("Welcome to your personal books digital library! ")
     print("================================================")
     print("1: Add a Book")
     print("2: Edit a Book")
     print("3: Search for Books")
     print("4: Delete a Book")
     print("5: View Library Stats")
     print("6: Exit app")
     print("Please select from 1 to 6")
     user_choise = int(input("your choice: ")) #初回操作の選択
     return user_choise

#リストの初期化
book_shelf = [] 

#idを定義する
def id(num=0):
      for num in range(num<100):
           num = 0
           return num + 1

#ステータスを定義する
def status():
     print("本のステータスを選んでください[1:既読、2:未読]")
     status_input = int(input("your choice: "))
     if status_input == 1:
          read_status = "既読"
     elif status_input == 2:
          read_status = "未読"
     return read_status


#辞書の作成
def book_dict():
      print("本のタイトルを記入してください")
      title = str(input("title: "))
      book_data = {
           "id":id(),
           "title":title,
           "read_status":status()
           }
      return book_data

#id = int()
title = str()
#read_status = bool()

#「1: Add a Book」を選択した場合
def add():
     # print("追加する本のタイトルを記入してください：") #追加するタイトルの入力
     # title = input()
     # book_data = {"id":id(), "title":title, "read_status":status()}
      book_shelf.append(book_dict())
      print(book_shelf)
      return book_shelf

#「2: Edit a Book」を選択した場合
def edit():
      print("次の項目から操作を選択してください")
      print("1:タイトルの編集、2:ステータスの編集") #編集内容の選択
      edit_type = int(input())
      if edit_type == 1:
           print("格納されていれ")
           print(book_shelf) 
           print("編集したい本のタイトルを入力してください")
           title = input()
           if title in book_dict() == True:
                print("新しいタイトルを入力してください")
                new_title = input()
                book_dict["title"] = new_title
           print(book_shelf)
      elif edit_type == 2:
           print(1)
      return book_shelf

#「3: Search for Books」を選択した場合
def search():
      print("検索したい本のタイトルを入力してください")
      title = input()

      return

#「4: Delete a Book」を選択した場合
def delete():
     return

#「5: View Library Stats」を選択した場合
def view_stats():
      print("閲覧したい統計情報の番号を選択してください")
      print("1:本の総数、2:既読の本の数、3:未読の本の数")
      print(input("your choise is :"))
      return

# ユーザーの選択に合わせた画面の遷移       
user_choise = int()
while (user_choise != 6): 
     user_choise = opening()
     if user_choise == 1:
          add()
     elif user_choise == 2:
          edit()
     elif user_choise == 3:
          search()
     elif user_choise == 4:
          delete()
     elif user_choise == 5:
          view_stats()
     elif user_choise == 6: #6を選択するとループから抜け出す
          print("================")
          print(" see you again! ")
          print("================")



     

#      return
# elif int(user_choise) == 2:
#     surch_book = input("編集したい本のタイトルを記入してください：")
#     x = book_list.index(surch_book) #編集したい本のリストのインデックスを取得する
#     re_title = input("修正後のタイトルを記入してください：")
#     book_list[x] = re_title
#     print(book_list)

# #「3: Search for Books」を選択した場合
# def search():
#      return
# elif int(user_choise) == 3:
#     surch_book = input("検索したい本のタイトルを記入してください：")
#     if surch_book in book_list and True:
#             print("この本は本棚にあります")
#     else :
#             print("この本は本棚にありません")

# #「4: Delete a Book」を選択した場合
# def delete():
#      return
# elif int(user_choise) == 4:
#     remove_book = input("本棚から削除したい本のタイトルを記入してください：")
#     book_list.remove(remove_book)
#     print(book_list)

# #「5: View Library Stats」を選択した場合
# def stats():
#      return
# elif int(user_choise) == 5:
#     user_choise = input("閲覧したい統計情報の番号を選択してください：\n1:本の総数、2:既読の本の数、3:未読の本の数\nyour choise is :")
#     if int(user_choise) == 1:
#          book_count = len(book_list)
#          print("本棚に格納されている本の数は、" + str(book_count) + "冊です")

#     elif int(user_choise) == 2:
#          book_count = len(book_list)
         
         
#     elif int(user_choise) == 3:
#          book_count = len(book_list)
         
         

# # 6: 「Exit app」を選択した場合

# #1～6以外の数字を入力した場合
# elif (0 < int(user_choise) <= 6) == False:
#      print("入力エラー：選択肢の番号を確認し、入力してください")

# elif user_choise == "":
#      print("入力エラー：選択肢の番号を確認し、数字を入力してください")
    
