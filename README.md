# CorrelAid Hugo Website


## 1. Installation :gear:

### 1.1 Install Hugo

You can find detailed installation instructions on the official hugo [website](https://gohugo.io/getting-started/installing/). Below you find the basic configurations to quickly install hugo on your local system. If you encounter any problems or require a special configuration visit the official website.

#### Windows

Congratulations! You are on the most complicated system for any programming :tada:.

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


## 2. Development :keyboard:

Hugo provides a development server that enables _hot-reload_. The folder is watched by hugo and as soon as you change a file the website is automatically reloaded.

1. Open your favorite CLI and direct to the folder of your web application.
2. Use `hugo server -D` to start the development server. The `-D` flag is important to indicate that drafts are also shown.
3. Use CTRL + C to shutdown the server.



## 3. Deployment :computer:

1. Run `hugo`.
2. Copy the complete content of the `public` directory to the web server.