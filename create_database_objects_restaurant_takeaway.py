import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from restaurant_takeaway_setup import Restaurant, Base, MenuItem, Customer, Staff, CustomerOrder, CustomerOrderedItem

engine = create_engine('sqlite:///restaurant_takeaway_system.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
restaurant1 = Restaurant(name="Urban Burger",address="restaurant1 address")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="French Fries", description="with garlic and parmesan",
                     price="2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Sirloin Burger", description="Made with grade A beef",
                     price="7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                     price="1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Iced Tea", description="with Lemon",
                     price=".99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     price="3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Super Stir Fry",address="restaurant2 address")

session.add(restaurant2)
session.commit()


menuItem9 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem9)
session.commit()

menuItem10 = MenuItem(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", 
                    price="25", course="Entree", restaurant=restaurant2)

session.add(menuItem10)
session.commit()

menuItem11 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem11)
session.commit()

menuItem12 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem12)
session.commit()

menuItem13 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem13)
session.commit()

menuItem14 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem14)
session.commit()


# Menu for Panda Garden
restaurant3 = Restaurant(name="Panda Garden",address="restaurant3 address")

session.add(restaurant3)
session.commit()


menuItem15 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="8.99", course="Entree", restaurant=restaurant3)

session.add(menuItem15)
session.commit()

menuItem16 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="6.99", course="Appetizer", restaurant=restaurant3)

session.add(menuItem16)
session.commit()

menuItem17 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     price="9.95", course="Entree", restaurant=restaurant3)

session.add(menuItem17)
session.commit()

menuItem18 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="6.99", course="Entree", restaurant=restaurant3)

session.add(menuItem18)
session.commit()

menuItem19 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="9.50", course="Entree", restaurant=restaurant3)

session.add(menuItem19)
session.commit()


# Menu for Thyme for that
restaurant4 = Restaurant(name="Thyme for That Vegetarian Cuisine",address="restaurant4 address")

session.add(restaurant4)
session.commit()


menuItem20 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="2.99", course="Dessert", restaurant=restaurant4)

session.add(menuItem20)
session.commit()

menuItem21 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="5.99", course="Entree", restaurant=restaurant4)

session.add(menuItem21)
session.commit()

menuItem22 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="4.50", course="Dessert", restaurant=restaurant4)

session.add(menuItem22)
session.commit()

menuItem23 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="6.95", course="Appetizer", restaurant=restaurant4)

session.add(menuItem23)
session.commit()

menuItem24 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="7.95", course="Entree", restaurant=restaurant4)

session.add(menuItem24)
session.commit()

menuItem25 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="6.80", course="Entree", restaurant=restaurant4)

session.add(menuItem25)
session.commit()


# Menu for Tony's Bistro
restaurant5 = Restaurant(name="Tony\'s Bistro", address="restaurant5 address")

session.add(restaurant5)
session.commit()


menuItem26 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="13.95", course="Entree", restaurant=restaurant5)

session.add(menuItem26)
session.commit()

menuItem27 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                     price="4.95", course="Entree", restaurant=restaurant5)

session.add(menuItem27)
session.commit()

menuItem28 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="6.95", course="Entree", restaurant=restaurant5)

session.add(menuItem28)
session.commit()

menuItem29 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="3.95", course="Dessert", restaurant=restaurant5)

session.add(menuItem29)
session.commit()

menuItem30 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="7.95", course="Entree", restaurant=restaurant5)

session.add(menuItem30)
session.commit()


# Menu for Andala's
restaurant6 = Restaurant(name="Andala\'s", address="restaurant6 address")

session.add(restaurant6)
session.commit()


menuItem31 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="9.95", course="Entree", restaurant=restaurant6)

session.add(menuItem31)
session.commit()

menuItem32 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="7.95", course="Entree", restaurant=restaurant6)

session.add(menuItem32)
session.commit()

menuItem33 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="6.50", course="Appetizer", restaurant=restaurant6)

session.add(menuItem33)
session.commit()

menuItem34 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="6.75", course="Appetizer", restaurant=restaurant6)

session.add(menuItem34)
session.commit()

menuItem35 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="7.00", course="Entree", restaurant=restaurant6)

session.add(menuItem35)
session.commit()


# Menu for Auntie Ann's
restaurant7 = Restaurant(name="Auntie Ann\'s Diner", address="restaurant7 address")

session.add(restaurant7)
session.commit()

menuItem36 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="8.99", course="Entree", restaurant=restaurant7)

session.add(menuItem36)
session.commit()


menuItem37 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="2.99", course="Dessert", restaurant=restaurant7)

session.add(menuItem37)
session.commit()

menuItem38 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="10.95", course="Entree", restaurant=restaurant7)

session.add(menuItem38)
session.commit()

menuItem39 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="7.50", course="Appetizer", restaurant=restaurant7)

session.add(menuItem39)
session.commit()

menuItem40 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="8.95", course="Entree", restaurant=restaurant7)

session.add(menuItem40)
session.commit()

menuItem41 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="9.50", course="Entree", restaurant=restaurant7)

session.add(menuItem41)
session.commit()

menuItem42 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="1.99", course="Dessert", restaurant=restaurant7)

session.add(menuItem42)
session.commit()


# Menu for Cocina Y Amor
restaurant8 = Restaurant(name="Cocina Y Amor", address="restaurant8 address")

session.add(restaurant8)
session.commit()


menuItem43 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="5.95", course="Entree", restaurant=restaurant8)

session.add(menuItem43)
session.commit()

menuItem44 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="7.99", course="Entree", restaurant=restaurant8)

session.add(menuItem44)
session.commit()


restaurant9 = Restaurant(name="State Bird Provisions", address="restaurant9 address")
session.add(restaurant9)
session.commit()

menuItem45 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="5.95", course="Appetizer", restaurant=restaurant9)

session.add(menuItem45)
session.commit

menuItem46 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="6.95", course="Dessert", restaurant=restaurant9)

session.add(menuItem46)
session.commit()


menuItem47 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="4.25", course="Dessert", restaurant=restaurant9)

session.add(menuItem47)
session.commit()


print "added menu items!"

# Add fake customers
customer1 = Customer(username='a@a.com',password='d643fa3207b471afd3aefcc93aaf4afe9cac42540fc16c5d49834f7a1e197e9e',email='a@a.com',preferred_delivery_address="Customer Delivery Address 1, Building 1, Country 1",preferred_billing_address="Customer Billing Address 1, Building 1, Country 1",
   phone_number=111,first_name="a",surname="apple")
session.add(customer1)
session.commit()

customer2 = Customer(username='b@b.com',password='e2951e3bfb3c928d670e6c666b7fad57aa76c0d3c96efa025a8ef001f99a3336',email='b@b.com',preferred_delivery_address="Customer Delivery Address 2, Building 2, Country 2",preferred_billing_address="Customer Billing Address 2, Building 2, Country 2",
   phone_number=222,first_name="b",surname="baby")
session.add(customer2)
session.commit()

customer3 = Customer(username='c@c.com',password='921f4606d54eaff3a0af439c1df8e55d6bf23044c13aeb4de54e34f27cd47eb4',email='c@c.com',preferred_delivery_address="Customer Delivery Address 3, Building 3, Country 3",preferred_billing_address="Customer Billing Address 3, Building 3, Country 3",
   phone_number=333,first_name="c",surname="cat")
session.add(customer3)
session.commit()

print "added customers!"

# Add fake customerorders
customerorder1 = CustomerOrder(customer_id=1,customer_username='a@a.com',restaurant_id=1,place_order_time=datetime.datetime(2015,1,1,00,00,00),completion_status=True,total_price=12.48,customerorderhash="a4b9775cad7a19b8563ecf41994868f50ef75403a5942788b15410305be762be",customer_phone_number=111,customer_billing_address="Customer Billing Address 1, Building 1, Country 1",customer_delivery_address="Customer Delivery Address 1, Building 1, Country 1")
session.add(customerorder1)
session.commit()

customerorder2 = CustomerOrder(customer_id=2,customer_username='b@b.com',restaurant_id=2,place_order_time=datetime.datetime(2015,1,2,00,00,00),completion_status=True,total_price=47.99,customerorderhash="71bbddfe53662445523c08653777b8f29b7091c51b8304633a6a4f0e824550b7",customer_phone_number=222,customer_billing_address="Customer Billing Address 2, Building 2, Country 2",customer_delivery_address="Customer Delivery Address 2, Building 2, Country 2")
session.add(customerorder2)
session.commit()

customerorder3 = CustomerOrder(customer_id=3,customer_username='c@c.com',restaurant_id=3,place_order_time=datetime.datetime(2015,1,3,00,00,00),completion_status=True,total_price=25.93,customerorderhash="abcfdc8137354e01336db880806c5660ef0015cadc2596f8316dc45e1c03f37b",customer_phone_number=333,customer_billing_address="Customer Billing Address 3, Building 3, Country 3",customer_delivery_address="Customer Delivery Address 3, Building 3, Country 3")
session.add(customerorder3)
session.commit()

print "added customerorders!"

# Add fake staff
staff1 = Staff(username='chefA@a.com',password='6681696132b4787faec38f833724d4b47d0e354028b032e051fe84b7c0a27cdd',email='chefA@chefA.com',restaurant_id=1)
session.add(staff1)
session.commit()

staff2 = Staff(username='chefB@b.com',password='3acc5bf3907ece5e4b2814cdaeff4fd9bf3701db7dffbac2b43e5828a2f70ce9',email='chefB@chefB.com',restaurant_id=2)
session.add(staff2)
session.commit()

print "added staff!"

# Add fake CustomerOrderedItems
customerOrderedItem1 = CustomerOrderedItem(restaurant_id=1,customer_id=1,customerorder_id=1,menuitem_id=1,menuitem_price=2.99)
session.add(customerOrderedItem1)
session.commit()

customerOrderedItem2 = CustomerOrderedItem(restaurant_id=1,customer_id=1,customerorder_id=1,menuitem_id=2,menuitem_price=5.50)
session.add(customerOrderedItem2)
session.commit()

customerOrderedItem3 = CustomerOrderedItem(restaurant_id=1,customer_id=1,customerorder_id=1,menuitem_id=3,menuitem_price=3.99)
session.add(customerOrderedItem3)
session.commit()

customerOrderedItem4 = CustomerOrderedItem(restaurant_id=2,customer_id=2,customerorder_id=2,menuitem_id=9,menuitem_price=7.99)
session.add(customerOrderedItem4)
session.commit()

customerOrderedItem5 = CustomerOrderedItem(restaurant_id=2,customer_id=2,customerorder_id=2,menuitem_id=10,menuitem_price=25)
session.add(customerOrderedItem5)
session.commit()

customerOrderedItem6 = CustomerOrderedItem(restaurant_id=2,customer_id=2,customerorder_id=2,menuitem_id=11,menuitem_price=15)
session.add(customerOrderedItem6)
session.commit()

customerOrderedItem7 = CustomerOrderedItem(restaurant_id=3,customer_id=3,customerorder_id=3,menuitem_id=15,menuitem_price=8.99)
session.add(customerOrderedItem7)
session.commit()

customerOrderedItem8 = CustomerOrderedItem(restaurant_id=3,customer_id=3,customerorder_id=3,menuitem_id=16,menuitem_price=9.95)
session.add(customerOrderedItem8)
session.commit()

customerOrderedItem9 = CustomerOrderedItem(restaurant_id=3,customer_id=3,customerorder_id=3,menuitem_id=17,menuitem_price=6.99)
session.add(customerOrderedItem9)
session.commit()

print "added customerordereditems!"