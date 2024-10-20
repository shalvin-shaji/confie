import json
import glob
from jinja2 import Template

def get_base_files():
    files = glob.glob("base/**/*.json")
    print(files)
    return files

def get_config_file(basefile):
    config_file ="configs/" + basefile.split("/", 1)[1]
    print(config_file)
    config_file = json.load(open(config_file))
    return config_file

def create_config(profile, configs, base_file):
    base = json.load(open(base_file))['data']
    template = Template(base)
    render = template.render(configs[profile])
    print(render)



def main():
    base_files = get_base_files()
    configs = get_config_file(base_files[0])
    create_config('dev', configs, base_files[0])


if __name__ == "__main__":
    main()