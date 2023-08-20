#!/usr/bin/env python

from app import app, db, Item  # Import your app and Item model
import random

with app.app_context():
    # List of sample items
    items = [
    {"name": "Ridgid K60 #1 Drain Machine", "item_type": "Tool"},
    {"name": "Ridgid K60 Drain Machine", "item_type": "Tool"},
    {"name": "M12 Propex Expander Kit", "item_type": "Tool"},
    {"name": "M18 Propex Expader 1-1/4\"-1-1/2\"", "item_type": "Tool"},
    {"name": "Mega Press 1/2\"- 2\" Jaws", "item_type": "Tool"},
    {"name": "Flex Shaft #1", "item_type": "Tool"},
    {"name": "Flexshaft #2", "item_type": "Tool"},
    {"name": "Ridgid Electric Flusher w/ H10 Cart", "item_type": "Tool"},
    {"name": "Ridgid KJ-3100 Gas Hydro Flusher", "item_type": "Tool"},
    {"name": "Ridgid K-400 Drum Machine 3/8\" cable", "item_type": "Tool"},
    {"name": "Ridgid K-40AF Sink Drain Machine 5/16\"", "item_type": "Tool"},
    {"name": "Ridgid Superfreeze Machine", "item_type": "Tool"},
    {"name": "General Wire Mini Rooter XP 3/8\" & 1/2\"", "item_type": "Tool"},
    {"name": "General Wire JM-1450 Electric Jetter", "item_type": "Tool"},
    {"name": "Ridgid Inspection Camera", "item_type": "Tool"},
    {"name": "Reed Ratcheting Snap Cutter 6 ft chain", "item_type": "Tool"},
    {"name": "Porter Cable 6 gal Portable Air Compressor", "item_type": "Tool"},
    {"name": "36\" Aluminum Pipe Wrench", "item_type": "Tool"},
    {"name": "M18 Deep Cut Band Saw Kit", "item_type": "Tool"},
    {"name": "Combustible Gas Leak Detector", "item_type": "Tool"},
    {"name": "M18 1” SDS Plus Rotary Hammer W/ DE Kit", "item_type": "Tool"},
    {"name": "Simoniz 2200psi gas pressure washer", "item_type": "Tool"},
    {"name": "Wirsbo Hand Expander Kit 1/2\"-1\"", "item_type": "Tool"},
    {"name": "Ridgid XL-C Kit Propress 2-1/2\"-4\"", "item_type": "Tool"},
    {"name": "Viega Pressgun 6", "item_type": "Tool"},
    {"name": "M18™ FORCE LOGIC™ Press Tool 1/2\"-2\"", "item_type": "Tool"},
    {"name": "Featherlite 16ft extension ladder grade II", "item_type": "Tool"},
    {"name": "Ridgid Viega 1/2\"-2\" Press Heads", "item_type": "Tool"},
    {"name": "Ridgid KJ-1750 Electric Flusher", "item_type": "Tool"},
    {"name": "Ridgid K45 Sink Machine", "item_type": "Tool"},
    {"name": "M12 Propex Expander Kit #2", "item_type": "Tool"},
    {"name": "Dewalt 4-1/2\" Angle Grinder", "item_type": "Tool"},
    {"name": "Sawzall® Recip Saw Kit", "item_type": "Tool"},
    {"name": "1/2\" Super Hawg™", "item_type": "Tool"},
    {"name": "Makita 14\" Cut off saw", "item_type": "Tool"},
    {"name": "14” Abrasive Cut-Off Machine", "item_type": "Tool"},
    ################################################################ TOOLS END HERE ############################################
    {"name": "STATION PLACE", "item_type": "Keys"},
    {"name": "8th AVE GARDENS", "item_type": "Keys"},
    {"name": "BROADWAY CROSSING", "item_type": "Keys"},
    {"name": "2484 RENFREW STREET", "item_type": "Keys"},
    {"name": "SOLEIL TERRACE", "item_type": "Keys"},
    {"name": "ELLINGTON", "item_type": "Keys"},
    {"name": "BLENHEIM TERRACE", "item_type": "Keys"},
    {"name": "VENTURA PLACE", "item_type": "Keys"},
    {"name": "BLUETREE", "item_type": "Keys"},
    {"name": "QUEENS PARK", "item_type": "Keys"},
    {"name": "FOLIO", "item_type": "Keys"},
    {"name": "CONCORDIA ONE", "item_type": "Keys"},
    {"name": "ADDITION", "item_type": "Keys"},
    {"name": "CENTREPOINTE", "item_type": "Keys"},
    {"name": "CRANE", "item_type": "Keys"},
    {"name": "CITY CREST", "item_type": "Keys"},
    {"name": "GEMINI ONE", "item_type": "Keys"},
    {"name": "GEMINI TWO", "item_type": "Keys"},
    {"name": "ETON HEIGHTS", "item_type": "Keys"},
    {"name": "CANADIAN", "item_type": "Keys"},
    {"name": "METROPOLITIAN", "item_type": "Keys"},
    {"name": "THE CROFTON", "item_type": "Keys"},
    {"name": "PARKVIEW PLACE", "item_type": "Keys"},
    {"name": "COURTYARDS", "item_type": "Keys"},
    {"name": "BRISTOL", "item_type": "Keys"},
    {"name": "FLATIRON", "item_type": "Keys"},
    {"name": "L'ATELIER", "item_type": "Keys"},
    {"name": "OMA A&B", "item_type": "Keys"},
    {"name": "SILHOUETTE", "item_type": "Keys"},
    {"name": "VINE", "item_type": "Keys"},
    {"name": "ARGYLE", "item_type": "Keys"},
    {"name": "RUSSELL PROFESIONAL", "item_type": "Keys"},
    {"name": "MONDELLA", "item_type": "Keys"},
    {"name": "WATERSIDE", "item_type": "Keys"},
    {"name": "NOVO 1", "item_type": "Keys"},
    {"name": "MAGNOLIA GATE", "item_type": "Keys"},
    {"name": "WALL CENTRE", "item_type": "Keys"},
    {"name": "VERSATILE", "item_type": "Keys"}
]

    
    for item in items:
        # Create new Item object
        new_item = Item(
            name=item["name"],
            item_type=item["item_type"],
            group_id=1  # Randomly assign a group_id between 1 and 5
        )

        # Add the new item to the session
        db.session.add(new_item)

    # Commit the session to save the new items
    db.session.commit()


    #Create this to generate to spreadsheet table generators


