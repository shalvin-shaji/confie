import json
import glob
from jinja2 import Template
import argparse
import pathlib

def init(args):
    if not pathlib.Path(args.output).exists():
        pathlib.Path(args.output).mkdir()
    files = glob.glob(pathname="*", root_dir=args.output)
    for file in files:
        pathlib.Path(file).unlink()


def parse_args():
    parser = argparse.ArgumentParser(prog="Configie",
                                     description="Generate environment specific config from base configuration file")
    parser.add_argument("-e", "--env", default='uat', help="Environment for which configs need to be generated")
    parser.add_argument('-b', "--base", default='.', help="Base/Config directory location")
    parser.add_argument('-o', "--output", default='output' , help="Output directory name to save configs")
    args = parser.parse_args()
    return args

def get_base_files(base):
    files = glob.glob("base/**/*.json", root_dir=base)
    print(files)
    return files

def get_config_file(base, basefile):
    config_file =f"{base}/configs/" + basefile.split("/", 1)[1]
    print(config_file)
    config_file = json.load(open(config_file))
    return config_file

def create_config(profile, configs, base_file, output):
    base = json.load(open(base_file))['data']
    template = Template(base)
    render = template.render(configs[profile])
    print(render)


def main(args):
    base_files = get_base_files(args.base)
    for base_file in base_files:
        config = get_config_file(args.base, base_file)
        create_config(args.env, config, base_file, args.output)

if __name__ == "__main__":
    args = parse_args()
    init(args)
    main(args)