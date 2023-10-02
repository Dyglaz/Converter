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

    @staticmethod
    def convert_weight(value, source_unit, target_unit):
        american_units = {
            'oz': 0.02835,  # Унции
            'lb': 0.453592  # Фунты
        }

        russian_units = {
            'лот': 0.012797,  # Лоты
            'золотник': 0.004266,  # Золотники
            'доля': 0.0000444,  # Доли
            'фунт': 0.409512  # Фунты
        }

        si_units = {
            'g': 0.001,  # Граммы
            'kg': 1,  # Килограммы
            'tonne': 1000  # Тонны
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

    @staticmethod
    def convert_currency(value, source_currency, target_currency):
        rates = {
            'USD': 1,  # Доллары
            'RUB': 96.04,  # Рубли
            'EUR': 0.94,  # Евро
            'GBP': 1.23  # Фунты стерлингов
        }

        conversion_factor = 1

        if source_currency in rates and target_currency in rates:
            conversion_factor = rates[target_currency] / rates[source_currency]

        target_value = value * conversion_factor

        return round(target_value, 3)