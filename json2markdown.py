import json
import os
import glob
import warnings
from markdownify import markdownify as md

warnings.filterwarnings("ignore", category=UserWarning, module='markdownify')


def json_to_markdown(json_file, output_dir):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Process the JSON data and convert it to Markdown.
    # This step depends on the structure of your JSON files.
    markdown_output = ""
    for item in data:
        if isinstance(item, dict):
            for key, value in item.items():
                markdown_output += f"## {key}\n\n{md(value)}\n\n"
        else:
            markdown_output += f"{md(item)}\n\n"

    # Write the output to a Markdown file.
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(json_file))[0] + '.md')
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_output)

# Set the folder paths and the input directory.
folder_paths = ['Codegen', 'Instruct', 'Roleplay', 'Toolformer']
input_dir = '.'
output_dir = 'output'

# Process all JSON files in the specified folder paths.
for folder in folder_paths:
    input_files = glob.glob(os.path.join(input_dir, folder, '*.json'))

    for input_file in input_files:
        # Create a mirrored output path by replacing the input directory with the output directory.
        mirrored_output_dir = input_file.replace(input_dir, output_dir)
        mirrored_output_dir = os.path.dirname(mirrored_output_dir)

        json_to_markdown(input_file, mirrored_output_dir)
