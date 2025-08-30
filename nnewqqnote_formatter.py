def main():
    print("📝 Умный форматировщик заметок")
    print("—" * 50)
    print("Введи строки (по одной). Оставь пустую строку, чтобы закончить.")

    lines = []
    while True:
        line = input("> ")
        if line.strip() == "":
            break
        lines.append(line.strip())

    if not lines:
        print("❌ Ничего не введено. Пока!")
        return

    print("\n✨ Выбери стиль форматирования:")
    print("1. Просто пронумеровать")
    print("2. Смайлики-маркеры")
    print("3. Заголовки (###)")
    print("4. To-do список с [ ]")

    choice = input("\nВведи номер (1–4): ").strip()

    print("\n🎯 Результат:\n")
    if choice == "1":
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line}")

    elif choice == "2":
        icons = ["🔹", "🔸", "✅", "📌", "💡", "🚀", "🌟", "🎯"]
        for i, line in enumerate(lines):
            icon = icons[i % len(icons)]
            print(f"{icon} {line}")

    elif choice == "3":
        for line in lines:
            print(f"### {line}")

    elif choice == "4":
        for line in lines:
            print(f"- [ ] {line}")

    else:
        print("❌ Неверный выбор. Вот просто список:")
        for line in lines:
            print(f"• {line}")

    print("\n💡 Совет: Скопируй результат в заметки (Telegram, Notion, Obsidian и т.д.)")

if __name__ == "__main__":
    main()
