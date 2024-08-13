import json
import requests
from pathlib import Path
from typing import List

class ExampleClass:
    def __init__(self, name: str, population: int, list_of_states: List[str]):
        self.name = name
        self.population = population
        self.list_of_states = list_of_states

    @staticmethod
    def create_instance():
        return ExampleClass(
            name="output name",
            population=12321,
            list_of_states=["state1", "state2", "state3"]
        )

class BikeMap:
    def __init__(self):
        self.target_path = Path(__file__).parent

    def read_file(self, file_path: str):
        file = self.target_path / file_path
        try:
            with open(file, 'r') as reader:
                for line in reader:
                    print(line.strip())
        except FileNotFoundError:
            print("FileNotFoundException")
        except IOError:
            print("IOException")

    def read_object_from_json_string(self, json_string: str):
        example = json.loads(json_string, object_hook= lambda d: ExampleClass(**d))
        print(example.name)
        print(example.population)
        print(example.list_of_states)

    def read_object_from_json(self, file_path: str):
        file = self.target_path / file_path
        try:
            with open(file, 'r') as reader:
                example = json.load(reader, object_hook=lambda d: ExampleClass(**d))
                print(example.name)
                print(example.population)
                print(example.list_of_states)
        except FileNotFoundError:
            print("FileNotFoundException")
        except IOError:
            print("IOException")

    def read_array_from_json(self, file_path: str):
        file = self.target_path / file_path
        try:
            with open(file, 'r') as reader:
                examples = json.load(reader)
                for example_dict in examples:
                    example = ExampleClass(**example_dict)
                    print(example.name)
                    print(example.population)
                    print(example.list_of_states)
        except FileNotFoundError:
            print("FileNotFoundException")
        except IOError:
            print("IOException")

    def read_list_from_json(self, file_path: str):
        file = self.target_path / file_path
        try:
            with open(file, 'r') as reader:
                examples = json.load(reader)
                for example_dict in examples:
                    example = ExampleClass(**example_dict)
                    print(example.name)
                    print(example.population)
                    print(example.list_of_states)
        except FileNotFoundError:
            print("FileNotFoundException")
        except IOError:
            print("IOException")

    def write_json(self):
        file_path = self.target_path / "out.json"
        example = ExampleClass.create_instance()
        with open(file_path, 'w') as writer:
            json.dump(example.__dict__, writer, indent=4)

    def download(self, url, filename):
        file_path = self.target_path / filename
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as output:
                output.write(response.content)

    
if __name__ == "__main__":
    sol = BikeMap()
    sol.read_file("text.txt")
    sol.read_object_from_json_string('{"name": "country name", "population": 123, "list_of_states": ["country1", "country2", "country3"]}')
    # sol.read_object_from_json("object.json")
    # sol.read_array_from_json("array.json")
    # sol.read_list_from_json("array.json")
    sol.write_json()
    sol.download("https://raw.github.com/square/okhttp/master/README.md", "README.md")
    sol.download("https://raw.githubusercontent.com/Luzifer/staticmap/master/example/postmap.png", "postmap.png")

