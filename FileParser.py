import csv
import json
import argparse


def parse_text_file(file_path):
    print("Parsing text file...")

    products = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):

        if lines[i].strip() == '':
            i += 1
            continue

        # Extracting product info from consecutive non-empty lines
        product_info = {}
        while i < len(lines) and lines[i].strip() != '':
            key, value = lines[i].strip().split(': ', 1)
            product_info[key] = value
            i += 1

        products.append(product_info)

    print("Finished parsing text file.")
    return products


def parse_csv_file(csv_file):
    print("Parsing CSV file...")
    products = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    print("Finished parsing CSV file...")
    return products


def main(text_file, csv_file, output_json):
    text_products = parse_text_file(text_file)
    csv_products = parse_csv_file(csv_file)
    all_products = text_products + csv_products

    print("Final Structured Data:")
    for product in all_products:
        print(product)

    with open(output_json, 'w') as json_file:
        json.dump(all_products, json_file, indent=4)

    print(f"Structured data has been saved to {output_json}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse product data from text and CSV files.")
    parser.add_argument("text_file", help="Path to the text file containing product information.")
    parser.add_argument("csv_file", help="Path to the CSV file containing product information.")
    parser.add_argument("output_json", help="Path to the JSON file to output the structured data.")
    args = parser.parse_args()

    main(args.text_file, args.csv_file, args.output_json)
