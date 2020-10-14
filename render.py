#!/usr/bin/env python3

import os
import codecs
import jinja2
import markdown

from frontmatter import Frontmatter
from bin.govukify import govukify_markdown_output

docs = "docs/"


def render(path, template, **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(**kwargs))


# register templates
multi_loader = jinja2.ChoiceLoader(
    [
        jinja2.FileSystemLoader(searchpath="./templates"),
        jinja2.PrefixLoader(
            {
                "digital-land-frontend": jinja2.PackageLoader("digital_land_frontend"),
                "govuk-jinja-components": jinja2.PackageLoader(
                    "govuk_jinja_components"
                ),
            }
        ),
    ]
)
env = jinja2.Environment(loader=multi_loader)

# get templates
project_template = env.get_template("project.html")

project_dir = "projects/"

# init markdown
md = markdown.Markdown()


def compile_markdown(md, s):
    html = md.convert(s)
    return govukify_markdown_output(html)


projects = os.listdir(project_dir)


def get_project_content(filename):
    file_content = Frontmatter.read_file(filename)
    return {
        "name": file_content["attributes"].get("name"),
        "status": file_content["attributes"].get("status"),
        "characteristics": file_content["attributes"].get("characteristics"),
        "description": compile_markdown(md, file_content["body"]),
    }


for project in projects:
    hasMultipleDatasets = False
    project_content = get_project_content(f"{project_dir}{project}/index.md")
    if os.path.isdir(f"{project_dir}{project}/datasets"):
        datasets = []
        md_files = [
            f
            for f in os.listdir(f"{project_dir}{project}/datasets")
            if f.endswith(".md")
        ]
        for f in md_files:
            datasets.append(get_project_content(f"{project_dir}{project}/datasets/{f}"))
        project_content["datasets"] = datasets
    render(f"project/{project}/index.html", project_template, project=project_content)
