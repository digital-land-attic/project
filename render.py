#!/usr/bin/env python3

import os
import markdown

from frontmatter import Frontmatter
from bin.govukify import govukify_markdown_output
from bin.jinja_setup import env, render
from bin.helpers import read_in_json
from digital_land_frontend.filters import make_link

from markdown.extensions.toc import TocExtension

# register jinja filters
env.filters["make_link"] = make_link

# set variables to make available to all templates
env.globals["staticPath"] = "https://digital-land.github.io"

# init markdown
md = markdown.Markdown(extensions=[TocExtension(toc_depth="2-3")])


def compile_markdown(md, s):
    html = md.convert(s)
    return govukify_markdown_output(html)


# making markdown compiler available to jinja templates
def markdown_filter(s):
    return compile_markdown(md, s)


env.filters["markdown"] = markdown_filter


def get_project_content(filename):
    file_content = Frontmatter.read_file(filename)
    return {
        "name": file_content["attributes"].get("name"),
        "status": file_content["attributes"].get("status"),
        "frontmatter": file_content["attributes"],
        "body": file_content["body"],
    }


def markdown_files_only(files, file_ext=".md"):
    return [f for f in files if f.endswith(file_ext)]


# get templates
index_template = env.get_template("index.html")
project_template = env.get_template("project.html")
content_template = env.get_template("content.html")
design_history_template = env.get_template("design-history.html")

# get empty project buckets
summary = read_in_json("config/project_buckets.json")


def add_to_bucket(project_path, project):
    summary.setdefault(project.get("status").lower(), {"projects": []})
    # make the summary obj
    project_summary = {
        "path": project_path,
        "name": project.get("name"),
        "description": project.get("one-liner"),
    }
    # append to correct bucket
    summary[project.get("status").lower()]["projects"].append(project_summary)


project_dir = "projects/"
projects = os.listdir(project_dir)


def render_project_content_pages(project):
    content_dir = f"{project_dir}{project}/content"
    md_files = markdown_files_only(os.listdir(content_dir))
    for f in md_files:
        file_content = Frontmatter.read_file(f"{content_dir}/{f}")
        html = compile_markdown(md, file_content["body"])
        render(
            f"{project}/{f.replace('.md', '')}/index.html",
            content_template,
            content=html,
            toc=md.toc_tokens,
            fm=file_content["attributes"],
            project=project,
        )


# loop each project
# loop over additional content files
# extract frontmatter
# compile markdown
# render

# get index md
# extract frontmatter
# process frontmatter
# compile markdown
# loop over updates
# extract frontmatter
# compile markdown
# render project page


for project in projects:

    # render any additional content pages
    if os.path.isdir(f"{project_dir}{project}/content"):
        render_project_content_pages(project)

    project_content = get_project_content(f"{project_dir}{project}/index.md")

    # add to buckets for index
    add_to_bucket(project, project_content)

    # collect any additional updates
    updates = []

    render(
        f"{project}/index.html",
        project_template,
        project=project_content,
        artefacts=project_content["frontmatter"].get("artefacts"),
        updates=updates,
    )


for k in summary.keys():
    summary[k]["projects"].sort(key=lambda x: x["name"])
# generate index page
render(f"index.html", index_template, projects=summary)