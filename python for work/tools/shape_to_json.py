import codecs
import json

import geopandas as gps

class Shapefile():
    def __init__(self, path: str, file_name: str, form: str, work_directory: str):
        self.path = path
        self.file_name = file_name
        self.form = form
        self.work_directory = work_directory


    def shape_to_geojson(self):
        # Чтение файлов из шейпа и перевод их в GeoJson
        try:
            zipfile = self.path + self.file_name + "." + self.form
            file = gps.read_file(zipfile)
            file.to_file(self.work_directory + self.file_name + '.geojson', driver='GeoJSON',
                         encoding='utf-8')
            print("Данные успешно переведены по пути " + self.work_directory + self.file_name + ".geojson")

        except EOFError as e:
            print(e)
            print("Не удалось перевести данные в GeoJson")

        # Чтение данных из GeoJson

        try:
            file_json = codecs.open(self.work_directory + self.file_name + '.geojson', "r",
                                    "utf_8_sig")
            json_read = file_json.read()
            file_json.close()
            json_data = json.loads(json_read)
            print("Данные успешно прочитаны")

        except EOFError as e:
            print(e)
            print("Ошибка при чтении файла")

        return json_data
