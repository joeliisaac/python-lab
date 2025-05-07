

def discount_calculator(discount_percentage, tax):

    def apply_discount(price):
        discounted_price =  (price - (price * (discount_percentage/100)))
        return discounted_price + (discounted_price * (tax/100))
        
    return apply_discount

apply_20_discount = discount_calculator(20, 3.6)
print(apply_20_discount(100))  
