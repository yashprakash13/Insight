<p align="center"><img width=43.5% src="https://github.com/yashprakash13/Insight/blob/main/app/images/logo.png"></p>
<h1 align="center">Insight</h1>
<p align="center">The ultimate YouTube Comments Analyser Tool, brought to you as a NLP project.</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<p align="center"><img src="https://img.shields.io/badge/Built%20for-YouTube Creators-red?style=for-the-badge">   <img src="https://img.shields.io/badge/python-3.9.1-brightgreen?style=for-the-badge">   <img src="https://img.shields.io/badge/maintained-yes-blue?style=for-the-badge"></p>
<p align="center"><img src="https://img.shields.io/badge/Built-Jan--Feb'21-yellow?style=for-the-badge"></p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


## Table of Contents
| Topics      | Jump to Link |
| ----------- | ----------- |
| Why I built this app      |  [because the thought matters](https://github.com/yashprakash13/Insight#understanding-the-motivation) |
| How Insight works   | [so that you love it as much I do](https://github.com/yashprakash13/Insight#how-it-works)  |
| Watch the demo video I made for the app | [this was hard to make but I enjoyed it very much](https://github.com/yashprakash13/Insight#see-the-app-in-action)   |
| Contribute to this app (built a frontend) | [yes, please. You're welcome to. ](https://github.com/yashprakash13/Insight#contribute-to-this-project)   |
| Run the app on your machine | [so you get a taste](https://github.com/yashprakash13/Insight#try-the-app-on-your-machine)  |
| How I built this app (included with tutorials) | [tools I used to make it happen](https://github.com/yashprakash13/Insight#how-i-built-this-app) |
| Your support matters!  | [I would appreciate it very much](https://github.com/yashprakash13/Insight#support-me)  |


## Understanding the motivation
The idea for this project was birthed from a tweet I saw about a famous YouTube creator saying that _a tool that can help analyse the enormous amount of comments that they get on each video_ wasn't yet present on the market. Being a data science practitioner and an avid YouTube fan, that tweet picked my brain and I was like, *this should be fun little challenge*. 😸

From then on, what began as an idea of a good, practical data science project, slowly developed into a full fledged web application with the help of the awesome frontend libary for data scientists called **Streamlit**(more later on this). 

## How it works
Insight currently offers these features:
- Fetch all comments from any video from a YouTube video by pasting a URL, or
- Select and load any pre-existing csv file of comments that you might have already scraped before
- Perform the following operations on the comments:
  * Cluster the set of comments into different topics with a percentage assigned to each topic pertaining of how much people have talked about that something in the comments
  * Find top used emojis by the commentors 😍
  * Write a query and get comments semantically related to that query available to analyse
  * Form a pretty little word cloud of the comments, using any of the shapes in the drop down list like a cloud(duh), a dog, a retro camera, and some others!


## See the app in action
This is what the app looks like:
![Demo GIF](https://github.com/yashprakash13/Insight/blob/main/app/images/Screen%20Recording%202021-02-28%20at%2011.10.26%20PM.gif)


You can also watch the demo video I made about the project (It's 3:16 long. I worked very hard on this to **make it fun** rather than just a boring demo):

<a href="http://www.youtube.com/watch?v=3zhDx04Nxd8"> <img src="https://lh3.googleusercontent.com/3zkP2SYe7yYoKKe47bsNe44yTgb4Ukh__rBbwXwgkjNRe4PykGG409ozBxzxkrubV7zHKjfxq6y9ShogWtMBMPyB3jiNps91LoNH8A=s500" width="148"> </a>

## Contribute to this project
I made Insight with 2️⃣ things in mind:
1. I wanted to build a real, usable app like this with inspiration from some of the awesome YouTubers like [Peter Mckinnon](https://www.youtube.com/user/petermckinnon24) that I love. His videos are actually being used in the demo video I made. Go watch it 👆🏻.
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

**If you want to build your own comments dataset with this app**, feel free to follow the entire process [I described in this blog post](https://medium.com/this-code/how-to-make-a-youtube-video-comments-dataset-with-the-googles-python-api-34cf32a14d16?source=your_stories_page-------------------------------------). This will help you make your own ```creds.json``` file that you can keep in the root project directory when you run the app.

**I'm also making an online course-ebook with the WHOLE guide to building this project.** [You can book your copy here.](https://tremendous-founder-3862.ck.page/69e31e7b71) It's free too. :)

## How I built this app
Insight was built with these major components. A huge thank you to their creators for making these amazing tools available for free.
* [Google YouTube API](http://cloud.google.com) -> to download comments from videos, as I've described [here](https://medium.com/this-code/how-to-make-a-youtube-video-comments-dataset-with-the-googles-python-api-34cf32a14d16?source=your_stories_page-------------------------------------).
* [Sentence Transformers](https://sbert.net) -> to enable semantic similarity search and information retrieval with by computing sentence embeddings, as described [here](https://pub.towardsai.net/a-quick-introduction-to-semantic-clustering-for-large-texts-3660a77b9611?source=your_stories_page-------------------------------------).
* [Streamlit](https://www.streamlit.io/) -> the easy frontend development library for backend people like me :P I wrote a detailed blog post around it too [here](https://towardsdatascience.com/a-guide-to-streamlit-frontend-for-data-science-made-simpler-c6dda54e3183?source=your_stories_page-------------------------------------).
* [Docker](https://www.docker.com/) -> to easy deploy the app as a stand-alone container, like I've written [here](https://pub.towardsai.net/how-to-dockerize-your-data-science-project-a-quick-guide-b6fa2d6a8ba1?source=your_stories_page-------------------------------------).

You might have a good idea by now that I absolutely LOVE to write. 😁

## Support me
Did you like this project and the features that it enables or are you hyped by the awesome use of NLP demonstrated in here? Please consider supporting me! :)

**Buy me a :coffee: or a :beer:**


<a href='https://ko-fi.com/G2G3R125' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi3.png?v=2' border='0' alt='BBuy Me a Coffee or a Beer' /></a>
