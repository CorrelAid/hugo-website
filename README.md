[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=0077b6">](https://github.com/SamKirkland/FTP-Deploy-Action)
[![Netlify Status](https://api.netlify.com/api/v1/badges/2c8e5dc8-1df6-4b21-bfdb-77af3b1d525a/deploy-status)](https://app.netlify.com/sites/jolly-boyd-ddf9b1/deploys) 

# CorrelAid Hugo Website
0. Licensing information
1. [Installation](#1-installation)
2. [Development](#2-development)
3. [Deployment](#3-deployment)
4. [Add Content](#4-add-content)

## 0. Licensing information

Please note that the MIT license does not apply to all the files shared in this repository. See [LICENSE.md](https://github.com/CorrelAid/hugo-website/blob/main/LICENSE) and [LICENSE-images.md](https://github.com/CorrelAid/hugo-website/blob/main/LICENSE-images.md) for details.

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

Every image that is used for a blog entry has the size **800px\*500px**.
