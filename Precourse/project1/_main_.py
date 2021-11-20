from Post import Post
import os, csv

# 데이터 불러오기
file_path = "./data.csv"

post_list = []

if os.path.exists(file_path):
    print("게시글 로딩중...\n")
    f = open(file_path, "r")
    reader = csv.reader(f)
    for d in reader:
        post_list.append(Post(int(d[0]), d[1], d[2], int(d[3])))
    f.close()
else:
    f = open(file_path, "w")
    f.close()


# 게시글 쓰기 함수
def write_post():
    print("\n\n- 게시글 쓰기 -")
    title = input("제목을 입력해주세요 : ")
    content = input("내용을 입력해주세요 : ")
    if len(post_list) == 0 : id = 1
    else : id = post_list[-1].get_id() + 1
    post_list.append(Post(id, title, content, 0))
    print("# 게시글이 등록되었습니다.")

# 게시글 목록
def list_post():
    print("\n\n- 게시글 목록 -")
    id_list =[]
    for i in post_list:
        print(i)
        id_list.append(i.get_id())
    while True:
        print("글번호 선택 (-1 입력으로 메뉴로 돌아가기): ")
        try:
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해주세요")


# 글 상세 페이지
def detail_post(id):
    target_post = 0
    for post in post_list:
        if post.get_id() == id:
            post.view_count_increment()
            print(post)
            target_post = post
            break

    while True:
        print("수정:1, 삭제:2 (메뉴로 돌아가기 위해서는 -1)")
        try:
            choice = int(input(">>>"))
            if choice == 1:
               update_post(target_post)
               break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("invalid input")
        except ValueError:
            print("input intergers")

# 게시글 삭제
def delete_post(target):
    post_list.remove(target)

# 게시글 수정
def update_post(target):
    print("\n\n게시글 수정")
    title = input("제목을 입력해주세요 : ")
    content = input("본문을 입력해주세요 : ")
    target.set_post(target.get_id(), title, content, target.get_view_count())
    print("게시글 수정 완료")

# 데이터 저장
def list_load():
    f = open(file_path, "w")
    writer = csv.writer(f)
    for data in post_list:
        writer.writerow([data.get_id(), data.get_title(), data.get_content(), data.get_view_count()])
    f.close()

# 주 메뉴
while True:
    print("\n\n- FC Blog -")
    print("- 메뉴를 선택해주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("input number!")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            list_load()
            print("프로그램 종료")
            break