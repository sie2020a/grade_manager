import csv

students =  {} #辞書

def get_score(subject): #成績入力の際、数字ではなく文字が入力された場合の対処
    while True:
        try:
            return float(input(f"{subject}の成績:"))
        except ValueError:
            print("数字を入力してください")


# ===== 成績登録機能 =====
def input_grades ():
    print("成績を入力してください(終了するときは「end」)")

    while True :
        name = (input("生徒の名前:"))
        if name == "end":
            break
        
        japanese = get_score("国語")
        math = get_score("数学")
        science = get_score("理科")
            
        average = (japanese + math + science ) / 3

        students[name] = {
            "国語": japanese,
            "数学": math,
            "理科": science,
            "平均": average
        }

     
        print(f"{name}さんの成績が登録されました（平均:{average:.2f}点）")

# ===== 修正機能 =====
def edit_grades():
    name = input("修正したい生徒の名前:")
    if name in students:
        print(f"{name}さんの現在の成績:")
        for subject, score in students[name].items():
            if subject != "平均":
                print(f"{subject}: {int(score)}点")
            else:
                print(f"{subject}: {score:.2f}点")
                
        subject = input("修正したい教科名:")
        if subject in students[name]:
            new_score = float(input(f"{subject}の新しい点数を入力:"))
            students[name][subject] = new_score
            
            total = 0
            for sub in ["国語", "数学", "理科"]:
                total += students[name][sub]
            students[name]["平均"] =total / 3
            print(f"{name}さんの{subject}の点数を修正しました。")
            
        else:
            print("その教科は存在しません")
            
    else:
        print("その名前の生徒は登録されていません")

# ===== 成績表示機能 =====
def show_student():
    name = input("成績を表示したい生徒の名前:")
    if name in students:
        print(f"{name}さんの成績:")
        for subject, score in students[name].items():
            if subject != "平均":
                print(f"{subject}: {int(score)}点")
            else:
                print(f"{subject}: {score:.2f}点")
    else:
        print("その名前の生徒は登録されていません。")
        
# ===== 全生徒の成績一覧表示 =====
def show_all_students():
    if not students:
        print("データがありません。")
        return
    print("全生徒の成績:")
    for name, scores in students.items():
        print(f"\n{name}さん:")
        for subject, score in scores.items():
            if subject != "平均":
                print(f"  {subject}: {int(score)}点")
            else:
                print(f"  {subject}: {score:.2f}点")
        

# ===== CSV保存機能 =====
def save_to_csv(filename="grades.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # ヘッダー行を書き込む
        writer.writerow(["名前", "国語", "数学", "理科", "平均"])
        # students辞書の中身を行ごとに書き込む
        for name, scores in students.items():
            writer.writerow([
                name,
                scores["国語"],
                scores["数学"],
                scores["理科"],
                scores["平均"]
            ])
    print("CSVに保存しました。")

# ===== CSV読み込み機能 =====
def load_from_csv(filename="grades.csv"):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students[row["名前"]] = {
                    "国語": float(row["国語"]),
                    "数学": float(row["数学"]),
                    "理科": float(row["理科"]),
                    "平均": float(row["平均"])
                }
        print("CSVから読み込みました。")
    except FileNotFoundError:
        print("CSVファイルが見つかりませんでした。")
        