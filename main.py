import grades

def grades_menu():
    while True:
        print("操作したい項目を入力してください")
        menu = input("登録/修正/確認/一覧/保存/読み込み/end:")
        if menu == "end":
            break
        elif menu == "登録":
            grades.input_grades()
        elif menu == "修正":
            grades.edit_grades()
        elif menu == "確認":
            grades.show_student()
        elif menu == "一覧":
            grades.show_all_students()
        elif menu == "保存":
            grades.save_to_csv()
        elif menu == "読み込み":
            grades.load_from_csv()
        else:
            print("無効な選択です。")
        
        
grades_menu()



#ターミナル起動　python3 ~/test/grades/main.py