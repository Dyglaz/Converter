class Converter:
    @staticmethod
    def convert_length(value, source_unit, target_unit):
        american_units = {
            'in': 0.0254,  # Дюймы
            'ft': 0.3048,  # Футы
            'yd': 0.9144,  # Ярды
            'mi': 1609.344  # Мили
        }

        russian_units = {
            'вершок': 0.04445,  # Вершки
            'аршин': 0.7112,  # Аршины
            'сажень': 2.1336,  # Сажени
            'верста': 1066.8  # Версты
        }

        si_units = {
            'mm': 0.001,  # Миллиметры
            'cm': 0.01,  # Сантиметры
            'm': 1,  # Метры
            'km': 1000  # Километры
        }

        conversion_factor = 1

        if source_unit in american_units and target_unit in american_units:
            conversion_factor = american_units[source_unit] / american_units[target_unit]
        elif source_unit in american_units and target_unit in russian_units:
            conversion_factor = american_units[source_unit] / russian_units[target_unit]
        elif source_unit in american_units and target_unit in si_units:
            conversion_factor = american_units[source_unit] / si_units[target_unit]
        elif source_unit in russian_units and target_unit in american_units:
            conversion_factor = russian_units[source_unit] / american_units[target_unit]
        elif source_unit in russian_units and target_unit in russian_units:
            conversion_factor = russian_units[source_unit] / russian_units[target_unit]
        elif source_unit in russian_units and target_unit in si_units:
            conversion_factor = (russian_units[source_unit]) / si_units[target_unit]
        elif source_unit in si_units and target_unit in american_units:
            conversion_factor = si_units[source_unit] / american_units[target_unit]
        elif source_unit in si_units and target_unit in russian_units:
            conversion_factor = si_units[source_unit] / russian_units[target_unit]
        elif source_unit in si_units and target_unit in si_units:
            conversion_factor = (si_units[source_unit]) / si_units[target_unit]

        target_value = value * conversion_factor

        return round(target_value, 3)