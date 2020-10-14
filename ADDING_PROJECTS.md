# Add a project

Follow these steps to create a project page. There is sample page content in the `/projects` folder.

### Create project

Create a folder with the project name in the `/projects` folder. The folder name such be kebab case, such as, `project-name`.

Create an `index.md` file in this project folder. In this file you should include frontmatter that sets `name`, `status` and if applicable, the set of `characteristics`.

It should look similar to this example

```
---
name: "Heritage assets"
status: "To explore"
---
```

If including characteristics, like this

```
---
name: Conservation Areas
status: In progress
characteristics:
    identifier: conservation-area
    typology: geography
    data provider and maintainer: Local Planning Authority
    legislation: https://www.legislation.gov.uk/ukpga/1990/9/section/69
    guidance: https://www.gov.uk/guidance/conserving-and-enhancing-the-historic-environment
---
```

The allowable `status` values are: **to explore**, **in progress** and **published**.

You can also add any markdown content after this frontmatter. It will be used as the content in description section of the page.

### Add datasets to project

If there are mulitple datasets for a project you should create a `datasets` folder in the project folder. For example the path to the dataset folder will be `/projects/name-of-project/datasets`.

Then create a `.md` file for each datasets that belongs to the project.

In this file add frontmatter to define the `name` and `characteristics`. E.g.

```
---
name: "Locally listed buildings"
characteristics:
    identifier: locally-listed-building
    typology: geography
    data provider and maintainer: local planning authorities
---
```

After the frontmatter add the content that describes the dataset. This will be used to describe the dataset on the project page.
