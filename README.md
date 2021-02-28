<p align="center"><img width=43.5% src="https://github.com/yashprakash13/Insight/blob/main/app/images/logo.png"></p>
<h1 align="center">Insight</h1>
<p align="center">The ultimate YouTube Comments Analyser Tool, brought to you as a NLP project.</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<p align="center"><img src="https://img.shields.io/badge/Built%20for-YouTube Creators-red?style=for-the-badge">   <img src="https://img.shields.io/badge/python-3.9.1-brightgreen?style=for-the-badge">   <img src="https://img.shields.io/badge/maintained-yes-blue?style=for-the-badge"></p>
<p align="center"><img src="https://img.shields.io/badge/Built-Jan--Feb'21-yellow?style=for-the-badge"></p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


## Table of Contents

## Understanding the motivation
The idea for this project was birthed from a tweet I saw about a famous YouTube creator saying that _a tool that can help analyse the enormous amount of comments that they get on each video_ wasn't yet present on the market. Being a data science practitioner and an avid YouTube fan, that tweet picked my brain and I was like, *this should be fun little challenge*. 

From then on, what began as an idea of a good, practical data science project, slowly developed into a full fledged web application with the help of the awesome frontend libary for data scientists called **Streamlit**(more later on this).

## How it works
Insight currently offers these features:
- Fetch all comments from any video from a YouTube video by pasting a URL, or
- Select and load any pre-existing csv file of comments that you might have already scraped before
- Perform the following operations on the comments:
  * Cluster the set of comments into different topics with a percentage assigned to each topic pertaining of how much people have talked about that something in the comments
  * Find top used emojis by the commentors 😍
  * Write a query and get comments semantically related to that query available to analyse
  * Form a pretty little word cloud of the comments, using any of the shapes in the drop down list like a cloud(duh), a dog, a retro camera, and others!


## See the app in action
Watch the demo video I made about the project (It's 3:06 minutes long. I worked very hard on this to **make it fun** rather than just a boring demo):

[![Watch the app in action on YouTube!](http://img.youtube.com/vi/3zhDx04Nxd8/0.jpg)](http://www.youtube.com/watch?v=3zhDx04Nxd8 "Insight Demo Video")


## Contribute to this project
I made Insight with two things in mind:
1. I wanted to build a real, usable app like this for the awesome YouTubers like [Peter Mckinnon](https://www.youtube.com/user/petermckinnon24) that I love.
2. I wanted to use and hone my skills in NLP by demonstrating its power to the world wth a practical app like this.

I have always been a backend-Java-Kotlin-Python guy and thus, I am unfortunately, very much lacking in frontend web development skills. Therefore, **if you are someone who is excited by the immense possibilites associated with this project and wants to make a modern, simplistic frontend for it**, PLEASE ping me in here via a [new Issue](https://github.com/yashprakash13/Insight/issues) or contact/DM me on [Twitter](https://twitter.com/csandyash) or [LinkedIn](https://www.linkedin.com/in/yashprakash13/) whenever you can. 

I would love to collab with someone like you who is eager to use his skills make this project more awesome! Thanks for being here anyway. :heart: 


## Try the app on your machine
1. Make a new directory to store the project:
```bash
mkdir InsightApp
```
2. **cd** into the directory:
```bash
cd InsightApp
```
3. Clone this repo: 
```bash
git clone https://github.com/yashprakash13/Insight.git
```
4. Make a new virtual environment. I recommend using **pipenv**:
```bash
pipenv shell
```
5. **cd** into the app directory:
```bash
cd Insight
```
6. Build the app with **docker**:
```bash
docker build --tag insight:1.0 .
```
7. Run the app:
```bash
docker run --publish 8501:8501 -it insight:1.0
```
8. Navigate to https://localhost:8501 to explore the app! Don't forget to see the [demo video](#see-the-app-in-action) first to make sure you have a good grasp of the app's workings!


## Support me
Did you like this project and the features that it enables or are you psyched by the awesome use of NLP demonstrated in here? Please consider supporting me! :)

**Buy me a :coffee: or a :beer:**


<a href='https://ko-fi.com/G2G3R125' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi3.png?v=2' border='0' alt='BBuy Me a Coffee or a Beer' /></a>
