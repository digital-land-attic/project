#!/usr/bin/env python3

import os
import codecs
import jinja2
import markdown

from frontmatter import Frontmatter
from bin.govukify import govukify_markdown_output
from digital_land_frontend.filters import make_link

from markdown.extensions.toc import TocExtension

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
env = jinja2.Environment(loader=multi_loader, autoescape=True)

# register jinja filters
env.filters["make_link"] = make_link

# get templates
index_template = env.get_template("index.html")
project_template = env.get_template("project.html")
content_template = env.get_template("content.html")

project_dir = "projects/"

# init markdown
md = markdown.Markdown(extensions=[TocExtension(toc_depth="2-3")])


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


def markdown_files_only(files, file_ext=".md"):
    return [f for f in files if f.endswith(file_ext)]


for project in projects:
    hasMultipleDatasets = False
    project_content = get_project_content(f"{project_dir}{project}/index.md")
    # get dataset content to display on project page
    if os.path.isdir(f"{project_dir}{project}/datasets"):
        datasets = []
        md_files = markdown_files_only(os.listdir(f"{project_dir}{project}/datasets"))

        for f in md_files:
            datasets.append(get_project_content(f"{project_dir}{project}/datasets/{f}"))
        project_content["datasets"] = datasets

    # render any additional content pages
    if os.path.isdir(f"{project_dir}{project}/content"):
        md_files = markdown_files_only(os.listdir(f"{project_dir}{project}/content"))

        for f in md_files:
            file_content = Frontmatter.read_file(f"{project_dir}{project}/content/{f}")
            html = compile_markdown(md, file_content["body"])
            render(
                f"{project}/{f.replace('.md', '')}/index.html",
                content_template,
                content=html,
                toc=md.toc_tokens,
                fm=file_content["attributes"],
                project=project,
            )

    render(f"{project}/index.html", project_template, project=project_content)


# generate summary for index page
summary = {}
for project in projects:
    filename = f"{project_dir}{project}/index.md"
    if os.path.exists(filename):
        file_content = Frontmatter.read_file(filename)
        summary.setdefault(file_content["attributes"].get("status").lower(), [])
        project_summary = {
            "name": file_content["attributes"].get("name"),
            "description": file_content["attributes"].get("one-liner"),
        }
        summary[file_content["attributes"].get("status").lower()].append(
            project_summary
        )
for k in summary.keys():
    summary[k].sort(key=lambda x: x["name"])
# generate index page
render(f"index.html", index_template, projects=summary)