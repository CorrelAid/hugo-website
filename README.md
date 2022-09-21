[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=0077b6">](https://github.com/SamKirkland/FTP-Deploy-Action)
[![Netlify Status](https://api.netlify.com/api/v1/badges/2c8e5dc8-1df6-4b21-bfdb-77af3b1d525a/deploy-status)](https://app.netlify.com/sites/jolly-boyd-ddf9b1/deploys) 

# Licensing information
Please note that the MIT license does not apply to all the files shared in this repository. See [LICENSE.md](https://github.com/CorrelAid/hugo-website/blob/main/LICENSE) and [LICENSE-images.md](https://github.com/CorrelAid/hugo-website/blob/main/LICENSE-images.md) for details.

# How to's
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

### Via the CorrelAid Events Calendar
An automated bridge exists that can add events from the [CorrelAid Events Calendar](https://calendar.google.com/calendar/embed?src=c_3mg1mfpa10cg1a03ogkrg6v1n4%40group.calendar.google.com&ctz=Europe%2FBerlin) to the Hugo website.

:warning: Due to the experimental nature of the workflow, it is recommended to only use this for events with low time pressure to allow for potential debugging. Good candidates are recurring events such as the open onboarding call. If you need your event to appear on the website asap, please use one of the "manual" methods described above. :warning:


**Prerequisites**:
- CorrelAid Google Workspace account. Request [here](https://docs.google.com/forms/d/e/1FAIpQLScJYiZDTlo0S4N7eeRVyo7GgSHFzdiaKvBt5RJ8C5Fo_22r0g/viewform) if you are an active member of CorrelAid. If you are an external person who stumbled here and you want to add an event, please reach out to info at correlaid dot org. 
- Write access to the CorrelAid Events Calendar. Request via Slack DM from Frie or Isabel. 
- added CorrelAid Events Calendar to your calendar.google.com view, see [instructions here](https://docs.correlaid.org/wiki/infrastructure/google-workspace#displaying-group-calendars). The calendar ID is: `c_3mg1mfpa10cg1a03ogkrg6v1n4@group.calendar.google.com`


**Steps**:
1. Open [calendar.google.com](https://calendar.google.com)
2. Create a new event in the CorrelAid Events Calendar. 
3. Edit title and time as usual. The title will be the title of the event on the website. If it is a recurring event, you *need* to set an end to the schedule (and **not** let it run forever). Otherwise, it'll crash the pipeline because there will be an indefinite amount of events.
4. Copy the following YAML header into the description field (including the `---`) and edit it (see explanation in the table below):

```
---
website: true 
correlaidx: false
tags: [] 
slug: ""
---
```


variable | values | what it does 
---------|----------|---------
 website | true or false | toggles whether event is on website
 correlaidx | true or false | if true, use blue/red design for event instead of green/blue
 tags | list of comma-separated tags, e.g. [dataviz, data4good] | displayed under the event on the [list view](https://correlaid.org/events) as list of hashtags

5. under the header, add your description of the event in English or German. Use the formatting options provided by Google Calendar. Save the event. 
6. Check the next day whether it has worked (reload the CorrelAid website if it was open). If it hasn't worked, reach out to Frie via Slack.
- if you do not want to wait until the next day: wait half an hour and then go to [GitHub Actions](https://github.com/CorrelAid/hugo-website/actions) and trigger the website build manually. 

**To delete an event from the website**

--> delete the YAML header or set `website` to `false`.


**How it works**

- each half an hour, a [Pipedream](https://pipedream.com/) workflow gets the newly created or updated events from the CorrelAid Events Calendar and inputs them into a Google Sheets spreadsheet in a tabular form. 
- our [nightly website build GitHub Action](https://github.com/CorrelAid/hugo-website/blob/main/.github/workflows/deploy-website.yml) pulls the events from the Google Spreadsheet and transforms them into markdown files which are then part of the hugo build process.

**Limitations**
- Events created this way are not tracked in GitHub as they are generated on the fly in the GitHub action (see "how it works"). I.e. there is no way to make small fixes via GitHub later. To track the events as files in GitHub would require an additional layer to map events in Google Calendar to file operations (e.g. deletion of event in GCal -> deletion of file)
- Time delay: The pipeline operates asynchronously, GitHub Action only running once a day. A possible extension would be to trigger a rebuild from pipedream directly via a webhook - however this might result in an unnecessary amount of GitHub Action runs if events are edited often (-> to be avoided for environmental reasons). 







## Add people to a page

detailed instructions coming soon. Pointer for now: edit [`data/people.json`](https://github.com/CorrelAid/hugo-website/blob/main/data/people.json) and refer to [this](https://raw.githubusercontent.com/CorrelAid/hugo-website/main/content/en/about/contact.md) on how to include it in Markdown content.
# Development
0. Licensing information
1. [Installation](#1-installation)
2. [Development](#2-development)
3. [Deployment](#3-deployment)
4. [Add Content](#4-add-content)

## 

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

## 4. Add content

### 4.1 Create a new page

1. Make a copy of a page which is found in the content folder under a language. These are markdown files `.md`
2. Change the yaml header to suit your new page:
   * The menu key will add a link in the top menu of the banner; its weight governs the ordering of the links
3. Create the content in your new page 
4. Ensure there's a version of the page for each language in the content folder
   
 

### 4.2 Using images

Every image that is used for a blog entry has the size **800px\*500px**. Every picture for people is **500px\*500px**.
