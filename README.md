### Youtube Videos

1. [Antigravity SDK 2.0 For Beginners](https://www.youtube.com/watch?v=JoQ3bbusX9Y)

2. [
Understanding Tools, Hooks & Observability in Antigravity SDK 2.0](https://www.youtube.com/watch?v=Qfdd2Qpbtik)

3. [
Custom Slash Commands for Antigravity 2.0](https://www.youtube.com/watch?v=_aAd-OlFzNM)

4. [Using custom scripts with Agent Skills and Antigravity](https://www.youtube.com/watch?v=ZnYc_8AO-9o)

5. [
Agent Skills with Antigravity CLI](https://www.youtube.com/watch?v=eMy8WZSWS4I)


# How to run
## Step 1: Install Antigravity
**Mac / Linux**
```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```
**Windows PowerShell**
```
irm https://antigravity.google/cli/install.ps1 | iex
```

## Step 2: Clone the repository
```bash
   git clone https://github.com/10xroadmap/agent-skills-using-google-antigravity-cli
   cd agent-skills-using-google-antigravity-cli
```

## Step 3: Launch Antigravity
Run the command below in your terminal to start the CLI.
```bash
agy
```
- This will initiate Google Authentication, if you are not already authenticated.
- To start using the Antigravity CLI, you need to authenticate with Google. You can typically log in using your standard Google account.

## Step 4: Using Antigravity CLI
- Once antigravity terminal is activated, you may start giving prompt:
```
How many files are there in current folder
```
```
Which file is last modified
```

# Creating skills
1. Create .agents folder
```
mkdir .agents
```
2. Create .agents/skills folder
```
mkdir .agents/skills
```
3. Create folder for your skill 
```
mkdir .agents/skills/funny-names folder
```
4. Create SKILL.md
```
touch .agents/skills/funny-names/SKILL.md
```
After Skill is written and saved, you may test skill inside agy terminal
```
agy -p ""
```
- To test skill **`funny-names`**, type:
``Suggest a funny name for Dennis Ritchie``

- To test skill **`public-repo-count`**, type:
`Find the number of public repositories created by user 10xroadmap`

- To test skill **`fotd`**, type:
`Generates forecast for Smith who is male and is 23 years old`

# What the skills demonstrated ?
- `funny-names` is a simple skill
- `public-repo-count` demonstrates how we can use bash script inside skill. You may customize it for Windows PoerShell
- `fotd`(forecast of the day) demonstrates how we can use python script inside skill. 

# GIT REPO URL
https://github.com/10xroadmap/agent-skills-using-google-antigravity-cli 

# License or Terms of Use
This project is open-source. However, no part of the source code may be republished, modified, or distributed for commercial or public purposes without giving appropriate credit to the original author.
