import json
import csv
import xml.etree.ElementTree as ET
import yaml

class JSONHandler:
    def load(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def save(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)

class CSVHandler:
    def load(self, filename):
        data = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def save(self, filename, data):
        with open(filename, 'w', newline='') as file:
            fieldnames = data[0].keys() if data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

class XMLHandler:
    def load(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        data = []
        for item_element in root.findall('item'):
            item_data = {}
            for element in item_element:
                item_data[element.tag] = element.text
            data.append(item_data)
        return data

    def save(self, filename, data):
        root = ET.Element('data')
        for item in data:
            item_element = ET.SubElement(root, 'item')
            for key, value in item.items():
                element = ET.SubElement(item_element, key)
                element.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(filename)

class YAMLHandler:
    def load(self, filename):
        with open(filename, 'r') as file:
            return yaml.safe_load(file)

    def save(self, filename, data):
        with open(filename, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)

# Facade
class FileFacade:
    def __init__(self):
        self.json_handler = JSONHandler()
        self.csv_handler = CSVHandler()
        self.xml_handler = XMLHandler()
        self.yaml_handler = YAMLHandler()

    def load(self, filename, format):
        if format == 'json':
            return self.json_handler.load(filename)
        elif format == 'csv':
            return self.csv_handler.load(filename)
        elif format == 'xml':
            return self.xml_handler.load(filename)
        elif format == 'yaml':
            return self.yaml_handler.load(filename)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def save(self, filename, data, format):
        if format == 'json':
            self.json_handler.save(filename, data)
        elif format == 'csv':
            self.csv_handler.save(filename, data)
        elif format == 'xml':
            self.xml_handler.save(filename, data)
        elif format == 'yaml':
            self.yaml_handler.save(filename, data)
        else:
            raise ValueError(f"Unsupported format: {format}")

# Client code
if __name__ == "__main__":
    converter = FileFacade()

    # Load data from a JSON file
    data = converter.load('data.json', 'json')
    print("Loaded data from JSON file:")
    print(data)

    # Save data to a CSV file
    converter.save('data.csv', data, 'csv')
    print("Saved data to CSV file (data.csv)")

    # Load data from a CSV file
    loaded_data = converter.load('data.csv', 'csv')
    print("Loaded data from CSV file:")
    print(loaded_data)

    # Save data to an XML file
    converter.save('data.xml', loaded_data, 'xml')
    print("Saved data to XML file (data.xml)")

    # Load data from an XML file
    loaded_data_xml = converter.load('data.xml', 'xml')
    print("Loaded data from XML file:")
    print(loaded_data_xml)

    # Save data to a YAML file
    converter.save('data.yaml', loaded_data_xml, 'yaml')
    print("Saved data to YAML file (data.yaml)")

    # Load data from a YAML file
    loaded_data_yaml = converter.load('data.yaml', 'yaml')
    print("Loaded data from YAML file:")
    print(loaded_data_yaml)

