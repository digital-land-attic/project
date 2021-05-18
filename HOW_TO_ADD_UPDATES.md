# How to add updates to project pages

Add updates to a project to record any progress made.

Updates should be short pieces of content. Try to stick to 1 or 2 sentences.

Whenever possible, include links to relevant material. For example, you could link to a page with more information or an artefact such as a policy paper or a diagram.

All updates need to contain the following information:

* what project it belongs to
* who wrote it - this helps us if there is an issue rendering the update
* the date it was written
* the type of update (see list below)
* the update

![Example of a update on a project page](https://raw.githubusercontent.com/digital-land/project/main/src/images/readmes/project-page-update-example.png)

There are 2 ways to add updates.

### 1. Add an update to the 'Project updates' spreadsheet

You can add an update to the [`Project updates`](https://docs.google.com/spreadsheets/d/1hOnXFXQFOt_pYIs6haCzym1eLPzBupvTQP0DWZh37ww/edit) spreadsheet.

![Screenshot of Project updates spreadsheet with 2 rows](https://raw.githubusercontent.com/digital-land/project/main/src/images/readmes/updates-spreadsheets-screenshot.png)

Each row of this spreadsheet will be turned into an update that appears on the project pages.

Use the the dropdowns to select the `Project` it relates to and the `Type` of update it is.

Give the update a short name in the `Name` column.

Add a date to `Date`. You should use the YYYY-MM-DD date format.

Add your name to `Author`. This makes it easier for us to fix any issues.

Write the update content in the `Update` column. This can be plain text or markdown (if you wish to add links).

The updates will be added to the project pages overnight. **If you need it updating sooner then we can run the script manually**.

We will periodically delete the updates in the spreadsheet so that it does not become overwhelming. It is a staging ground for the updates. The complete record of updates will be stored in github along with the other content for the project.

If you need to update an existing update it is best to do that manually.

### 2. Write update in markdown

If you are familiar with [markdown you can create an update file and write markdown directly in [this repo](https://github.com/digital-land/project).

Firstly, find the update folder for the project you are adding an update. For example, `projects/conservation-areas/updates/`.

In this folder create a markdown file for the update. For example `finding-conservation-area-data.md`.

The contents of this file should look similar to this

```
---
author: Colm Britton
date: '2020-11-27'
name: Finding conservation area data
type: update
---

We were able to find and collect [conservation area data from 70+ local authorities](https://digital-land.github.io/conservation-area/). The data is a bit sparse with a lot of names and references missing. However we do have geometries for ~5000 conservation areas.
```


### Update types

It is helpful to categorise your updates. Broadly, we think they can be categorised in these groups:

* **decision** - a decision we have made that needs to be recorded
* **event** - a event worth recording, e.g. a kick off workshop or procurement of a 3rd party
* **learning** - something we have learnt along the way that we think is worth calling out
* **milestone** - projects pass common milestones, we should record when that happens
* **update** - a broad category for when the update doesn't fit into any of the above