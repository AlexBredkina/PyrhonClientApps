import yaml

data_to_yaml = {'first': ["python", 3, "course"], 'second': 2,
                "third": {"third1": "120€", "third2": "125€", "third3": "128€"}}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('data_write.yaml') as f_n:
    print(f_n.read())
