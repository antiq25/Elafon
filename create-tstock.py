from app import app, db, Inventory, Group # THIS SCRIPT IS TO GENERATE TECH TRUCK STOCK INVENTORY #
# Create a list of items
items = [
  {"name": "Copper pipes", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "Copper fittings", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "PVC pipes", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "PVC fittings", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "PEX pipes", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "PEX fittings", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "Galvanized pipes", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "Galvanized fittings", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "Brass fittings and adapters", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "Flexible supply lines", "item_type": "Pipe and Fittings", "quantity": 10},
  {"name": "Pipe joint compound", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Pipe thread tape (Teflon tape)", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Pipe putty", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Pipe repair clamps", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Epoxy putty", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Leak repair tape", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Rubber gaskets", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "O-rings", "item_type": "Sealing and Repair Materials", "quantity": 10},
  {"name": "Faucet cartridges", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Faucet repair kits", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Toilet flappers", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Flush valves", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Sink stoppers", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Basin stoppers", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Showerhead replacement parts", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Tub spout replacement parts", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Garbage disposal parts", "item_type": "Fixtures and Parts", "quantity": 10},
  {"name": "Drain augers (snake)", "item_type": "Drain and Sewer Cleaning", "quantity": 10},
  {"name": "Plunger", "item_type": "Drain and Sewer Cleaning", "quantity": 10},
  {"name": "Drain cleaning cables", "item_type": "Drain and Sewer Cleaning", "quantity": 10},
  {"name": "Drain cleaning blades", "item_type": "Drain and Sewer Cleaning", "quantity": 10},
  {"name": "Drain cleaning chemicals", "item_type": "Drain and Sewer Cleaning", "quantity": 10},
  {"name": "Pipe insulation", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Pipe hangers", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Pipe supports", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Expansion tanks", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Pressure relief valves", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Pipe connectors", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Pipe couplings", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Plumbing-grade silicone sealant", "item_type": "Miscellaneous Supplies", "quantity": 10},
  {"name": "Work gloves", "item_type": "Safety and Cleanup", "quantity": 10},
  {"name": "Disposable gloves", "item_type": "Safety and Cleanup", "quantity": 10},
  {"name": "Shop towels", "item_type": "Safety and Cleanup", "quantity": 10},
  {"name": "Rags", "item_type": "Safety and Cleanup", "quantity": 10},
  {"name": "Absorbent materials for water cleanup", "item_type": "Safety and Cleanup", "quantity": 10},
  {"name": "Invoice forms", "item_type": "Documentation and Communication", "quantity": 10},
  {"name": "Receipts", "item_type": "Documentation and Communication", "quantity": 10},
  {"name": "Work orders", "item_type": "Documentation and Communication", "quantity": 10},
  {"name": "Plumbing system diagrams", "item_type": "Documentation and Communication", "quantity": 10},
  {"name": "Contact information for suppliers", "item_type": "Documentation and Communication", "quantity": 10},
  {"name": "Contact information for clients", "item_type": "Documentation and Communication", "quantity": 10},
  {"name": "Adjustable wrenches", "item_type": "Tools (Minimal)", "quantity": 10},
  {"name": "Pliers", "item_type": "Tools (Minimal)", "quantity": 10},
  {"name": "Multi-bit screwdriver", "item_type": "Tools (Minimal)", "quantity": 10},
  {"name": "Utility knife", "item_type": "Tools (Minimal)", "quantity": 10}
]

# Prompt for the truck name
truck_name = input("Enter the truck name (e.g., Truck FJ3922): ")

# Create a context for the app
with app.app_context():
    # Get the group_id for the specified truck name
    group = Group.query.filter_by(name=truck_name).first()
    
    # If the group (truck) doesn't exist, create it
    if group is None:
        group = Group(name=truck_name)
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
