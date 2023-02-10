class DataCapture():
    def __init__(self):
        self.all_numbers_list = []
        self.validator = Validator(int)

    def add(self, number):
        number = self.validator.validate(number)
        self.all_numbers_list.append(number)

    def build_stats(self):
        highest = 0
        for number in self.all_numbers_list:
            if number > highest:
                highest = number
        highest += 1
        grouped_numbers = [None]*highest
        for number in self.all_numbers_list:
            if grouped_numbers[number] is None:
                grouped_numbers[number] = number
            else:
                grouped_numbers[number] = str(grouped_numbers[number]) +\
                    ' ' + str(number)

        return Stats(grouped_numbers, highest, self.validator)


class Stats():
    def __init__(self, numbers_list, highest_number, validator):
        self.numbers_list = numbers_list
        self.highest_number = highest_number
        self.validator = validator

    def less(self, number):
        number = self.validator.validate(number)
        result = ''
        for i in range(number):
            if self.numbers_list[i] is not None:
                result += str(self.numbers_list[i]) + ' '
        print(result)

    def greater(self, number):
        number = self.validator.validate(number)
        result = ''
        for i in range(number+1, self.highest_number):
            if self.numbers_list[i] is not None:
                result += str(self.numbers_list[i]) + ' '
        print(result)

    def between(self, lower_limit, upper_limit):
        lower_limit = self.validator.validate(lower_limit)
        upper_limit = self.validator.validate(upper_limit)
        result = ''
        for i in range(lower_limit, upper_limit):
            if self.numbers_list[i] is not None:
                result += str(self.numbers_list[i]) + ' '
        print(result)


class Validator():
    def __init__(self, type):
        self.type = type
    def validate(self, val):
        if isinstance(val, int):
            return val
        else:
            raise TypeError("Only integers are allowed")
