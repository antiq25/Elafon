from app import app, db, Inventory, Group

# Create a list of items
items = [
    {"name": "Item1", "item_type": "Type1", "quantity": 10},
    {"name": "Item2", "item_type": "Type2", "quantity": 5},
    {"name": "Item3", "item_type": "Type3", "quantity": 7},
    # Add more items as needed
]

shop = input("Enter the name of the shop ")

# Create a context for the app
with app.app_context():
    # Get the group_id for the specified truck name
    group = Group.query.filter_by(name=shop).first()

    # If the group (truck) doesn't exist, create it
    if group is None:
        group = Group(name=shop)
        db.session.add(group)
        db.session.commit()

    group_id = group.id

    # Add each item to the database under the specified group (truck)
    for item in items:
        existing_item = Inventory.query.filter_by(name=item["name"], group_id=group_id).first()

        if existing_item:
            # Update attributes of existing item if needed, e.g., increase quantity
            existing_item.quantity += item["quantity"]
        else:
            # If item doesn't exist for the truck, add a new one
            inventory_item = Inventory(name=item["name"], item_type=item["item_type"],
                                      group_id=group_id, quantity=item["quantity"])
            db.session.add(inventory_item)

    # Commit the changes to the database
    db.session.commit()
