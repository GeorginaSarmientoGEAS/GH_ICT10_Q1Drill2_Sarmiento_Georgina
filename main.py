from pyscript import display, document

def add_numbers(e): # adds numbers
    document.getElementById('result').innerHTML="  " 
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}.', target='result')

def subtract_numbers(e): # subtracts numbers
    document.getElementById('result').innerHTML="  " 
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {difference}.', target='result')

def multiply_numbers(e): # multiplies numbers
    document.getElementById('result').innerHTML="  " 
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {product}.', target='result')

def divide_numbers(e): # divides numbers
    document.getElementById('result').innerHTML="  " 
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number / second_number

    display(f'The quotient of {first_number} and {second_number} is {quotient}.', target='result')
