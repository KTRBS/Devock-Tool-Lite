import os
import json

BASE_OFFER = {
    "text": "lite",
    "amount": "1",
    "price": "0",
    "item": "14",
    "time": "950400",
    "theme": "offer_bgr_generic"
}

def get_shop_json_path():
    while True:
        folder_path = input("Enter the folder path /storage/emulated/0/: ")
        full_path = os.path.join("/storage/emulated/0/", folder_path, "shop.json")
        folder_dir = os.path.dirname(full_path)

        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

        if not os.path.exists(full_path):
            with open(full_path, "w") as file:
                json.dump({}, file, indent=4)

        return full_path

def load_shop_data(file_path):
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Invalid JSON")
            return {}

def save_shop_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("v47 lite")
    shop_file_path = get_shop_json_path()
    shop_data = load_shop_data(shop_file_path)

    while True:
        item = input("Enter item ID: ").strip()
        if not item.isdigit():
            print("Invalid ID")
            continue

        title = input("Enter title: ").strip()
        if not title:
            print("Try again")
            continue

        new_offer_id = str(max([int(offer_id) for offer_id in shop_data.keys()] or [0]) + 1)

        offer_data = BASE_OFFER.copy()
        offer_data["text"] = title
        offer_data["item"] = item

        shop_data[new_offer_id] = offer_data

        save_shop_data(shop_file_path, shop_data)
        print("Done.\n")

if __name__ == "__main__":
    main()