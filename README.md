# Python

A project for learning the basics of **Python** programming language. My purpose is to learn best practices for writing—in theory—production-grade **Python** that is clean, efficient, and maintainable.


## Table of Contents

- [Software Installation and Setup](https://github.com/Pece17/Python?tab=readme-ov-file#software-installation-and-setup)


## Software Installation and Setup

First I need to set up the environment where I'll be writing **Python** codes and programs. Many people on **Reddit** suggest **Visual Studio Code**/**VS Code**, and it should do fine for simple programs at this stage. My antique desktop PC is still running **Windows 7** so I'll need a legacy **VS Code** version that supports it. A quick **Google** search reveals that **version 1.70** is what I'm looking for.

I go to https://code.visualstudio.com/updates/v1_70 and download the **x64** version. I go through the installation, use the default settings, after which **VS Code** launches.

**ChatGPT** says I should install **Python extension for Visual Studio Code**, so I select the **Extensions** icon on the left sidebar in **VS Code**, write **Python** on the search bar, and select **Install Release Version**.

After the installation is complete, I click **Create Python File** and save the file as **Hello_World.py**.

At this point I need to actually install **Python** on my computer, so I go to https://www.python.org/downloads/windows/, find version **3.8.6** (the latest compatible version with **Windows 7**), and download **Windows x86 executable installer**.

After downloading, I right-click on **python-3.8.6.exe**, select **Run as administrator**, unselect **Install launcher for all users (recommended)**, and click **Install Now**. I check that **Python** has been installed by opening **cmd.exe**/**Windows Command Prompt** and entering command ```py --version```. The terminal outputs ```Python 3.8.6```, so we're good to go.

Now I go back to **VS Code** and **Hello_World.py** file, and write a very simple program:

```
print("Hello, World!")
```

I try to run the code in **VS Code** by clicking the ▶️ (play) button, but get an error and a button saying **Select Python Interpreter**. I click on it, type **Python: Select Interpreter** on the search bar as per **ChatGPT**'s instructions, and paste the path of the **python.exe** file on my PC. In my case it is: ```C:\Users\Business\AppData\Local\Programs\Python\Python38-32\python.exe```. Now I run the file again, and get the following output:

```
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/Hello_World.py
Hello, World!
PS C:\Users\Business>
```

**VS Code** and **Python** seem to work correctly, so I can move on to more complex exercises.


## Placeholder Title
