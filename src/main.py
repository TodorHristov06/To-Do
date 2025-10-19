from task_manager import TaskManager

def main():
    manager = TaskManager()
    manager.load_from_file()  # Load existing tasks

    while True:
        print("\n===== Python To-Do App =====")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(task)

        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                manager.create_task(title)
                manager.save_to_file()
            else:
                print("⚠️ Title cannot be empty!")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                manager.mark_task_done(task_id)
                manager.save_to_file()
            except ValueError:
                print("⚠️ Please enter a valid number for ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                manager.remove_task(task_id)
                manager.save_to_file()
            except ValueError:
                print("⚠️ Please enter a valid number for ID.")

        elif choice == "5":
            manager.save_to_file()
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()