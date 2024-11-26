def calculate_total_price(product_price, discount_price, quantity_purchased):
    """Calculates the total amount of money to be paid

    Args:
        product_price (int): Price of the product being bought
        discount_price (int): The discount to be applied    
        quantity_purchased (int): The amount of products being bought

    Returns:
        int: Total amount of money to be paid
    """
    final_price = product_price - discount_price
    total_amount = final_price * quantity_purchased
    return total_amount

variable_42 = 42
hello_world = "Hello, World!"
temporary_value = 3.14