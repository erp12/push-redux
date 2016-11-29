Title: How to Contribute to the Push Redux

The Push Redux is an implementation agnostic place to document things about Push and PushGP. It is hosted on [Github Pages](https://pages.github.com/) and is built using [Pelican](http://blog.getpelican.com/). The content is written in [Markdown](https://en.wikipedia.org/wiki/Markdown) and then built into static HTML pages. All contributions are handled through [GitHub Pull Requests](https://help.github.com/articles/about-pull-requests/).

This document aims to explain how to contribute to the Push Redux. 

#### Table of Contents

1. [Required Background Knowledge](#background)
2. [Basics of Pelican and Github Pages](#basics)
    - [Getting Set Up](#set_up)
    - [Previewing Changes Locally](#preview_change)
    - [Pushing changes](#push_change)
3. [Modifying Existing Pages](#modify_page)
4. [Creating New Pages](#new_page)
5. [Creating New Blog Posts](#new_post)
6. [Modifying the Style](#style)
7. [Modifying the Theme](#theme)
8. [Modifying the Sidebar Links](#sidebar)
9. [Tips and Tricks](#tips_and_tricks)
    - Adding anchors to post/pages and linking to them.

<a name="background"></a> 
#### Required Background Knowledge

For this guide I will assume you know the basics of:

* Unix. This guide also assumes you are on a unix machine, or know how to perform the equivalent actions on windows.
* Installing python packages using `pip`.
* Writing documents in Markdown.
* Working with a fork of a GitHub repository.

<a name="basics"></a> 
#### Basics of Pelican and Github Pages

Pelican is a static site generator that requires no database or server-side logic. This means that Pelican can take in content (written in Markdown) and output a static web page (HTML/css/js). This makes it ideal for creating a site on GitHub Pages.

<a name="set_up"></a> 
##### Getting Set Up

To get started using Pelican, first you need Pelican! Use `pip` to get it.

```
pip install pelican markdown
```

Make sure you include `markdown` because we will use it.

Next, you must fork the [push-redux GitHub repo](https://github.com/erp12/push-redux). Once the repo is forked, clone the repo so you can edit your fork locally.

Once the repo is cloned, `cd` into the project folder. You should see the following folders and files.

```
content/
docs/
themes/
Makefile
pelicanconf.py
publishconf.py
```

There will likely be other files and folders in the `push-redux` repo, but won't need to talk about them in this guide.

The `content/` folder contains all of the Markdown files that make up the pages and posts in the final web page.

The `docs/` folder is where Github Pages looks for static web pages to display when a browser goes to `erp12.github.io/push-redux/`. This means that Pelican will place the HTML/css/js/etc in the `docs/` folder when we build our static website.

The `themes/` folder contains folders of themes that determine the layout and style of the Push Redux website. Pelican uses the [Jinja](http://jinja.pocoo.org/) template-ing engine to create themes. Modifying the contents of the `themes/` folder will only be necessary if you intend to modify the sites layout and style. 

`pelicanconf.py` and `publishconf.py` are python modules. They behave like simple settings files with Python syntax. These files will likely be the only Python coding required to contribute to the Push Redux, and it is very unlikely any modifications to these files will be needed.

The `Makefile` assists in building the Pelican project into a static site. See the next section.

<a name="preview_change"></a> 
##### Previewing Changes Locally

To preview the site locally, simply run the following command:

```
pelican path/to/push-redux/content -o path/to/push-redux/docs -s path/to/push-redux/pelicanconf.py
```

If you are on a Unix machine, this is made easier by the `Makefile`. Simply run `make html`.

>Be sure to check the console for any errors that occured wile building the site.

Now open the `path/to/push-redux/docs/index.html` file in your web browser to preview your changes.

>BE WARNED: As you navigate between pages, you may find yourself having to click on the `index.html` file for the folder you are in. This is normal. GitHub Pages displays the `index.html` file in the current directory by default. Once your changes go live on the main repository, this will not happen anymore.

<a name="push_change"></a> 
##### Pushing changes

After you make your changes locally, and have previewed them to ensure they look as intended, you will need to push these changes to your GitHub fork.

Once your changes are have been pushed to your GitHub fork, open a pull request between your fork and the main `push-redux` repository. This can be done from the GitHub website. More information about pull requests can be found [here](https://help.github.com/articles/creating-a-pull-request/) and [here](https://help.github.com/articles/about-pull-requests/).

One the pull request has been submitted, your changes will be reviewed and (most likely) accepted. Then your changes will be visible on the Push Redux GitHub Pages site!

<a name="modify_page"></a> 
#### Modifying Existing Pages

In Pelican projects, you can find the Markdown (.md) files for every pages in the `path/to/push-redux/content/pages/` folder. Every time the Pelican site is built, the Markdown files in the `content/` and `content/pages/` folders in converted into HTML files in the `docs/` folder.

To modify the text of a page, simply change the corresponding markdown file found in the `content/pages/` folder.

<a name="new_page"></a> 
#### Creating New Pages

When the Push Redux site is built, Pelican looks for any `.md` files in the `content/pages/` folder and converts them to HTML pages on the site. Thus, in order to make a new page on the Push Redux site, simply add a new Markdown file (with `.md` extension) in the `content/pages/` folder.

At the top of the Markdown file, you must enter some metadata. The metadata for this page looks like this:

```
Title: How to Contribute to the Push Redux
```

The `Title` value will be the title of the page. This will appear in large print at the top of the page. The `Title` value is the only metadata value that is *required* for pages. There are [more metadata values that could be set](http://docs.getpelican.com/en/3.6.3/content.html#file-metadata), but they will have no visible effect.

Notice the URL of this page: `pages/contributing/index.html`. The filename of the Markdown file this page was generated from is named `contributing.md`. When you create your Markdown file, be sure to give it a name that is 1) not the same as any other page and 2) the path you would like Pelican to place your page on.

Below the metadata (Title), you may write the content of the page.

<a name="new_post"></a> 
#### Creating New Blog Posts

Creating new blog posts is very similar to creating new Pages. When the site is built, Pelican looks for any `.md` files in the `content/` folder and converts them to HTML posts on the site. Thus, in order to make a new post simply add a new Markdown file (with `.md` extension) in the `content/` folder.

At the top of the Markdown file, you must enter some metadata. The metadata for a typical blog post looks like this:

```
Title: My post title
Date: 2016-11-22 5:00 
Modified: 2016-11-22 5:00
Category: PushGP
Slug: my-post-url
Authors: Your Name
Summary: A few sentences summarizing the post. When you browse through the blog posts, this is the text that is shown.
```

All of the above fields are strongly recommended, as they help Pelican generate the HTML for the posts in a way that looks like a non-static blog.

The `Modified` date is meant to be the most recent date the post was edited. If you are adding a new post, you should use the same date as the `Date` field.

Unlike pages, the URL of a post is determined by the `Slug` field.

Below the metadata, you may write the content of the post.

<a name="style"></a> 
#### Modifying the Style

The style of the Push Redux site is determined by the style-sheets included in the theme. The Push Redux site uses the theme found in the `themes/push-redux-theme/` folder. This theme is modified version of the theme found in the `themes/tuxlite_zf/` folder.

Unlike the `tuxlite_zf` theme, the `push-redux-theme` uses a style-sheet that customizes style components. This style sheet is located at `themes/push-redux-theme/static/css/push-style.css`.

If you modify the `push-style.css` file, you can change the style of the Push Redux site.

You can also add more css, js, and images to the `themes/push-redux-theme/static/` folder to change the style of the theme. If you do this, it is likely you will need to modify the HTML of the theme. (ie. Link a new style sheet or load a new javascript script). This will require changes to the Jinja theme files, which is explained in the next section.

<a name="theme"></a> 
#### Modifying the Theme

Pelican uses the [Jinja](http://jinja.pocoo.org/) theme engine to manage the theme of the website. If you look in the `themes/push-redux-theme` folder you should see two folders: `static/` and `templates/`. As mentioned in the previous section, the `static/` folder is where you put all of the external resources that will be included in the HTML of the theme. Javacript files, css style sheets, image files, etc should all be placed in the `static/` folder.

The `templates/` folder contains many `.html` files. These files are Jinja templates, which define how various HTML components of the Pelican site should be generated.

The `base.html` file contains the `<head>` that will be included in every generated HTML file, the navbar definition, and the sidebar definition. If you intend on adding your own scripts/style sheets, you will have to modify this file.

For larger changes to the `push-redux-theme` you will have to consult the [Jinja documentation](http://jinja.pocoo.org/docs/dev/).

<a name="sidebar"></a> 
#### Modifying the Sidebar Links

Modifying the sidebar links is done by modifying values in the `pelicanconf.py` file. In the `pelicanconf.py` file, there is a variable called `LINKS` which is defined as nested tuples. Each tuple consists of 1) the text that should appear in the sidebar and 2) the URL which the link should point to. Modify the `LINKS` tuple to change and rebuild the site to change the sidebar links.

<a name="tips_and_tricks"></a> 
#### Tips and Tricks

##### Anchors in Posts/Pages

Generally speaking, if you insert HTML into your Markdown files it will be preserved when the site is built. This can be used to put anchors throughout your Markdown document. This allows other pages to link directly to the location on the page which the achor is placed.

For example, in the Markdown file that creates this page the **Tips and Tricks** section looks like this:

```
<a name="tips_and_tricks"></a> 
#### Tips and Tricks
```

The `<a>` tag with the `name` attribute is an anchor. Now we can link to this anchor like this:

```
<a href="path/to/contributing/index.html#tips_and_tricks">
```
or
```
[text here](path/to/contributing/index.html#tips_and_tricks)
```

To link to an anchor found in the same page you are linking from, simply do the following:

```
[text here](#tips_and_tricks)
```

To see it in action [this link](#set_up) will bring you to the **Getting Set Up** section at the top of the page.