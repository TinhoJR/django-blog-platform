from django import template
import string

register = template.Library()


# CONVERT TO LIST
@register.filter(name="list_converter")
def list_converter(value):
    return value.split(" ")


# @register.filter(name="listconverter")
# def list_converter(value):
#     return value.upper()

# CRYPTO CONVERSION
@register.filter(name="target_currency")
def target_currency(price,target):
    convert_crypto = {
        "BTC" : 0.00001506,
        "ETH" : 0.00016
    }

    converted = price * convert_crypto[target]

    return str(converted) + " " + target
 

# SIMPLE ADDITION 
@register.simple_tag(name="add_numbers") 
def add_numbers(f_num,s_num):
    answer = f_num + s_num

    return answer


# GET HALF (DIVIDE BY TWO)
@register.simple_tag(name="divide_by_two") 
def divide_by_two(num):
    answer = num / 2

    return answer


# DISCOUNT CALCULATOR
@register.filter(name="calculate_discount")
def calculate_discount(price,discount):

    discount_amount = (price * discount) / 100
    total_amount = price - discount_amount

    return int(total_amount)
    
# TAX CALCULATOR
@register.filter(name="calculate_tax")
def calculate_tax(price,tax):

    tax_amount = (price * tax) / 100
    total_amount = price + tax_amount

    return total_amount

# PERCENTAGE CALCULATOR TRICK
@register.filter(name="calculate_percentage")
def calculate_percentage(number,percentage):

    total_amount = (number * percentage) / 100

    return total_amount

# PERCENTAGE CALCULATOR TRICK
@register.filter(name="calculate_percentage_trick")
def calculate_percentage_trick(num,percentage):

    total_amount = (num / 10) * (percentage / 10)
     
    return total_amount


# FREQUENCY MAP
@register.filter(name="frequency")
def frequency(value):

    if isinstance(value,(str,list,tuple)):
        count = {}
        for v in value:
            if v in count:
                count[v] += 1
            else:
                count[v] = 1  
        return count 
    
    else:
        return value 

# FORMAT FREQUENCY
@register.filter("format_frequency")
def format_frequency(f_dict):
    if isinstance(f_dict,dict):
       formatted = ""
       for key,value in f_dict.items():
            formatted += f"{key} appeared {value} time(s) <br>" 

       return formatted

    else:
        return f_dict   


# NAME INITIALS 

@register.filter("name_initials")
def name_initials(value):
    clean_name = value.strip()
    if clean_name == "":
        return value
    
    result = ""  
    name_list = clean_name.split()
    for name in name_list:
        result += name[0].capitalize()

    return result    

# COUNT WORDS IN A TEXT (NUMBERS INCLUDED)
@register.filter("word_count")
def word_count(value):
    text = value.strip()
    if text == "":
        return value
    
    # FIND ALL CHARACTERS AND REMOVE THE TWO NEEDED
    punctuation = string.punctuation.replace("'","").replace("-","")
    text = text.translate(str.maketrans("","",punctuation))

    result_list = text.split()
    return len(result_list)
      

# CHARACTER COUNT
@register.filter("char_count")
def char_count(value):

    if value == "":
        return "None"
    
    result = len(value)
    return result
    
              