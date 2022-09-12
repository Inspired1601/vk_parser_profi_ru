import re


class Parser:
    def __init__(self, text):
        self.text = text

    def _extract_data(self, regex):
        matches = re.findall(regex, self.text)
        return [match[0].replace(' ', '') for match in matches]

    def extract_phones(self):
        regex = r'((?<=\D)(8|\+7)[\- ]?\(?\d{3}\)?[\- ]?\d{3}[\- ]?\d{2}[\- ]?\d{2})'
        raw_numbers = self._extract_data(regex)

        cleaned_numbers = []
        chars_to_delete = '()- '
        for number in raw_numbers:
            for char in chars_to_delete:
                number = number.replace(char, '')
            cleaned_numbers.append(number)
        return cleaned_numbers

    def extract_cards(self):
        regex = r'((\d{4}\s?){4})'
        return self._extract_data(regex)

    def extract_urls(self):
        regex = r'((https?:\/\/)[a-zA-Z0-9\.\/\-_]+)'
        return self._extract_data(regex)


# Как использовать:
# 1. Создаёте объект-парсер, передаёте ему текст
# parser = Parser(text)
# 2. Вызываете нужные методы, получаете в ответ списки
# parser.extract_phones()
# parser.extract_cards()
# parser.extract_urls()
