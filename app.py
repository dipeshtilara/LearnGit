import streamlit as st
import os
import json
from datetime import datetime
import time

# app.py
from pathlib import Path
import streamlit as st

def load_css():
    css_path = Path(__file__).parent / "styles.css"   # <- file is at repo root
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>",
                unsafe_allow_html=True)



# Page Configuration
st.set_page_config(
    page_title="GitHub Tutorial for 9th Graders",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="expanded"
)

'''
# Load custom CSS
def load_css():
    with open('streamlit_conversion/styles.css', 'r') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
'''

# Initialize session state for progress tracking
def initialize_session_state():
    if 'progress' not in st.session_state:
        st.session_state.progress = {
            'pages': {},
            'overall_progress': 0,
            'total_pages': 11,
            'current_page': 'home',
            'started_at': datetime.now().isoformat(),
            'last_activity': datetime.now().isoformat(),
            'quiz_scores': {},
            'time_spent': {}
        }
    
    if 'achievements' not in st.session_state:
        st.session_state.achievements = {
            'first_steps': False,
            'setup_master': False,
            'concept_explorer': False,
            'repository_creator': False,
            'command_line_pro': False,
            'team_player': False,
            'best_practice': False,
            'quiz_master': False,
            'knowledge_seeker': False,
            'complete_journey': False,
            'dedicated_learner': False,
            'project_builder': False,
            'resource_collector': False
        }
    
    if 'quiz_data' not in st.session_state:
        st.session_state.quiz_data = {
            'current_section': None,
            'current_question': 0,
            'answers': {},
            'show_feedback': False,
            'quiz_completed': False
        }

# Progress tracking functions
def mark_page_visited(page_id):
    st.session_state.progress['current_page'] = page_id
    st.session_state.progress['last_activity'] = datetime.now().isoformat()
    
    if page_id not in st.session_state.progress['pages']:
        st.session_state.progress['pages'][page_id] = {
            'last_visited': datetime.now().isoformat(),
            'completed': False,
            'time_spent': 0,
            'visits': 1
        }
    else:
        st.session_state.progress['pages'][page_id]['visits'] += 1
        st.session_state.progress['pages'][page_id]['last_visited'] = datetime.now().isoformat()
    
    # Calculate overall progress
    completed_pages = sum(1 for page in st.session_state.progress['pages'].values() if page['completed'])
    st.session_state.progress['overall_progress'] = int((completed_pages / st.session_state.progress['total_pages']) * 100)
    
    # Check for achievements
    check_achievements()

def mark_page_completed(page_id):
    if page_id in st.session_state.progress['pages']:
        st.session_state.progress['pages'][page_id]['completed'] = True
        st.session_state.progress['pages'][page_id]['completion_date'] = datetime.now().isoformat()
        
        # Recalculate progress
        completed_pages = sum(1 for page in st.session_state.progress['pages'].values() if page['completed'])
        st.session_state.progress['overall_progress'] = int((completed_pages / st.session_state.progress['total_pages']) * 100)
        
        # Check for achievements
        check_achievements()

def record_quiz_score(section, score, total_questions):
    st.session_state.progress['quiz_scores'][section] = {
        'score': score,
        'total': total_questions,
        'percentage': int((score / total_questions) * 100),
        'completed_at': datetime.now().isoformat()
    }
    
    # Check for quiz-related achievements
    check_achievements()

# Achievement system
def check_achievements():
    progress = st.session_state.progress
    achievements = st.session_state.achievements
    
    # First Steps - visited first page
    if not achievements['first_steps'] and len(progress['pages']) > 0:
        achievements['first_steps'] = True
        show_achievement_unlock("First Steps", "Welcome to your GitHub journey! 🐙")
    
    # Setup Master - completed getting started
    if not achievements['setup_master'] and progress['pages'].get('getting-started', {}).get('completed', False):
        achievements['setup_master'] = True
        show_achievement_unlock("Setup Master", "You've mastered the basics!")
    
    # Concept Explorer - completed core concepts
    if not achievements['concept_explorer'] and progress['pages'].get('concepts', {}).get('completed', False):
        achievements['concept_explorer'] = True
        show_achievement_unlock("Concept Explorer", "You understand the fundamentals!")
    
    # Repository Creator - completed first repository
    if not achievements['repository_creator'] and progress['pages'].get('first-repo', {}).get('completed', False):
        achievements['repository_creator'] = True
        show_achievement_unlock("Repository Creator", "You've created your first repo!")
    
    # Command Line Pro - completed command line
    if not achievements['command_line_pro'] and progress['pages'].get('command-line', {}).get('completed', False):
        achievements['command_line_pro'] = True
        show_achievement_unlock("Command Line Pro", "CLI mastery achieved!")
    
    # Team Player - completed collaboration
    if not achievements['team_player'] and progress['pages'].get('collaboration', {}).get('completed', False):
        achievements['team_player'] = True
        show_achievement_unlock("Team Player", "Ready to collaborate!")
    
    # Best Practice - completed best practices
    if not achievements['best_practice'] and progress['pages'].get('best-practices', {}).get('completed', False):
        achievements['best_practice'] = True
        show_achievement_unlock("Best Practice", "You follow best practices!")
    
    # Complete Journey - completed all pages
    if not achievements['complete_journey'] and progress['overall_progress'] == 100:
        achievements['complete_journey'] = True
        show_achievement_unlock("Complete Journey", "🎉 You've completed the entire tutorial!")
    
    # Quiz Master - 100% on any quiz
    if not achievements['quiz_master']:
        for section, data in progress['quiz_scores'].items():
            if data['percentage'] == 100:
                achievements['quiz_master'] = True
                show_achievement_unlock("Quiz Master", "Perfect score achieved!")
                break
    
    # Knowledge Seeker - 80%+ average across quizzes
    if not achievements['knowledge_seeker'] and len(progress['quiz_scores']) > 0:
        avg_score = sum(data['percentage'] for data in progress['quiz_scores'].values()) / len(progress['quiz_scores'])
        if avg_score >= 80:
            achievements['knowledge_seeker'] = True
            show_achievement_unlock("Knowledge Seeker", "Strong knowledge demonstrated!")

def show_achievement_unlock(title, message):
    st.success(f"🏆 Achievement Unlocked: {title} - {message}")
    time.sleep(2)

# Sidebar Navigation
def render_sidebar():
    with st.sidebar:
        st.markdown("## 🐙 GitHub Tutorial")
        
        # Progress indicator
        st.markdown("### Your Progress")
        progress_bar = st.progress(st.session_state.progress['overall_progress'] / 100)
        st.caption(f"{st.session_state.progress['overall_progress']}% Complete")
        
        # Achievement count
        unlocked_count = sum(1 for unlocked in st.session_state.achievements.values() if unlocked)
        total_achievements = len(st.session_state.achievements)
        st.markdown(f"### 🏆 Achievements")
        st.markdown(f"**{unlocked_count}/{total_achievements}** Unlocked")
        
        st.markdown("---")
        
        # Navigation
        st.markdown("### Navigation")
        
        pages = {
            "🏠 Home": "home",
            "📖 Getting Started": "getting-started",
            "🎯 Core Concepts": "concepts",
            "💻 First Repository": "first-repo",
            "⌨️ Command Line": "command-line",
            "🤝 Collaboration": "collaboration",
            "⭐ Best Practices": "best-practices",
            "🚀 Real Projects": "real-projects",
            "📝 Practice Quiz": "practice",
            "📚 Resources": "resources",
            "⚡ Quick Reference": "quick-reference"
        }
        
        current_page = st.session_state.progress.get('current_page', 'home')
        
        # Render navigation items with status indicators
        for display_name, page_id in pages.items():
            is_completed = st.session_state.progress['pages'].get(page_id, {}).get('completed', False)
            is_current = current_page == page_id
            
            status_indicator = "✅" if is_completed else "🔄" if st.session_state.progress['pages'].get(page_id, {}).get('last_visited') else "⭕"
            
            if st.button(f"{status_indicator} {display_name}", key=page_id, use_container_width=True):
                st.session_state.current_page = page_id
                st.rerun()
        
        st.markdown("---")
        
        # Reset progress button
        if st.button("🔄 Reset Progress", use_container_width=True):
            st.session_state.clear()
            st.rerun()

# Page rendering functions
def render_home_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="hero-section">
            <h1>Learn GitHub Like a Pro</h1>
            <p class="hero-subtitle">Master version control with GitHub in this interactive tutorial designed for 9th graders</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Dashboard widgets
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="dashboard-card">
            <h3>📊 Progress</h3>
            <div class="progress-circle">{progress}%</div>
            <p>{completed} of {total} lessons completed</p>
        </div>
        """.format(
            progress=st.session_state.progress['overall_progress'],
            completed=sum(1 for p in st.session_state.progress['pages'].values() if p['completed']),
            total=st.session_state.progress['total_pages']
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="dashboard-card">
            <h3>🏆 Achievements</h3>
            <div class="achievement-count">{unlocked}</div>
            <p>Achievements unlocked</p>
        </div>
        """.format(
            unlocked=sum(1 for unlocked in st.session_state.achievements.values() if unlocked)
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="dashboard-card">
            <h3>📚 Current Focus</h3>
            <div class="current-focus">Next Lesson</div>
            <p>Continue your journey</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Learning path
    st.markdown("### 🛤️ Learning Path")
    
    learning_modules = [
        {"id": "getting-started", "title": "Getting Started", "description": "Set up your GitHub account and learn the basics", "icon": "📖"},
        {"id": "concepts", "title": "Core Concepts", "description": "Master repository, commits, branches, and pull requests", "icon": "🎯"},
        {"id": "first-repo", "title": "First Repository", "description": "Create your first repository with the Hello World tutorial", "icon": "💻"},
        {"id": "command-line", "title": "Command Line", "description": "Learn Git commands and local to remote workflows", "icon": "⌨️"},
        {"id": "collaboration", "title": "Collaboration", "description": "Work with others using branches and pull requests", "icon": "🤝"},
        {"id": "best-practices", "title": "Best Practices", "description": "Learn professional development workflows", "icon": "⭐"},
    ]
    
    cols = st.columns(3)
    for i, module in enumerate(learning_modules):
        with cols[i % 3]:
            status = st.session_state.progress['pages'].get(module['id'], {}).get('completed', False)
            is_visited = st.session_state.progress['pages'].get(module['id'], {}).get('last_visited', False)
            
            if status:
                status_text = "✅ Completed"
                card_class = "module-card completed"
            elif is_visited:
                status_text = "🔄 In Progress"
                card_class = "module-card in-progress"
            else:
                status_text = "⭕ Not Started"
                card_class = "module-card not-started"
            
            st.markdown(f"""
            <div class="{card_class}">
                <div class="module-icon">{module['icon']}</div>
                <h4>{module['title']}</h4>
                <p>{module['description']}</p>
                <div class="module-status">{status_text}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Start {module['title']}", key=f"start_{module['id']}", use_container_width=True):
                st.session_state.current_page = module['id']
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_getting_started_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>📖 Getting Started</h1>
        <p class="page-description">Set up your GitHub account and learn the basics of version control</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## What is GitHub? 🤔

GitHub is like a **digital locker** for your code projects. Just like how you might use Google Drive or iCloud to store your photos and documents, GitHub helps programmers store, track, and share their code.

### Why Should You Care? 💡

- **Show off your projects**: Create a portfolio of your work
- **Work with others**: Collaborate on team projects
- **Learn from others**: Explore millions of open source projects
- **Save your work**: Never lose your code again!
- **Real-world skills**: Professional developers use GitHub daily
    """)
    
    st.markdown("## Setup Checklist ✅")
    
    checklist_items = [
        "Create a GitHub account at github.com",
        "Verify your email address",
        "Download and install Git on your computer",
        "Connect Git to your GitHub account",
        "Set up your profile with a profile picture"
    ]
    
    for i, item in enumerate(checklist_items, 1):
        col1, col2 = st.columns([1, 5])
        with col1:
            st.write(f"{i}.")
        with col2:
            st.write(item)
    
    if st.button("✅ Mark Getting Started Complete"):
        mark_page_completed("getting-started")
        st.success("Great job! You've completed the Getting Started section.")
        st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_core_concepts_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>🎯 Core Concepts</h1>
        <p class="page-description">Master the fundamental concepts of GitHub and version control</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Repository (Repo) 📁

A **repository** is like a project folder that contains all your files and the history of changes made to those files.

<div class="explanation-text">
<strong>Think of it like:</strong>
- A **Google Drive folder** for your code
- A **game save file** that remembers your progress
- A **time machine** for your project
</div>

### What Makes a Repo Special?

- **Version History**: See every change ever made
- **Branches**: Create different versions of your project
- **Collaborative**: Multiple people can work on the same project
    """)
    
    st.markdown("""
    ## Commits 💾

A **commit** is like a **save point** in a video game. It records exactly what your project looks like at that moment.

<div class="explanation-text">
<strong>Each commit includes:</strong>
- A **snapshot** of all your files
- A **message** describing what changed
- A **timestamp** of when it was saved
- A **unique ID** to find it later
</div>
    """)
    
    st.markdown("""
    ## Branches 🌳

A **branch** is like a **parallel universe** for your project. You can make changes without affecting the main version.

**Why use branches?**
- **Experiment** with new features safely
- **Work on different features** at the same time
- **Prepare for collaboration** with others
- **Test ideas** before merging them
    """)
    
    st.markdown("""
    ## Pull Requests (PRs) 🔄

A **pull request** is like asking for permission to merge your changes. It's a way to:
- **Review changes** before they're merged
- **Discuss modifications** with your team
- **Ensure quality** before combining code
- **Document decisions** about the project
    """)
    
    if st.button("✅ Mark Core Concepts Complete"):
        mark_page_completed("concepts")
        st.success("Excellent! You understand the core concepts of GitHub.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_first_repository_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>💻 First Repository</h1>
        <p class="page-description">Create your first repository with the classic "Hello World" tutorial</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Creating Your Hello World Repository 🚀

Follow these steps to create your very first repository on GitHub!
    """)
    
    st.markdown("""
    ### Step 1: Create a New Repository

1. **Sign in** to your GitHub account
2. **Click the green "New" button** (or the "+" icon in the top right)
3. **Repository name**: Type `hello-world`
4. **Description**: "My first repository on GitHub"
5. **Public or Private**: Choose public (so others can see it)
6. **Check "Add a README file"**
7. **Click "Create repository"** 🎉
    """)
    
    st.markdown("""
    ### Step 2: Understanding Your Repository

Your new repository contains:
- **README.md**: A file that describes your project
- **.gitignore**: Tells Git which files to ignore
- **Files**: Any code or documents you upload
    """)
    
    st.markdown("""
    ### Step 3: Edit Your README

1. **Click the pencil icon** (✏️) to edit the README file
2. **Add a description** about yourself or your project
3. **Click "Commit changes"** to save your edits
    """)
    
    # Interactive code block simulation
    st.markdown("### 📝 Your First README Content:")
    
    readme_content = """# Hello, World! 👋

I'm [Your Name] and this is my first GitHub repository!

## About Me
- I'm learning to use GitHub
- I like [your interests]
- I'm excited to build cool projects

## What I'm Learning
- GitHub basics
- Version control
- Collaboration

---

*This README was created as part of my GitHub learning journey.*
"""
    
    st.code(readme_content, language='markdown')
    
    if st.button("✅ Mark First Repository Complete"):
        mark_page_completed("first-repo")
        st.success("Fantastic! You've created your first repository!")
        st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_command_line_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>⌨️ Command Line</h1>
        <p class="page-description">Learn Git commands and workflows from local to remote</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## The Command Line Interface 🖥️

The command line (also called **Terminal** or **Command Prompt**) is a text-based way to interact with your computer. Think of it as **talking directly to your computer** instead of clicking buttons.

<div class="explanation-text">
<strong>Why learn the command line?</strong>
- **Faster workflows**: Complete tasks quickly
- **Professional skills**: Developers use CLI daily
- **More control**: Access advanced features
- **Automation**: Script repetitive tasks
</div>
    """)
    
    st.markdown("""
    ## Essential Git Commands 🚀
    """)
    
    commands = [
        {
            "command": "git init",
            "description": "Initialize a new Git repository in your project folder",
            "analogy": "Like turning on a recorder before starting a video"
        },
        {
            "command": "git add .",
            "description": "Stage all changes for commit",
            "analogy": "Like selecting all the photos you want to upload"
        },
        {
            "command": "git commit -m 'message'",
            "description": "Save your changes with a descriptive message",
            "analogy": "Like taking a photo with a caption"
        },
        {
            "command": "git push",
            "description": "Upload your commits to GitHub",
            "analogy": "Like uploading your photos to the cloud"
        },
        {
            "command": "git pull",
            "description": "Download the latest changes from GitHub",
            "analogy": "Like syncing your phone with the cloud"
        }
    ]
    
    for cmd in commands:
        st.markdown(f"""
        ### {cmd['command']}
        <div class="command-description">
        <strong>What it does:</strong> {cmd['description']}
        </div>
        
        <div class="command-analogy">
        <strong>Think of it like:</strong> {cmd['analogy']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Typical Workflow 📋
    """)
    
    workflow_steps = """# 1. Create or open your project
mkdir my-project
cd my-project

# 2. Initialize Git (one time only)
git init

# 3. Make changes to your files
# (edit files in your code editor)

# 4. Check what changed
git status

# 5. Stage your changes
git add .

# 6. Commit your changes
git commit -m "Add new feature"

# 7. Push to GitHub
git push origin main
"""
    
    st.code(workflow_steps, language='bash')
    
    if st.button("✅ Mark Command Line Complete"):
        mark_page_completed("command-line")
        st.success("Great work! You're getting comfortable with Git commands.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_collaboration_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>🤝 Collaboration</h1>
        <p class="page-description">Learn to work with others using branches and pull requests</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Why Collaborate on GitHub? 💡

GitHub makes it easy for multiple people to work on the same project. It's like having a **shared workspace** where everyone can contribute their ideas.
    """)
    
    st.markdown("""
    ## The Branching Strategy 🌳

### Main Branch (main)
- **Stable code** that's ready to use
- **Protected** from direct changes
- **Source of truth** for the project

### Feature Branches
- **Experiment safely** without breaking the main code
- **Develop new features** independently
- **Easy to track** who is working on what
    """)
    
    st.markdown("""
    ## Pull Request Process 🔄

### 1. Create a Feature Branch
```bash
git checkout -b feature/new-feature
```

### 2. Make Your Changes
- Edit files
- Add new features
- Fix bugs
- Write tests

### 3. Commit and Push
```bash
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

### 4. Open a Pull Request
- **Navigate** to your repository on GitHub
- **Click** "Pull requests" → "New pull request"
- **Compare** your branch with main
- **Write** a clear description
- **Request reviews** from team members

### 5. Code Review Process
- **Team members** review your code
- **Discuss changes** in comments
- **Make modifications** if needed
- **Approve** when ready to merge

### 6. Merge Your Changes
- **Click "Merge pull request"**
- **Delete** the feature branch
- **Celebrate** your contribution! 🎉
    """)
    
    st.markdown("""
    ## Best Practices for Collaboration ✨

- **Write clear commit messages**
- **Keep branches small and focused**
- **Test your code** before creating a PR
- **Be respectful** in code reviews
- **Ask for help** when you're stuck
    """)
    
    if st.button("✅ Mark Collaboration Complete"):
        mark_page_completed("collaboration")
        st.success("Excellent! You're ready to collaborate with others.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_best_practices_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>⭐ Best Practices</h1>
        <p class="page-description">Learn professional development workflows and common mistakes to avoid</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Writing Great Commit Messages 📝

### Good Commit Message Structure:
```
type: Brief description (50 chars max)

Longer explanation if needed. Explain what and why, not how.
Break lines at 72 characters.

Fixes #123
```

### Types of Commits:
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Formatting changes
- **refactor**: Code restructuring
- **test**: Adding tests
- **chore**: Maintenance tasks
    """)
    
    # Interactive example
    st.markdown("### ✨ Good Examples:")
    
    good_examples = [
        "feat: Add user authentication system",
        "fix: Resolve login button alignment issue",
        "docs: Update README with setup instructions",
        "refactor: Simplify database connection logic",
        "test: Add unit tests for user model"
    ]
    
    for example in good_examples:
        st.success(f"✅ {example}")
    
    st.markdown("### ❌ Bad Examples:")
    
    bad_examples = [
        "fixed stuff",
        "update",
        "changes",
        "wip",
        "asdf"
    ]
    
    for example in bad_examples:
        st.error(f"❌ {example}")
    
    st.markdown("""
    ## The .gitignore File 🚫

A `.gitignore` file tells Git which files to **ignore**. This includes:
- **Sensitive data** (passwords, API keys)
- **Temporary files** (`.tmp`, `.log`)
- **Build files** (compiled code, dependencies)
- **IDE files** (project settings)
- **OS files** (`.DS_Store`, `Thumbs.db`)
    """)
    
    st.markdown("### Common .gitignore entries:")
    
    gitignore_content = """# Dependencies
node_modules/
vendor/
__pycache__/

# Build outputs
dist/
build/
*.exe

# Environment variables
.env
.env.local

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
logs/
"""
    
    st.code(gitignore_content, language='gitignore')
    
    st.markdown("""
    ## Common Mistakes to Avoid ⚠️

### 1. Committing Large Files
- **Problem**: Storing large files in Git
- **Solution**: Use Git LFS or external storage

### 2. Committing Secrets
- **Problem**: Accidentally sharing passwords or API keys
- **Solution**: Use `.gitignore` and environment variables

### 3. Committing to Main Branch
- **Problem**: Directly changing the main codebase
- **Solution**: Always use feature branches and pull requests

### 4. Not Writing Commit Messages
- **Problem**: Unclear history
- **Solution**: Write descriptive, meaningful messages

### 5. Not Testing Before Committing
- **Problem**: Breaking the build
- **Solution**: Always test your changes locally
    """)
    
    if st.button("✅ Mark Best Practices Complete"):
        mark_page_completed("best-practices")
        st.success("Perfect! You're following professional development practices.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_real_projects_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>🚀 Real Projects</h1>
        <p class="page-description">Apply your skills with these teen-friendly project ideas</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Project Ideas for Your Portfolio 💼

Now that you know the basics, let's put your skills to work! Here are some project ideas that are perfect for your skill level and interests.
    """)
    
    projects = [
        {
            "title": "Personal Portfolio Website",
            "difficulty": "Beginner",
            "description": "Create a website showcasing your projects, skills, and resume",
            "skills": ["HTML", "CSS", "JavaScript"],
            "why_cool": "Showcase your work to colleges and employers"
        },
        {
            "title": "Study Planner App",
            "difficulty": "Intermediate",
            "description": "Build an app to track assignments, grades, and study schedules",
            "skills": ["React", "JavaScript", "APIs"],
            "why_cool": "Solve a real problem you have every day"
        },
        {
            "title": "Game Review Database",
            "difficulty": "Beginner",
            "description": "Create a database of your favorite games with reviews and ratings",
            "skills": ["Database", "API", "CRUD"],
            "why_cool": "Combine gaming with coding"
        },
        {
            "title": "School Event Tracker",
            "difficulty": "Intermediate",
            "description": "Track school events, clubs, and activities with notifications",
            "skills": ["Mobile", "Backend", "Database"],
            "why_cool": "Help your school community stay organized"
        },
        {
            "title": "Music Playlist Analyzer",
            "difficulty": "Advanced",
            "description": "Analyze your Spotify playlists and create visualizations",
            "skills": ["Python", "Data Analysis", "APIs"],
            "why_cool": "Discover patterns in your music taste"
        },
        {
            "title": "Virtual Study Group Platform",
            "difficulty": "Advanced",
            "description": "Create a platform for students to form virtual study groups",
            "skills": ["WebRTC", "Real-time", "Authentication"],
            "why_cool": "Help students connect during remote learning"
        }
    ]
    
    for project in projects:
        difficulty_color = {
            "Beginner": "🟢",
            "Intermediate": "🟡",
            "Advanced": "🔴"
        }[project["difficulty"]]
        
        st.markdown(f"""
        ### {difficulty_color} {project['title']} ({project['difficulty']})

**What it is:** {project['description']}

**What you'll learn:** {', '.join(project['skills'])}

**Why it's awesome:** {project['why_cool']}
        """)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"💡 Get Started with {project['title']}", key=f"project_{project['title']}"):
                st.info("This feature is coming soon! Check back later.")
        with col2:
            if st.button(f"📖 View Example", key=f"example_{project['title']}"):
                st.info("Example projects coming soon!")
        
        st.markdown("---")
    
    st.markdown("""
    ## Project Planning Tips 📋

### 1. Start Small
- Break big projects into smaller tasks
- Complete one feature at a time
- Don't try to build everything at once

### 2. Document Your Process
- Write clear README files
- Add comments to your code
- Create tutorials for others

### 3. Get Feedback
- Share your projects with friends
- Ask for code reviews
- Join GitHub communities

### 4. Keep Learning
- Explore new technologies
- Read other people's code
- Take online courses
    """)
    
    if st.button("✅ Mark Real Projects Complete"):
        mark_page_completed("real-projects")
        st.success("Awesome! You're ready to build real projects!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_practice_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>📝 Practice Quiz</h1>
        <p class="page-description">Test your knowledge with interactive quizzes</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quiz sections
    quiz_sections = {
        "core_concepts": {
            "title": "Core Concepts",
            "questions": [
                {
                    "question": "What is a repository in GitHub?",
                    "options": [
                        "A folder that contains your project and its history",
                        "A type of file format",
                        "A programming language",
                        "A website hosting service"
                    ],
                    "correct": 0,
                    "explanation": "A repository (or 'repo') is like a project folder that contains all your files and the complete history of changes made to those files."
                },
                {
                    "question": "What is a commit?",
                    "options": [
                        "A type of backup",
                        "A save point that records changes",
                        "A file sharing method",
                        "A code error"
                    ],
                    "correct": 1,
                    "explanation": "A commit is like a save point in a video game - it records exactly what your project looks like at that moment, with a message describing what changed."
                },
                {
                    "question": "Why would you use a branch?",
                    "options": [
                        "To make copies of your computer",
                        "To experiment with new features safely",
                        "To store passwords",
                        "To make your code run faster"
                    ],
                    "correct": 1,
                    "explanation": "Branches let you create parallel versions of your project where you can experiment with new features without affecting the main codebase."
                }
            ]
        },
        "workflow": {
            "title": "Hello World Workflow",
            "questions": [
                {
                    "question": "What should you do first when starting a new project locally?",
                    "options": [
                        "Write code immediately",
                        "Initialize a Git repository",
                        "Create files",
                        "Ask for permission"
                    ],
                    "correct": 1,
                    "explanation": "You should initialize a Git repository first using 'git init' to start tracking your project changes."
                },
                {
                    "question": "What does 'git add .' do?",
                    "options": [
                        "Adds all files to the project",
                        "Stages all changes for commit",
                        "Uploads to GitHub",
                        "Creates a backup"
                    ],
                    "correct": 1,
                    "explanation": "git add . stages all your current changes, preparing them to be committed. It's like selecting all the photos you want to upload."
                },
                {
                    "question": "What is a pull request?",
                    "options": [
                        "A request to download code",
                        "A way to propose and discuss changes",
                        "An error message",
                        "A backup process"
                    ],
                    "correct": 1,
                    "explanation": "A pull request is a way to propose your changes, get them reviewed by others, and discuss modifications before merging them into the main codebase."
                }
            ]
        },
        "command_line": {
            "title": "Command Line",
            "questions": [
                {
                    "question": "What does 'git init' do?",
                    "options": [
                        "Downloads a repository",
                        "Initializes a new Git repository",
                        "Uploads code to GitHub",
                        "Deletes a project"
                    ],
                    "correct": 1,
                    "explanation": "git init initializes a new Git repository in your current directory, setting up the necessary files to start tracking changes."
                },
                {
                    "question": "What does 'git push' do?",
                    "options": [
                        "Uploads commits to GitHub",
                        "Downloads from GitHub",
                        "Creates a new branch",
                        "Deletes files"
                    ],
                    "correct": 0,
                    "explanation": "git push uploads your local commits to a remote repository like GitHub, making your changes available to others."
                },
                {
                    "question": "What does 'git pull' do?",
                    "options": [
                        "Downloads the latest changes",
                        "Uploads your changes",
                        "Creates a backup",
                        "Deletes files"
                    ],
                    "correct": 0,
                    "explanation": "git pull downloads the latest changes from the remote repository and merges them into your local branch."
                },
                {
                    "question": "What is the purpose of commit messages?",
                    "options": [
                        "To confuse other developers",
                        "To document what changed and why",
                        "To make the code prettier",
                        "To increase file size"
                    ],
                    "correct": 1,
                    "explanation": "Commit messages help you and others understand what changed and why, making it easier to track project history and debug issues."
                }
            ]
        },
        "collaboration": {
            "title": "Collaboration",
            "questions": [
                {
                    "question": "What is the main branch typically called?",
                    "options": [
                        "master",
                        "main",
                        "production",
                        "primary"
                    ],
                    "correct": 1,
                    "explanation": "The main branch is typically called 'main' in modern Git repositories. It represents the stable, production-ready code."
                },
                {
                    "question": "When should you create a pull request?",
                    "options": [
                        "After committing changes locally",
                        "After testing your changes and before merging",
                        "Never, it's optional",
                        "Only for large projects"
                    ],
                    "correct": 1,
                    "explanation": "You should create a pull request after testing your changes and before merging them, to allow for code review and discussion."
                },
                {
                    "question": "What is code review?",
                    "options": [
                        "Checking code for errors and discussing improvements",
                        "Reading code for fun",
                        "Deleting code",
                        "Writing documentation"
                    ],
                    "correct": 0,
                    "explanation": "Code review is the process of examining code changes to find bugs, suggest improvements, and ensure code quality before merging."
                }
            ]
        },
        "best_practices": {
            "title": "Best Practices",
            "questions": [
                {
                    "question": "What should you include in .gitignore?",
                    "options": [
                        "All your project files",
                        "Sensitive data and temporary files",
                        "Only code files",
                        "Nothing, it's not important"
                    ],
                    "correct": 1,
                    "explanation": ".gitignore should include sensitive data (passwords, API keys), temporary files, and build artifacts that shouldn't be tracked in version control."
                },
                {
                    "question": "What makes a good commit message?",
                    "options": [
                        "Long and detailed",
                        "Clear, concise, and descriptive",
                        "Single words like 'update' or 'fix'",
                        "Emojis only"
                    ],
                    "correct": 1,
                    "explanation": "Good commit messages are clear, concise, and describe what changed and why. They help maintain a readable project history."
                },
                {
                    "question": "Why should you use feature branches?",
                    "options": [
                        "To confuse other developers",
                        "To work on features independently and safely",
                        "To make the repository larger",
                        "To avoid using Git"
                    ],
                    "correct": 1,
                    "explanation": "Feature branches allow you to work on new features independently without affecting the main codebase, making collaboration safer and more organized."
                }
            ]
        }
    }
    
    # Section selector
    sections = list(quiz_sections.keys())
    section_titles = [quiz_sections[section]["title"] for section in sections]
    
    selected_section = st.selectbox("Select a quiz section:", section_titles)
    section_key = sections[section_titles.index(selected_section)]
    
    # Initialize quiz state
    if 'current_quiz_section' not in st.session_state:
        st.session_state.current_quiz_section = section_key
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.show_feedback = False
        st.session_state.quiz_completed = False
    
    # Reset if section changed
    if st.session_state.current_quiz_section != section_key:
        st.session_state.current_quiz_section = section_key
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.show_feedback = False
        st.session_state.quiz_completed = False
    
    quiz_data = quiz_sections[section_key]
    current_q = st.session_state.current_question
    total_q = len(quiz_data["questions"])
    
    if current_q < total_q and not st.session_state.quiz_completed:
        question_data = quiz_data["questions"][current_q]
        
        st.markdown(f"### Question {current_q + 1} of {total_q}")
        st.progress((current_q) / total_q)
        
        st.markdown(f"**{question_data['question']}**")
        
        selected_answer = st.radio(
            "Select your answer:",
            question_data["options"],
            key=f"q_{current_q}"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Submit Answer", disabled=selected_answer is None):
                if selected_answer is not None:
                    st.session_state.answers[current_q] = question_data["options"].index(selected_answer)
                    st.session_state.show_feedback = True
                    st.rerun()
        
        with col2:
            if st.button("Skip Question"):
                st.session_state.current_question += 1
                st.session_state.show_feedback = False
                st.rerun()
        
        # Show feedback
        if st.session_state.show_feedback and current_q in st.session_state.answers:
            is_correct = st.session_state.answers[current_q] == question_data["correct"]
            
            if is_correct:
                st.success("✅ Correct!")
            else:
                st.error("❌ Incorrect")
            
            st.info(f"**Explanation:** {question_data['explanation']}")
            
            if st.button("Next Question"):
                st.session_state.current_question += 1
                st.session_state.show_feedback = False
                st.rerun()
    
    else:
        # Show results
        st.markdown("### Quiz Results 🎉")
        
        correct_answers = sum(
            1 for i, answer in st.session_state.answers.items()
            if answer == quiz_data["questions"][i]["correct"]
        )
        
        score_percentage = int((correct_answers / total_q) * 100)
        
        st.markdown(f"**Score: {correct_answers}/{total_q} ({score_percentage}%)**")
        
        if score_percentage >= 90:
            st.balloons()
            st.success("🏆 Excellent work!")
        elif score_percentage >= 70:
            st.success("👍 Good job!")
        else:
            st.info("💪 Keep learning!")
        
        # Show detailed results
        st.markdown("### Detailed Results")
        for i, question_data in enumerate(quiz_data["questions"]):
            user_answer = st.session_state.answers.get(i)
            is_correct = user_answer == question_data["correct"]
            
            status = "✅" if is_correct else "❌"
            st.markdown(f"{status} **Q{i+1}:** {question_data['question']}")
            
            if user_answer is not None:
                st.markdown(f"   Your answer: {question_data['options'][user_answer]}")
                if not is_correct:
                    st.markdown(f"   Correct answer: {question_data['options'][question_data['correct']]}")
        
        # Save score
        record_quiz_score(section_key, correct_answers, total_q)
        
        # Retake quiz
        if st.button("🔄 Retake Quiz"):
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.show_feedback = False
            st.session_state.quiz_completed = False
            st.rerun()
    
    if st.button("✅ Mark Practice Complete"):
        mark_page_completed("practice")
        st.success("Great job on completing the practice section!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_resources_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>📚 Resources</h1>
        <p class="page-description">External tools and references to continue your GitHub journey</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Official GitHub Resources 🔗

### GitHub Skills
- **Learn GitHub**: Interactive tutorials right on GitHub
- **URL**: skills.github.com
- **What you'll learn**: Real GitHub workflows through hands-on exercises

### GitHub Documentation
- **Pro Git Book**: Free online book about Git
- **GitHub Guides**: Step-by-step tutorials
- **GitHub Learning Lab**: Interactive learning experience
    """)
    
    st.markdown("""
    ## Interactive Learning Tools 🎮

### Learn Git Branching
- **Visual Git**: See how Git commands affect the repository
- **URL**: learngitbranching.js.org
- **Great for**: Understanding branching and merging

### GitHub Desktop
- **Visual Interface**: Use Git without command line
- **Free**: Available for Windows, Mac, Linux
- **Perfect for**: Beginners who want GUI

### Visual Studio Code with Git
- **Integrated**: Built-in Git support
- **Extensions**: GitLens for advanced features
- **Recommended**: If you like coding in VS Code
    """)
    
    st.markdown("""
    ## Practice Platforms 💪

### Hacktoberfest
- **Annual Event**: October, celebrate open source
- **Free T-Shirt**: Complete 4 pull requests
- **Great for**: Real-world collaboration practice

### First Timers Only
- **Beginner-Friendly**: Issues labeled for newcomers
- **URL**: firsttimersonly.com
- **Perfect for**: First open source contribution

### Up for Grabs
- **Beginner Issues**: Projects looking for help
- **URL**: up-for-grabs.net
- **Variety**: Many different technologies
    """)
    
    st.markdown("""
    ## YouTube Channels 📺

### GitHub Training & Guides
- **Official Channel**: GitHub's official tutorials
- **Content**: Feature announcements, deep dives

### The Net Ninja
- **Git Tutorial Series**: Comprehensive Git course
- **Beginner Friendly**: Starts from absolute basics

### Traversy Media
- **Practical Projects**: Real-world Git workflows
- **Intermediate**: For those ready to build projects
    """)
    
    st.markdown("""
    ## Books and Reading 📖

### "Pro Git" (Free Online)
- **Comprehensive**: Everything about Git
- **Free**: Available at git-scm.com/book
- **Advanced**: For serious learners

### "Learn Enough Git to Be Dangerous"
- **Practical**: Focus on essential commands
- **Beginner**: Great starting point
    """)
    
    st.markdown("""
    ## Communities and Support 🤝

### Stack Overflow
- **Questions**: Get help with specific problems
- **Search**: Find answers to common issues
- **Community**: Experienced developers helping beginners

### Reddit
- **r/github**: GitHub-specific discussions
- **r/git**: Git version control discussions
- **r/learnprogramming**: General programming help

### Discord Servers
- **GitHub Community**: Official Discord server
- **Programming Communities**: Find beginner-friendly servers
    """)
    
    st.markdown("""
    ## Next Steps 🚀

### 1. Keep Practicing
- Create personal projects
- Contribute to open source
- Help friends with their repositories

### 2. Explore Advanced Topics
- GitHub Actions (automation)
- GitHub Pages (hosting websites)
- Security features (code scanning, dependency tracking)

### 3. Join the Community
- Follow GitHub on social media
- Attend local meetups
- Share your learning journey
    """)
    
    if st.button("✅ Mark Resources Complete"):
        mark_page_completed("resources")
        st.success("Great! You have all the resources you need to continue learning.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_quick_reference_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-header">
        <h1>⚡ Quick Reference</h1>
        <p class="page-description">Command cheat sheet and concept summary</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Essential Git Commands 🚀
    """)
    
    # Create a table of Git commands
    commands_data = [
        ["git init", "Initialize a new repository"],
        ["git clone <url>", "Copy a repository from GitHub"],
        ["git status", "Check what files have changed"],
        ["git add .", "Stage all changes for commit"],
        ["git commit -m 'message'", "Save changes with a message"],
        ["git push", "Upload commits to GitHub"],
        ["git pull", "Download latest changes from GitHub"],
        ["git branch", "List all branches"],
        ["git checkout -b <name>", "Create and switch to new branch"],
        ["git merge <branch>", "Merge a branch into current branch"],
        ["git log", "View commit history"],
        ["git diff", "See differences between versions"]
    ]
    
    # Display as a nice table
    for cmd, desc in commands_data:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.code(cmd)
        with col2:
            st.write(desc)
    
    st.markdown("---")
    
    st.markdown("""
    ## Concept Quick Reference 📋
    """)
    
    concepts = {
        "Repository": "A project folder with version history",
        "Commit": "A save point that records changes",
        "Branch": "A parallel version of your project",
        "Pull Request": "A request to merge your changes",
        "Merge": "Combining changes from different branches",
        "Clone": "Copying a repository to your computer",
        "Fork": "Your own copy of someone else's repository",
        "Remote": "A version of your repository hosted on GitHub",
        "Origin": "The default name for the remote repository",
        "Main/Master": "The primary branch of your project"
    }
    
    for term, definition in concepts.items():
        st.markdown(f"**{term}**: {definition}")
    
    st.markdown("---")
    
    st.markdown("""
    ## Workflow Cheat Sheet 📝

### Starting a New Project
```bash
# 1. Create project folder
mkdir my-project
cd my-project

# 2. Initialize Git
git init

# 3. Create files and make changes
# (edit your files)

# 4. Stage and commit
git add .
git commit -m "Initial commit"

# 5. Create repository on GitHub
# (do this on GitHub.com)

# 6. Connect and push
git remote add origin <your-repo-url>
git push -u origin main
```
    """)
    
    st.markdown("""
### Working on an Existing Project
```bash
# 1. Clone the repository
git clone <repository-url>

# 2. Create a feature branch
git checkout -b feature/new-feature

# 3. Make your changes
# (edit files)

# 4. Stage and commit
git add .
git commit -m "Add new feature"

# 5. Push to GitHub
git push origin feature/new-feature

# 6. Create pull request on GitHub
# (do this on GitHub.com)
```
    """)
    
    st.markdown("""
    ## GitHub Actions (Bonus) ⚡

### Create a Simple Workflow
1. **Create** `.github/workflows/` folder
2. **Add** a YAML file (e.g., `build.yml`)
3. **Define** your workflow
4. **Commit and push** to see it in action!

### Example Workflow
```yaml
name: Build and Test
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run tests
      run: npm test
```
    """)
    
    if st.button("✅ Mark Quick Reference Complete"):
        mark_page_completed("quick-reference")
        st.success("Perfect! You have a handy reference for Git and GitHub.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main application
def main():
    load_css()
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Get current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    
    # Mark current page as visited
    current_page = st.session_state.current_page
    mark_page_visited(current_page)
    
    # Render current page
    if current_page == 'home':
        render_home_page()
    elif current_page == 'getting-started':
        render_getting_started_page()
    elif current_page == 'concepts':
        render_core_concepts_page()
    elif current_page == 'first-repo':
        render_first_repository_page()
    elif current_page == 'command-line':
        render_command_line_page()
    elif current_page == 'collaboration':
        render_collaboration_page()
    elif current_page == 'best-practices':
        render_best_practices_page()
    elif current_page == 'real-projects':
        render_real_projects_page()
    elif current_page == 'practice':
        render_practice_page()
    elif current_page == 'resources':
        render_resources_page()
    elif current_page == 'quick-reference':
        render_quick_reference_page()

if __name__ == "__main__":
    main()
