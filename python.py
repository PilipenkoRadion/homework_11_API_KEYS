import requests
url = "https://restcountries.com/v3.1/name/ukraine"
url_1 = "https://catfact.ninja/fact"
url_2 = "https://zenquotes.io/api/random"
content_save = requests.get(url)
content_save_information = content_save.json()

content_save_1 = requests.get(url_1)
content_save_information_1 = content_save_1.json()

content_save_2 = requests.get(url_2)
content_save_information_2 = content_save_2.json()

population = content_save_information[0]["population"]
formated_population = f"{population:,}"


lat = content_save_information[0]["latlng"][0]
lnt = content_save_information[0]["latlng"][1]


print("--ІНФОРМАЦІЯ ПРО КРАЇНУ--")
print("Офицальное название:", content_save_information[0]["name"]["official"])
print("Столица:", content_save_information[0]["capital"][0])
print("Прапор:", content_save_information[0]["flag"])
print("Населення", [formated_population], "осіб")
print("Географічне положення", content_save_information[0]["name"]["common"], "размещенна приблизительно на ширине", lat, "и длине", lnt)





print("--ВИПАДКОВИЙ ФАКТ ДЛЯ РОЗВАГИ--")
print("Длина шутки:",content_save_information_1["length"], "слова")
print("Шутка:", content_save_information_1["fact"])





print("Шутка 1:",content_save_information_2[0]["q"], "Хахахах")
print("Шутка 2:",content_save_information_2[0]["a"], "Тебе и правда смешно?")
print("Шутка 3:", content_save_information_2[0]["h"], "Ты правда понимаешь Английский?")