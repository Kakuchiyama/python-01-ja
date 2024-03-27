#まずは、userに操作を選択してもらう
choise = input("ようこそ電子書棚へ！以下から選択したい項目の数字で入力してください。 1:本の追加、2:本の編集、3:本の検索、4:本の削除、5:ブックシェルフの統計情報の表示  your choice is :")

#本棚を作成
book_list = ["赤毛のアン"]

#「1:本の追加」を選択した場合
if choise == 1:
    add_list = input("追加したい本のタイトルを記入してください：")
    append.book_list(add_list)

#「2:本の編集」を選択した場合
elif choise == 2:
    surch_book = input("編集したい本のタイトルを記入してください：")
    x = book_list.index(surch_book) #編集したい本のリストのインデックスを取得する
    re_title = input("修正後のタイトルを記入してください：")
    book_list[x] = re_title

#「3:本の検索」を選択した場合
elif choise == 3:
    surch_book = input("検索したい本のタイトルを記入してください：")
    if surch_book in book_list and True:
            print("この本は本棚にあります")
    else :
            print("この本は本棚にありません")

#「4:本の削除」を選択した場合
elif choise == 4:
    remove_book = input("本棚から削除したい本のタイトルを記入してください：")
    remove.book_list(remove_book)

#「5:ブックシェルフの統計情報の表示」を選択した場合
elif choise == 5:
    print("本棚に格納されている本の数は、" + len(book_list) + "冊です")

# 選択肢にない番号を入力している場合
elif (0 < int(choise) <= 5) == False:
     print("入力エラー：選択肢の番号を確認し、半角で番号を入力してください")