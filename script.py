def calculate_total(price, tax):
    """
    Calculate the total price including tax.

    Args:
        price (float): The base price.
        tax (float): The tax rate.

    Returns:
        float: Total price after tax.
    """
    return price + (price * tax)
