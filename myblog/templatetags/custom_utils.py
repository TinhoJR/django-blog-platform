from django import template


register = template.Library()


@register.filter(name="emojify")
def emojify(value):
    return value.lower()
    # return value + "YOO"


@register.filter("reverse")
def reverse(value):
    if value == "":
        return "N/A"
    
    # DETERMINE THE VALUE DATA TYPE
    original_type = type(value)
    if original_type not in (str,list,tuple):
        return value

    temporary_result = []
    current_p = len(value) - 1

    while current_p >= 0:
        temporary_result.append(value[current_p])
        current_p -= 1

    # USE DATA TYPE TO CONVERT VALUE TO ORIGINAL TYPE
    if original_type == str:
        return "".join(temporary_result)
    elif original_type == list:
        return temporary_result
    elif original_type == tuple:
        return tuple(temporary_result)


    