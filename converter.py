class Converter:
    @staticmethod
    def convert_length(value, source_unit, target_unit):

        conversion_factor = 1

        target_value = value * conversion_factor

        return round(target_value, 3)