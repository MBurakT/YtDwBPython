def calculate_discount(price: float, rate: float) -> float:
    """
    Calculate the final price after applying a discount.
    Args:
        price (float): Original Product Price.
        rate (float): Dİscount Rate as numbers (e.g 20 for 20%).
    Returns:
        final_price (float): Final Price after applying discount.
    """
    final_price = price - (price * rate / 100)
    return final_price


print("Calculating Discount")
print(calculate_discount(80, 20))
help(calculate_discount)
