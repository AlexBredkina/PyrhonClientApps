import yaml


data_to_yaml = {'action':action_list, 'to':to_list}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode = True)

with open('data_write.yaml') as f_n:
    print(f_n.read())