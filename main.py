import requests
from bs4 import BeautifulSoup
import tkinter as tk
# функция для калорийности
def get_calories_data_ordered():
    url = 'https://rsport.ria.ru/20220514/kaloriynost-1788483172.html?ysclid=lxt2u1gqcl461725737'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        if tables:
            data = ''
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['th', 'td'])
                    for cell in cells:
                        data += cell.get_text(strip=True) + ' '
                    data += '\n'
            return data
        else:
            return 'Таблицы с данными не найдены'
    else:
        return 'Ошибка при отправке запроса на сайт'



# функция для упражнений
def get_exercises_data():
    url = 'https://multiurok.ru/files/kompleks-obshcherazvivaiushchikh-uprazhnenii-v-tab.html?ysclid=lxt3mtfjna754993115'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        exercise_data = ''
        for table in soup.find_all('table'):
            for td in table.find_all('td'):
                exercise_data += td.get_text(strip=True) + '\n'
        return exercise_data
    else:
        return 'Ошибка при отправке запроса на сайт'


# функция для советов

def get_health_tips():
    url = 'https://www.fbuz04.ru/index.php/o-centre/press-sluzhba/10-samykh-glavnykh-pravil-zdorovogo-obraza-zhizni?ysclid=lxt6zejyv9918213684'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tips_data = ''
        for item in soup.find_all('h2'):
            tips_data += item.get_text(strip=True) + '\n'
        paragraph_list = soup.find_all('p')
        for paragraph in paragraph_list:
            tips_data += paragraph.get_text(strip=True) + '\n\n'
        return tips_data
    else:
        return 'Ошибка при отправке запроса на сайт'



# отображение данных
def show_data(data):
    data_window = tk.Toplevel(root)
    data_text = tk.Text(data_window, wrap=tk.WORD)
    data_text.insert(tk.END, data)
    data_text.pack()

    # текстовые настройки
    data_text.config(font=('Arial', 12), padx=20, pady=20)

# функция для обработки кнопки калорийности
def get_calories_button_click():
    data = get_calories_data_ordered()
    show_data(data)

root = tk.Tk()
root.title("Приложение здорового образа жизни")
root.geometry("800x600")
background_image = tk.PhotoImage(file="C:/Users/kunki/PycharmProjects/pythonProject/myaso-original.png")  # Путь к изображению заднего фона
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# функция для обработки кнопки упражнений
def get_exercises_button_click():
    data = get_exercises_data()
    show_data(data)

# функция для обработки кгнопки советов
def get_health_tips_button_click():
    data = get_health_tips()
    show_data(data)

# кнопочки
calories_button = tk.Button(root, text='Получить данные о калорийности продуктов', command=get_calories_button_click, font=('Arial', 14))
calories_button.pack()
calories_button.config(width=40, height=2, bg='white')
exercises_button = tk.Button(root, text='Получить данные о физических упражнениях', command=get_exercises_button_click, font=('Arial', 14))
exercises_button.pack()
exercises_button.config(width=40, height=2, bg='blue')
health_tips_button = tk.Button(root, text='Получить советы по здоровому образу жизни', command=get_health_tips_button_click, font=('Arial', 14))
health_tips_button.pack()
health_tips_button.config(width=40, height=2, bg='red')

root.mainloop()
