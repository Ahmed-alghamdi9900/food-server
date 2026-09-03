from food import app, db
from models import Shops, MenuList, ItemList, CategoryTypes


with app.app_context():
    shop = db.session.get(Shops, 1001)

    if shop is None:
        shop = Shops(
            name="Domino's Saudi Arabia",
            category_code=CategoryTypes.Pizza,
            description="Domino's Saudi Arabia test restaurant",
            shop_code=1001,
            wait_time=30,
            address="Saudi Arabia",
            amenity="Delivery",
            phone="0000000000",
            message="Test restaurant",
        )
        db.session.add(shop)

    menu = db.session.get(MenuList, 2001)

    if menu is None:
        menu = MenuList(
            menu_code=2001,
            title="Test Menu",
            info="Saudi Arabia test menu",
            shop_code=1001,
        )
        db.session.add(menu)

    item = db.session.get(ItemList, 3001)

    if item is None:
        item = ItemList(
            item_code=3001,
            menu_code=2001,
            name="Test Pizza",
            description="Test pizza for Saudi Arabia integration",
            price="29.00",
        )
        db.session.add(item)

    db.session.commit()

    print("Saudi test data is ready.")
    print("Restaurant: Domino's Saudi Arabia")
    print("Menu: Test Menu")
    print("Item: Test Pizza")