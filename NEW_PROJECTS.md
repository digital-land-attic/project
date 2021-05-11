# Creating new projects

For a new project, create a new folder in `/projects`. Call it the name of the project, e.g. `conservation-areas`.

In this folder create a markdown file, call it `index.md`.

This file should contain

```
---
name:
status:
one-liner:
latest_updated: # use the YYYY-MM-DD format
artefacts:
    - text:
      href:
    - text:
      href:
---

<!-- description/overview goes here -->

## Why we are looking at <project name>

## What are we focused on

```

This will create the main page for the project.

For the `status` use one of the following values: 

## Updates

To add updates, firstly, create a folder called `updates` in the project folder. For example, you will have a folder at `/projects/conservation-areas/updates`.

Then for each update create a `.md` file. For example, `changes-to-document-schema.md`. Each update should be structured like:

```
---
name:
date:
type:
---

<!-- update content -->

```
For `type` use one of; `update`, `decision`, `event`, `learning`.

Aim for a brief sentence or 2 to describe the update. Ideally add links to further information, an artefact or associated thing.

## Additional content

For any additional content pages, create a folder in the project folder called  `content`. Then for each page create a `.md` file. For example, `projects/locals-plans/alpha.md`.

```
---
name:
date:
---

<!-- content -->

```

There are a number of optional parameters to use with additional content pages. To use them add to the frontmatter of the markdown file. These options are:

* `displayContents` - if set to `True` it will change the layout of the page to include a contents section to the left of the main body of content.
