from task_manager import TaskManager

def show_tasks(manager):
    tasks = manager.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return False
    print("\nCurrent tasks:")
    for task in tasks:
        print(task)
    return True

def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\n===== Python To-Do App =====")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(manager)

        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                task = manager.create_task(title)
                manager.save_to_file()
                print(f"✅ Task added: {task}")
            else:
                print("⚠️ Title cannot be empty!")

        elif choice == "3":
            if show_tasks(manager):
                try:
                    task_id = int(input("Enter task ID to mark done: "))
                    if task_id in manager.tasks:
                        manager.mark_task_done(task_id)
                        manager.save_to_file()
                        print(f"✅ Task marked as done: {manager.tasks[task_id]}")
                    else:
                        print("⚠️ Task ID not found.")
                except ValueError:
                    print("⚠️ Please enter a valid number.")

        elif choice == "4":
            if show_tasks(manager):
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    if task_id in manager.tasks:
                        manager.remove_task(task_id)
                        manager.save_to_file()
                        print("🗑️ Task deleted.")
                    else:
                        print("⚠️ Task ID not found.")
                except ValueError:
                    print("⚠️ Please enter a valid number.")

        elif choice == "5":
            manager.save_to_file()
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid option, choose 1-5.")


if __name__ == "__main__":
    main()
