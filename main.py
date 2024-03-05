import os

def create_tree(height, output_file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(current_dir, output_file_name) # Немного изменил логику, вместо указания полного пути я сохраняю файл в коренной директории

    with open(output_file_path, 'w') as file:
        w = " " * (height) + "W\n"
        file.write(w) # Первая линия

        single_star = " " * height + "*\n"
        file.write(single_star) # Вторая линия

        i = 3 
        while i < height + 1: # Построение елки в зависимости от этажей
            spaces = ' ' * (height - i)
            stars = '*' * (2 * i - 1)
            dog_left = '@' if i % 4 == 3 else ''
            dog_right = '@' if i % 4 == 1 else ''
            tree_line = f"{spaces}{dog_left}{stars}{dog_right}\n"
            file.write(tree_line)
            i = i + 2

        empty_spaces = ' ' * (height -1 ) # Последнии две линии
        trunk = empty_spaces + "TTTTT\n" + empty_spaces + "TTTTT\n"
        file.write(trunk)

if __name__ == "__main__":
    try:
        num_floors = int(input("Enter a level of the tree: ")) # Количество этажей елки
        output_filename = input("Enter a name of the output file: ") # Название выходного файла

        create_tree(num_floors, output_filename) # Создание елки
        print(f"'{output_filename}' File was created.")
    except Exception as e:
        print(f"Error occured: {e}")