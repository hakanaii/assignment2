import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(tasks):
    task = input("추가할 할 일을 입력하세요: ").strip()
    if not task:
        print("할 일 내용이 비어 있습니다. 다시 입력해주세요.")
        return
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("할 일이 추가되었습니다.")


def show_tasks(tasks):
    if not tasks:
        print("할 일이 없습니다.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['task']}")


def get_valid_number(tasks, prompt):
    try:
        number = int(input(prompt))
    except ValueError:
        print("숫자를 입력해주세요.")
        return None
    if 1 <= number <= len(tasks):
        return number
    print("잘못된 번호입니다.")
    return None


def toggle_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    number = get_valid_number(tasks, "완료/미완료를 전환할 번호를 입력하세요: ")
    if number is None:
        return
    tasks[number - 1]["done"] = not tasks[number - 1]["done"]
    save_tasks(tasks)
    state = "완료" if tasks[number - 1]["done"] else "미완료"
    print(f"{number}번 할 일이 '{state}' 상태로 변경되었습니다.")


def edit_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    number = get_valid_number(tasks, "수정할 번호를 입력하세요: ")
    if number is None:
        return
    new_text = input("새로운 내용을 입력하세요: ").strip()
    if not new_text:
        print("내용이 비어 있어 수정을 취소합니다.")
        return
    tasks[number - 1]["task"] = new_text
    save_tasks(tasks)
    print("수정되었습니다.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    number = get_valid_number(tasks, "삭제할 번호를 입력하세요: ")
    if number is None:
        return
    removed = tasks.pop(number - 1)
    save_tasks(tasks)
    print(f"'{removed['task']}'이(가) 삭제되었습니다.")


def show_stats(tasks):
    total = len(tasks)
    if total == 0:
        print("할 일이 없습니다.")
        return
    done = sum(1 for task in tasks if task["done"])
    percent = (done / total) * 100
    print(f"전체 {total}개 중 {done}개 완료 ({percent:.1f}%)")


def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List =====")
        print("1. 할 일 추가")
        print("2. 할 일 보기")
        print("3. 완료/미완료 전환")
        print("4. 할 일 수정")
        print("5. 삭제")
        print("6. 통계 보기")
        print("7. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            show_stats(tasks)
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()