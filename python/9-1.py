class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):  #此处需加上形参self
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):      #此处需加上形参self
        print("the restaurant is open")

myrestaurant = Restaurant('peace',"bbq")    #实参需使用string
myrestaurant.describe_restaurant()
myrestaurant.open_restaurant()
