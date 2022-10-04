[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=0077b6">](https://github.com/SamKirkland/FTP-Deploy-Action)
[![Netlify Status](https://api.netlify.com/api/v1/badges/2c8e5dc8-1df6-4b21-bfdb-77af3b1d525a/deploy-status)](https://app.netlify.com/sites/jolly-boyd-ddf9b1/deploys) 

# Licensing information
Please note that the MIT license does not apply to all the files shared in this repository. See [LICENSE.md](https://github.com/CorrelAid/hugo-website/blob/main/LICENSE) and [LICENSE-images.md](https://github.com/CorrelAid/hugo-website/blob/main/LICENSE-images.md) for details.

# How to's


## Add content

### Create a new page

1. Make a copy of a page which is found in the content folder under a language. These are markdown files `.md`
2. Change the yaml header to suit your new page:
   * The menu key will add a link in the top menu of the banner; its weight governs the ordering of the links
3. Create the content in your new page 
4. Ensure there's a version of the page for each language in the content folder
   
### Using images

Every image that is used for a blog entry has the size **800px\*500px**. Every picture for people is **500px\*500px**.

## Add an expert 

What information / content you need:
- name of expert
- image (500px x 500px)
- 2-3 words about the areas of their expertise (used for the subheader, see [here](https://correlaid.org/nonprofits/experts/))
- 2-3 description of the expert, in English and German
- optional but recommended, any of the following: GitHub profile link, Linkedin profile link, personal website

### Manually via GitHub interface

If you do not have write access to the website repository or you don't want to clone the repo and setup hugo, you can add (yourself as) an expert via the GitHub graphical interface:

1. Make sure you're logged into GitHub and that you have all the content ready.
2. open [this link](https://github.dev/CorrelAid/hugo-website/blob/add_experts/data/experts.json). It should open an editor in your browser.
2. Scroll to the end of the file and copy-paste the last block. Make sure to add a comma before it (invalid JSON will be underlined in red). 
3. Edit the key (`firstname_lastname`, e.g. `alex_musterperson`) and the content of your new block as needed. Available keys for social links are `website`, `github`, `linkedin` (check the other experts for examples).
4. In the sidebar, navigate to `static/images/people`. Right-click on `people` and click on "upload". Upload your square image. It needs to be named like the `image` element in `experts.json` from step 3. Pay attention to the file extension, lower-/uppercase and the separator (`_` or `-`).
5. Navigate to `content/en/nonprofits/experts.md`. Copy-paste any of the blocks and edit the `key` element to `firstname_lastname`. It needs to match the key from step 3. 
6. Repeat for `content/de/nonprofits/experts.md`.
7. In the sidebar, go to the Git tab. You should be able to commit your changes there. It might create a fork if you do not have write rights to the repository.
8. Go to https://github.com/correlaid/hugo-website/pulls and open your Pull Request (there should be a yellow sign)
9. Ping Frie via Slack to let them know about your PR, sending them the link to it. 

If you have any problems with the process, ask Frie. 

## Add an event

### Manually via GitHub interface

If you do not have write access to the website repository or you don't want to clone the repo and setup hugo, you can create an event via the GitHub graphical interface:

1. open [this link](https://raw.githubusercontent.com/CorrelAid/hugo-website/main/archetypes/news.md). Copy the content to your clipboard (ctrl/cmd + c).
2. Open [this link](https://github.com/CorrelAid/hugo-website/new/main/content/de/events). Edit the file name so that: 
- the month of the event is the folder, e.g. add `2022-09/`. GitHub will autocomplete that to a new folder.
- the file name has no spaces in it, e.g. `open-onboarding-call.md`. The file name, will be the URL of the event, so choose carefully :) 
- the file name ends in `.md`, indicating markdown format
3. Copy the content from 1. in the editor and edit away. Especially pay attention to the fiels in the YAML header at the beginning of the document, following the instructions in the comments (comments start with `#`).
4. Once you have finished your edits, ...
- if you don't have write access to the repository: click on "Propose new file" to make a Pull Request from your fork.  On the next page, click "Create Pull Request". Create a meaningful name for the Pull Request and a small (one-sentence) description. 
- if you have write access: select "create new branch and start a new Pull Request" and then click on "Propose new file" to make a branch and PR directly in the CorrelAid repository. On the next page, click "Create Pull Request", give it a meaningful title and short description. 
5. Repeat the process to add the event for the English page, replacing the link from step 2 with [this link](https://github.com/CorrelAid/hugo-website/new/main/content/en/events).
### Manually with Hugo installed

A template for event pages exists (a so called [archetype file](https://gohugo.io/content-management/archetypes/)). To use it, please proceed as follows:

1. in your terminal:

```
hugo new events/2022-09/my-event-name.md
```

This will create a markdown file with the given name under `content/de/events` (because "de" is our default language). 

2. Edit the file as needed, especially the YAML header - you'll find instructions in the comments. 
3. Copy the file to the appropriate location under `content/en/events` to also add the event to the English version of our website. 




## Add people to a page

detailed instructions coming soon. Pointer for now: edit [`data/people.json`](https://github.com/CorrelAid/hugo-website/blob/main/data/people.json) and refer to [this](https://raw.githubusercontent.com/CorrelAid/hugo-website/main/content/en/about/contact.md) on how to include it in Markdown content.
# Development
0. Licensing information
1. [Installation](#1-installation)
2. [Development](#2-development)
3. [Deployment](#3-deployment)
4. [Add Content](#4-add-content)


## 1. Installation

### 1.1 Install Hugo

You can find detailed installation instructions on the official hugo [website](https://gohugo.io/getting-started/installing/). Below you find the basic configurations to quickly install hugo on your local system. If you encounter any problems or require a special configuration visit the official website.

#### Windows

Congratulations! You are on the most complicated system for using hugo :tada:.

1. Download the latest zipped _Hugo Extended_ executable from [Hugo Releases](https://github.com/gohugoio/hugo/releases). The current version for 64-bit is called `hugo_extended_0.49_Windows-64bit.zip`.
2. Extract all contents to your `..\Hugo\bin` folder.
3. The hugo executable will be named as hugo_hugo-version_platform_arch.exe. Rename the executable to hugo.exe for ease of use.
4. In PowerShell or your preferred CLI, add the hugo.exe executable to your PATH by navigating to C:\Hugo\bin (or the location of your hugo.exe file) and use the command set `PATH=%PATH%;C:\Hugo\bin`.
5. Reboot your system.
6. Open the PowerShell or your preferred CLI and enter `hugo version` to verify your installation.

#### Mac

Use `brew` to install `hugo` on your local system. Run `hugo version` to verify your installation.

```
brew install hugo
```

#### Linux (Ubuntu 18.04)

Use `apt` to install `hugo` on your local system. Run `hugo version` to verify your installation.

```
sudo apt-get install hugo
```

### 1.2 Clone Directory

```
git clone https://github.com/CorrelAid/hugo-website.git
```

## 2. Development

Hugo provides a development server that enables _hot-reload_. The folder is watched by hugo and as soon as you change a file the website is automatically reloaded.

1. Open your favorite CLI and direct to the folder of your web application.
2. Use `hugo server -D` to start the development server. The `-D` flag is important to indicate that drafts are also shown.
3. Use CTRL + C to shutdown the server.



## 3. Deployment

1. Commit your changes to GitHub. If you're not an admin, you cannot push to the `main` branch, so please create a branch for your changes and then open a pull request. 
2. Pull requests to the `main` branched are built into a _deploy preview_ by Netlify. You will see this in the PR status checks. If you click on "Details" for the last status check (it should say something like "Deploy preview ready!"), you'll be taken to the deploy preview.
3. After someone has reviewed your changes and approved them, they'll be merged to `main` and automatically deployed to our FTP server by GitHub Actions. You can check the status of this deployment by looking at the "Actions" tab of the GitHub Repository. This will only happend if you have modified files that are actually relevant to the website, i.e. updating the README will not trigger a build.

