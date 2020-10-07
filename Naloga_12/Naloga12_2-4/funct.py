def cube_function(number):
    result = number * number * number
    return result


def steps_counter(distance, step_length):
    number_of_steps = distance / step_length
    return number_of_steps


def absolute_difference(number1, number2):
    if number1 > number2:
        return  number1-number2
    else:
        return number2-number1
