Title: All you need is to use pelican and github pages to write blogs
Date: 2025-8-25
Tags: python, pelican, pages, blog
Description: How to Build a Blog with Pelican and GitHub Pages: No Tech Degree Required!
Category: Tutorial


## Introduction

Hey there, future blog superstar! 😎 Want to share your thoughts, memes, or cat-pic reviews with the world? You don’t need to be a coding ninja to make a slick blog. With **Pelican** (a Python-powered static site generator) and **GitHub Pages** (free hosting, yay!), you can have a blog up faster than you can say “I forgot my Wi-Fi password.” Let’s make it happen with this step-by-step guide that’s easier than assembling IKEA furniture.


## Why Pelican and GitHub Pages?
- **Pelican**: It’s like a magical typewriter that turns simple text files into a beautiful website. No databases, no drama—just pure, static HTML goodness.
- **GitHub Pages**: Free hosting by GitHub. It’s like renting a penthouse for $0, except it’s a website, and there’s no rooftop pool (yet).

Ready? Let’s roll! 🚀


## Step 1: Get Your Tools Ready
Before we start, make sure you have:
- **Python** (3.8 or higher): Pelican runs on Python, so grab it from [python.org](https://www.python.org/downloads/) if you haven’t already. Think of Python as the coffee that powers this blogging machine.
- **Git**: You’ll need Git to push your blog to GitHub. Download it from [git-scm.com](https://git-scm.com/).
- **Make**: Pelican’s `make github` command uses `make` to automate deployment. Most Linux/macOS systems have it; Windows users can install it via [MinGW](http://www.mingw.org/) or WSL.
- A **GitHub account**: If you don’t have one, sign up at [github.com](https://github.com). It’s free, and you’ll feel like a coder just by logging in.
- A text editor: VS Code, Sublime Text, or even Notepad will do. This is where you’ll write your blog posts in Markdown (fancy text, basically).

Got all that? Sweet, you’re ready to rumble!


## Step 2: Install Pelican
Pelican is a Python package, so we’ll use `pip` to install it. Open your terminal (or Command Prompt on Windows) and type:

```bash
pip install pelican markdown
```

- `pelican`: The star of the show, turning your text into a website.
- `markdown`: Lets you write blog posts in Markdown, which is like texting but for blogs.

If you see some installation gibberish and no errors, you’re golden. If you get errors, double-check that Python and `pip` are installed correctly (`pip --version` should tell you something useful).


## Step 3: Create a Pelican Project
Time to set up your blog’s skeleton. In your terminal, navigate to a folder where you want your blog to live (e.g., `~/my-blog`), then run:

```bash
pelican-quickstart
```

Pelican will ask you a bunch of questions. Here’s how to answer them (feel free to tweak as needed):
- **Where do you want to create your new project?** Just hit Enter to use the current folder.
- **What will be the title of this web site?** Pick something cool like “My Epic Blog.”
- **Who will be the author of this web site?** That’s you! Put your name or “Blogging McBlogface.”
- **What will be the default language?** Probably “en” for English, unless you’re feeling fancy.
- **Do you want to specify a URL prefix?** For GitHub Pages, enter `https://<your-username>.github.io/<repo-name>` (e.g., `https://coolcoder.github.io/my-blog`).
- **Do you want to enable article pagination?** Say “y” (yes) for now—it’s nice for readers.
- **What is your time zone?** Something like “America/New_York” or “Europe/London.” Google “Python time zones” if you’re unsure.
- **Do you want to generate a tasks.py/Makefile to automate generation and publishing?** Say “y” (yes)—this gives you the `Makefile` we’ll use for `make github`.

Boom! Pelican just created a bunch of folders and files, including a `Makefile` for easy deployment. Don’t panic—they’re just the scaffolding for your blog.


## Step 4: Write Your First Blog Post
Your blog posts live in the `content` folder as Markdown files (`.md`). Let’s write one! Create a file called `first-post.md` in the `content` folder with this content:

```markdown
Title: My First Blog Post
Date: 2025-08-25 12:00
Category: Blog
Tags: first, blog, awesomeness
Slug: my-first-post
Author: Your Name

Hello, world! This is my *awesome* blog, powered by Pelican and GitHub Pages. I’m basically a tech wizard now. Stay tuned for more epic content, like how to microwave popcorn without burning it.
```

Save it, and you’ve just written your first post! Markdown is super simple: use `#` for headings, `*` for italics, `**` for bold, and lists are just `-` or `*`. Google “Markdown cheatsheet” if you want to get fancy.


## Step 5: Generate Your Site
Now, let’s turn your Markdown into a website. In your terminal, navigate to your project folder and run:

```bash
make html
```

This tells Pelican to grab your `content` folder and spit out a shiny website in the `output` folder. Check the `output` folder—you’ll see HTML files, CSS, and other goodies.

To preview your site locally, run:

```bash
make serve
```

Open your browser and go to `http://localhost:8000`. Behold, your blog! It’s probably using Pelican’s default theme, which is like wearing a plain T-shirt—functional but not super stylish. We’ll fix that later.


## Step 6: Set Up GitHub Pages with make github
Time to share your blog with the world using Pelican’s `make github` command for a super-smooth deployment:

1. **Create a GitHub Repository**:
   - Go to [github.com](https://github.com) and click “New repository.”
   - Name it `<your-username>.github.io` (e.g., `coolcoder.github.io`) for a personal site, or any name if it’s a project site (e.g., `my-blog`).
   - Make it public and initialize it with a README.

2. **Initialize Your Local Repo**:
   - In your project folder (where `pelicanconf.py` and `Makefile` live), initialize a Git repo:
     ```bash
     git init
     git add .
     git commit -m "My awesome blog begins!"
     ```
   - Link it to your GitHub repo:
     ```bash
     git remote add origin https://github.com/<your-username>/<repo-name>.git
     git branch -M main
     git push -u origin main
     ```

3. **Configure the Makefile**:
   - Open the `Makefile` in your project folder. Ensure it has a `github` target (it should, thanks to `pelican-quickstart`). Look for lines like:
     ```makefile
     github: publish
         ghp-import -n -p -f output
     ```
   - This uses `ghp-import` under the hood, so let’s install it:
     ```bash
     pip install ghp-import
     ```

4. **Push Your Site to GitHub Pages**:
   - Generate and publish your site in one go:
     ```bash
     make github
     ```
   - This runs `pelican content` to generate your site, then uses `ghp-import` to push the `output` folder to the `gh-pages` branch, which GitHub Pages uses to serve your site.

5. **Configure GitHub Pages**:
   - Go to your repo on GitHub, click “Settings,” then “Pages.”
   - Under “Source,” select “Deploy from a branch” and choose the `gh-pages` branch.
   - Save, and GitHub will give you a URL like `https://<your-username>.github.io` (or `https://<your-username>.github.io/<repo-name>` for project sites). Wait a few minutes, and your blog should be live!


## Step 7: Update Your Blog
Want to add a new post or update your blog? It’s as easy as eating leftover pizza:
1. Write a new `.md` file in the `content` folder (like `second-post.md`).
2. Generate and publish your updated site:
   ```bash
   make github
   ```
3. Wait a minute or two, and your updated blog will be live! The `make github` command handles everything—generating the site and pushing it to the `gh-pages` branch. No manual file copying or branch juggling required.



## Step 8: Make It Pretty (Optional)
Pelican’s default theme is… meh. To spice it up:
- Browse themes at [pelicanthemes.com](http://pelicanthemes.com/) or GitHub.
- Clone a theme to your project’s `themes` folder:
  ```bash
  git clone https://github.com/getpelican/pelican-themes themes
  ```
- Update `pelicanconf.py` in your project folder to use the theme. Add:
  ```python
  THEME = "themes/<theme-name>"
  ```
- Regenerate and publish your site with `make github`.


## Step 9: Keep Blogging!
To keep your blog fresh, just add more `.md` files to the `content` folder and run `make github`. It’s like sending postcards to the internet, but cooler.


## Troubleshooting: When Things Go Wrong
- **Pelican or ghp-import not found?** Make sure they’re installed (`pip show pelican ghp-import`).
- **make: command not found?** Install `make` (e.g., via MinGW on Windows or `sudo apt install make` on Linux).
- **Site not updating on GitHub?** Ensure you ran `make github` and check that the `gh-pages` branch is set in GitHub Pages settings.
- **Looks like a 90s website?** Grab a better theme or tweak the CSS in `pelicanconf.py`.


## You’re a Blogger Now!
Congrats, you’ve just built a blog with Pelican and GitHub Pages! 🎉 The `make github` command makes updating your blog so easy you’ll have time to argue about pineapple on pizza. Go write about your favorite taco recipe, your pet’s secret talents, or why Comic Sans isn’t *that* bad. Share your blog link with friends, and bask in your new tech cred. 

Happy blogging, you internet rockstar! 🌟

