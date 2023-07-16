

I. BRIEF OVERVIEW OF THE TOPIC/PROBLEM 

Things on the internet contain a variety of information about almost everything that can be useful to people who can find it. Often, things like this are combined into a single file, and this file can be in the form of a 
document, an audio, and even a video. But browsing those websites where these files are located can consume mobile data which is not good for those who do not have unlimited Wi-Fi connections at home. Downloading these files is a solution to save mobile data and will be the focus of this project. Also, this can consume a significant amount of data, but the file is already saved on the phone or computer and can be viewed even without an internet connection which saves on mobile data as well as time. The goal of this project is to create a program that can download files on the internet that anybody can use. Downloadable files should only be 
in the form of audio, YouTube videos as well as videos other than YouTube with the highest quality, and specific documents such as xls, pdf, ppt, and docx.

II. ABOUT THE IDE/PACKAGE USED 

• IDE(Pycharm) 
We used Pycharm as our IDE to create this program. This IDE were 
recommended by our professor this semester since we start this subject course Computer Programming 2. Pycharm is an integrated development environment used in computer programming, specifically for the Python language and Pycharm is easy-to-use and beginner programming 
friendly especially to us students. 

• Tkinter 
We use this package in the GUI in our program. Tkinter is Python’s commonly used standard GUI (Graphical User Interface) package.

• Pytube 
We used Pytube package in our program to download YouTube videos. Pytube operate as the converter of YouTube links into a file. Pytube is a very serious, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

• MoviePy 
Moviepy package is a Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects. And its function in our program is to convert some mp4 file into mp3 file since YouTube only composed of mp4 files. 

• Request 
There are other links that are supported by our program due to this package it allows files outside the YouTube to be downloaded as a document. Request is designed to be the simplest way possible to make http calls. It supports HTTPS and follows redirects by default.

III. MAIN FLOW OF THE PROGRAM AND THE SOURCE CODES 

• The Flow of the Program starts at File Format where the User will be inputting what kind of File Format will he/she be downloading. Its either mp4, mp3, or document format

• The next one will inputting the file link for the to-be-downloaded File, and the output of the File will be depending on the Format you inputted, for example, if you inputted a YouTube Link, then depending on your File Format Input(mp4), the format of the downloaded YouTube will be mp4

• The next is setting up the Download Location of your File, it can be either typed in the Destination Text Box or browsed by clicking the Browse Button

• The Final Step will be Clicking the Download to start the Downloading Process, the Program will inform the User that the Downloading Process has begun and will also inform the User when the Download has completed 
