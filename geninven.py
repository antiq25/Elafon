from app import app, db, Inventory, Group

# Create a list of items
items = [
    {"name": "Item1", "item_type": "Type1", "quantity": 10},
    {"name": "Item2", "item_type": "Type2", "quantity": 5},
    {"name": "Item3", "item_type": "Type3", "quantity": 7},
    # Add more items as needed
]

# Create a context for the app
with app.app_context():
    # Get the group_id for the "Material" group
    group = Group.query.filter_by(name="Material").first()
    if group is None:
        print("Group 'Material' not found.")
        exit()

    group_id = group.id

    # Add each item to the database
    for item in items:
        inventory_item = Inventory(name=item["name"], item_type=item["item_type"],
                                  group_id=group_id, quantity=item["quantity"])
        db.session.add(inventory_item)

    # Commit the changes to the database
    db.session.commit()

