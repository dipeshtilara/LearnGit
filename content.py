"""
GitHub Tutorial Educational Content - Streamlit Version
Complete migration from React with all 11 tutorial pages
Designed for 9th grade students with age-appropriate analogies
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Tuple
import time

# Page configuration
st.set_page_config(
    page_title="GitHub Tutorial - Interactive Learning",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        border: 1px solid #e0e0e0;
        padding: 5%;
        border-radius: 10px;
        border-left: 0.5rem solid #4e79a7;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    .step-container {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .concept-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state for progress tracking"""
    if 'completed_pages' not in st.session_state:
        st.session_state.completed_pages = set()
    if 'quiz_scores' not in st.session_state:
        st.session_state.quiz_scores = {}
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'
    if 'setup_steps' not in st.session_state:
        st.session_state.setup_steps = {
            'install_git': False,
            'create_account': False,
            'configure_name': False,
            'configure_email': False,
            'verify_config': False
        }

def display_header(title: str, subtitle: str, emoji: str = "🎓"):
    """Display consistent page headers"""
    st.markdown(f"""
    <div style='text-align: center; background: linear-gradient(90deg, #4e79a7 0%, #f28e2b 100%); 
                color: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h1 style='margin: 0; font-size: 2.5rem;'>{emoji} {title}</h1>
        <p style='margin: 1rem 0; font-size: 1.2rem; opacity: 0.9;'>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def display_progress_dashboard():
    """Display learning progress dashboard"""
    total_pages = 11
    completed_count = len(st.session_state.completed_pages)
    progress_percentage = (completed_count / total_pages) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Your Progress",
            f"{progress_percentage:.0f}%",
            f"{completed_count} of {total_pages} lessons completed"
        )
    
    with col2:
        quiz_completed = len(st.session_state.quiz_scores)
        st.metric(
            "Quiz Scores",
            f"{quiz_completed}",
            "sections completed"
        )
    
    with col3:
        recent_activity = "Active today" if progress_percentage > 0 else "Not started"
        st.metric(
            "Current Status",
            recent_activity,
            "Keep learning!"
        )

def home_page():
    """Home page with learning path and overview"""
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 3rem; border-radius: 15px; margin-bottom: 2rem; text-align: center;'>
        <h1 style='font-size: 3rem; margin-bottom: 1rem;'>Master GitHub with Interactive Learning</h1>
        <p style='font-size: 1.3rem; line-height: 1.6; margin-bottom: 2rem;'>
            Learn version control and collaboration the fun way. Build real projects, 
            earn achievements, and become a confident programmer through hands-on tutorials 
            designed for 9th graders.
        </p>
        <div style='display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;'>
            <a href='#getting-started' style='background: #28a745; color: white; padding: 0.8rem 1.5rem; 
               border-radius: 8px; text-decoration: none; font-weight: bold;'>🚀 Start Learning</a>
            <a href='#quick-reference' style='background: transparent; color: white; padding: 0.8rem 1.5rem; 
               border: 2px solid white; border-radius: 8px; text-decoration: none; font-weight: bold;'>📚 Quick Reference</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    display_progress_dashboard()
    
    st.markdown("## Your Learning Journey")
    st.markdown("Follow our structured path from complete beginner to confident GitHub user. Each lesson builds on the previous one, with hands-on practice and real-world examples.")
    
    # Learning modules with descriptions
    modules = [
        {
            "id": "getting-started",
            "title": "1. Getting Started",
            "description": "Set up your GitHub account and learn the basics",
            "icon": "⚙️",
            "status": "✅ Completed" if "Getting Started" in st.session_state.completed_pages else "📝 In Progress"
        },
        {
            "id": "core-concepts",
            "title": "2. Core Concepts", 
            "description": "Master repository, commits, branches, and pull requests",
            "icon": "🧠",
            "status": "✅ Completed" if "Core Concepts" in st.session_state.completed_pages else "📝 In Progress"
        },
        {
            "id": "first-repository",
            "title": "3. First Repository",
            "description": "Create your first repository with the Hello World tutorial",
            "icon": "🏗️",
            "status": "✅ Completed" if "First Repository" in st.session_state.completed_pages else "📝 In Progress"
        },
        {
            "id": "command-line",
            "title": "4. Command Line",
            "description": "Learn Git commands and local to remote workflows",
            "icon": "⌨️",
            "status": "✅ Completed" if "Command Line" in st.session_state.completed_pages else "📝 In Progress"
        },
        {
            "id": "collaboration",
            "title": "5. Collaboration",
            "description": "Master branches, pull requests, and code review",
            "icon": "👥",
            "status": "✅ Completed" if "Collaboration" in st.session_state.completed_pages else "📝 In Progress"
        },
        {
            "id": "best-practices",
            "title": "6. Best Practices",
            "description": "Learn common mistakes to avoid and professional habits",
            "icon": "⭐",
            "status": "✅ Completed" if "Best Practices" in st.session_state.completed_pages else "📝 In Progress"
        }
    ]
    
    for module in modules:
        with st.container():
            st.markdown(f"""
            <div class='step-container'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;'>
                    <div style='font-size: 2rem;'>{module['icon']}</div>
                    <div style='flex: 1;'>
                        <h3 style='margin: 0; color: #2c3e50;'>{module['title']}</h3>
                        <p style='margin: 0.5rem 0; color: #7f8c8d;'>{module['description']}</p>
                    </div>
                    <div style='font-size: 0.9rem; color: #27ae60; font-weight: bold;'>{module['status']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Quick actions
    st.markdown("## Ready to Dive Deeper?")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎯 Take Practice Quiz", use_container_width=True):
            st.session_state.current_page = "Practice"
            st.rerun()
    
    with col2:
        if st.button("📖 Quick Reference", use_container_width=True):
            st.session_state.current_page = "Quick Reference"
            st.rerun()

def getting_started_page():
    """Getting Started - Setup and configuration"""
    display_header("Getting Started", "Set up your GitHub account and configure Git in under 10 minutes", "🚀")
    
    # Why Git + GitHub section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='info-box'>
            <h3>Why Git + GitHub?</h3>
            <p><strong>Git (Your Computer):</strong> Tracks changes on your computer, keeps a history, lets you branch to try ideas safely.</p>
            <p><strong>GitHub (Online):</strong> Hosts your repository online, makes collaboration easier, enables review via pull requests.</p>
            <p><strong>Key Point:</strong> You can use Git without GitHub, and you can use GitHub with Git—together they are a powerful team.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Quick Setup (10 minutes)")
        st.markdown("""
        1. **Install Git** (5 min)
        2. **Create GitHub Account** (3 min)  
        3. **Configure Git** (2 min)
        """)
    
    # Setup checklist
    st.markdown("## Setup Checklist")
    st.markdown("Complete these steps to get ready for GitHub:")
    
    setup_steps = [
        {
            "id": "install_git",
            "title": "1. Install Git",
            "description": "Download and install Git on your computer",
            "action": "Download from git-scm.com/downloads",
            "details": [
                "Choose your operating system (Windows, macOS, or Linux)",
                "Run the installer with default settings", 
                "Verify installation by opening terminal and typing: git --version"
            ]
        },
        {
            "id": "create_account", 
            "title": "2. Create GitHub Account",
            "description": "Sign up for a free GitHub account",
            "action": "Sign up at github.com/join",
            "details": [
                "Choose a username you're comfortable sharing",
                "Use your school email if possible",
                "Add a profile picture (optional)",
                "Verify your email address"
            ]
        },
        {
            "id": "configure_name",
            "title": "3. Configure Your Name", 
            "description": "Set your global Git username",
            "action": "git config --global user.name \"Your Name\"",
            "details": [
                "Open your terminal/command prompt",
                "Type: git config --global user.name \"Your Name\"",
                "Replace \"Your Name\" with your actual name",
                "This will appear on your commits"
            ]
        },
        {
            "id": "configure_email",
            "title": "4. Configure Your Email",
            "description": "Set your global Git email address", 
            "action": "git config --global user.email \"you@example.com\"",
            "details": [
                "Type: git config --global user.email \"your@email.com\"",
                "Use the same email as your GitHub account",
                "This connects your commits to your GitHub profile"
            ]
        },
        {
            "id": "verify_config",
            "title": "5. Verify Configuration",
            "description": "Check that Git is configured correctly",
            "action": "git config --list", 
            "details": [
                "Type: git config --list",
                "Look for user.name and user.email entries",
                "Press Q to exit the list",
                "If settings are missing, re-run the configure steps"
            ]
        }
    ]
    
    completed_count = sum(1 for step in setup_steps if st.session_state.setup_steps[step["id"]])
    
    # Progress indicator
    st.progress(completed_count / len(setup_steps))
    st.caption(f"Setup Progress: {completed_count} of {len(setup_steps)} completed")
    
    # Step checkboxes
    for i, step in enumerate(setup_steps, 1):
        with st.expander(f"Step {i}: {step['title']}", expanded=(i <= 2)):
            st.markdown(f"**What you need to do:** {step['description']}")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(step['action'], language='bash')
                
                st.markdown("**Details:**")
                for detail in step['details']:
                    st.markdown(f"• {detail}")
            
            with col2:
                completed = st.checkbox(
                    "Mark as completed",
                    value=st.session_state.setup_steps[step['id']],
                    key=f"setup_{step['id']}"
                )
                
                if completed != st.session_state.setup_steps[step['id']]:
                    st.session_state.setup_steps[step['id']] = completed
                    
                    # Check if all completed
                    if all(st.session_state.setup_steps.values()):
                        st.session_state.completed_pages.add("Getting Started")
                        st.balloons()
                        st.success("🎉 Setup Complete! You've successfully set up Git and GitHub!")
    
    # Terminal commands cheat sheet
    if completed_count > 0:
        st.markdown("""
        <div class='success-box'>
            <h3>💡 Pro Tip: Essential Terminal Commands</h3>
            <p>Keep these handy while you set up and practice:</p>
        </div>
        """, unsafe_allow_html=True)
        
        commands = [
            ("git --version", "Check Git version"),
            ("git config --global user.name \"Your Name\"", "Set your name"),
            ("git config --global user.email \"email@example.com\"", "Set your email"),
            ("git config --list", "View all configurations"),
            ("pwd", "Show current directory"),
            ("ls", "List files in current directory"),
            ("mkdir my-project", "Create a new folder"),
            ("cd my-project", "Change to project folder")
        ]
        
        for cmd, desc in commands:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.code(cmd, language='bash')
            with col2:
                st.text(desc)
    
    # Completion encouragement
    if completed_count == len(setup_steps):
        st.markdown("""
        <div style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                    color: white; padding: 2rem; border-radius: 10px; text-align: center; margin-top: 2rem;'>
            <h2>🎉 Setup Complete!</h2>
            <p>Congratulations! You've successfully set up Git and GitHub. You're ready to start learning version control.</p>
            <a href='#core-concepts' style='background: white; color: #11998e; padding: 1rem 2rem; 
               border-radius: 8px; text-decoration: none; font-weight: bold;'>Continue to Core Concepts →</a>
        </div>
        """, unsafe_allow_html=True)

def core_concepts_page():
    """Core Concepts with age-appropriate analogies"""
    display_header("Core Concepts", "Master the fundamentals through teen-friendly analogies", "🧠")
    
    st.markdown("Understanding these basics will make everything else click into place.")
    
    # Essential GitHub concepts with analogies
    concepts = [
        {
            "title": "Repository",
            "analogy": "🗃️ A locker or shared class folder",
            "description": "A single place that holds all your project files and their history",
            "details": "A repository is the home base for a project. It holds your files, folders, and a complete history of changes. In a school club, the repo is like a shared locker where everyone knows where to find the current files, and you can also see who changed what and when."
        },
        {
            "title": "Commit", 
            "analogy": "💾 A saved checkpoint in a game",
            "description": "A record of what you changed and why; the basic unit of history",
            "details": "A commit is a saved checkpoint. It records what you changed and why, forming a trail you can always look back on. Good commit messages are short and descriptive—'Fix layout on phones' or 'Add bio section'—so teammates (and future you) can quickly understand what happened."
        },
        {
            "title": "Branch",
            "analogy": "🌿 A side-quest track", 
            "description": "A parallel version of your project where you can experiment safely",
            "details": "A branch is a side-quest track. You can try a new feature, fix a bug, or experiment without messing up the main story. When you are happy with the results, you can bring those changes back into the main line. Branches are lightweight pointers that move forward as you commit, and they are central to parallel work in Git."
        },
        {
            "title": "Pull Request",
            "analogy": "📝 A group-edit request with discussion",
            "description": "A proposal to merge your changes; teammates can review and chat before merging", 
            "details": "A pull request proposes changes from one branch to another and opens a space for discussion and review. You can look at the differences, leave comments, and decide when to merge. On GitHub, this is the standard way teams collaborate safely."
        },
        {
            "title": "Merge",
            "analogy": "🔗 Combining tracks into the main story",
            "description": "Integrating changes from one branch into another, combining histories",
            "details": "Merging combines changes from one branch into another. After merging a pull request, you can delete the branch you merged, because its work is now part of the main story."
        },
        {
            "title": "Clone",
            "analogy": "📥 Downloading the locker contents to your computer", 
            "description": "A local copy of a remote repository, including its history",
            "details": "Cloning downloads a repository and its history to your computer, so you can work offline and push changes back to the remote."
        }
    ]
    
    # Display concepts in a grid
    cols = st.columns(2)
    for i, concept in enumerate(concepts):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
            <div style='background: white; border: 1px solid #e0e0e0; border-radius: 10px; padding: 1.5rem; margin: 0.5rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h3 style='color: #2c3e50; margin-bottom: 1rem;'>🧠 {concept['title']}</h3>
                <div style='background: #e8f4f8; padding: 0.8rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #3498db;'>
                    <strong>Analogy: {concept['analogy']}</strong>
                </div>
                <p style='color: #7f8c8d; margin-bottom: 1rem;'>{concept['description']}</p>
                <div style='border-top: 1px solid #ecf0f1; padding-top: 1rem; font-size: 0.9rem; color: #34495e;'>
                    {concept['details']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Branch naming best practices
    st.markdown("## Branch Naming Best Practices")
    st.markdown("Use a pattern like `type/short-description` to keep branches clear for everyone.")
    
    branch_examples = [
        ("feature/about-page", "Add a new 'About' page"),
        ("bugfix/typo-title", "Fix a typo in the title"), 
        ("fix/mobile-menu", "Repair the mobile menu")
    ]
    
    for branch_name, purpose in branch_examples:
        st.markdown(f"""
        <div style='border-left: 4px solid #3498db; padding: 0.8rem; background: #f8f9fa; margin: 0.5rem 0;'>
            <code style='background: #e9ecef; padding: 0.2rem 0.4rem; border-radius: 4px; color: #d63384;'>{branch_name}</code>
            <p style='margin: 0.5rem 0 0 0; color: #6c757d;'>{purpose}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4>💡 Why naming matters:</h4>
        <p>Clear branch names help teammates understand what you're working on without having to dig into the code changes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Three areas workflow
    st.markdown("## How Changes Move Through Git")
    st.markdown("Understanding the three areas explains how your changes move from 'desk' to 'history' to 'cloud.'")
    
    workflow_areas = [
        {
            "name": "Working Directory",
            "description": "Your current files on disk", 
            "action": "Edit, create, delete files",
            "color": "primary"
        },
        {
            "name": "Staging Area",
            "description": "A prep space to select changes",
            "action": "git add the changes you want to commit", 
            "color": "warning"
        },
        {
            "name": "Local Repository",
            "description": "The history stored on your machine",
            "action": "git commit to record staged changes",
            "color": "success"
        },
        {
            "name": "Remote Repository", 
            "description": "The cloud version on GitHub",
            "action": "git push to upload; git pull to download updates",
            "color": "secondary"
        }
    ]
    
    for i, area in enumerate(workflow_areas, 1):
        color_map = {
            "primary": ("#3498db", "#e3f2fd"),
            "warning": ("#f39c12", "#fff8e1"), 
            "success": ("#27ae60", "#e8f5e8"),
            "secondary": ("#9b59b6", "#f3e5f5")
        }
        border_color, bg_color = color_map[area["color"]]
        
        st.markdown(f"""
        <div style='padding: 1.5rem; border: 2px solid {border_color}; background: {bg_color}; border-radius: 8px; margin: 1rem 0;'>
            <div style='display: flex; justify-content: between; align-items: center; margin-bottom: 0.5rem;'>
                <h4 style='margin: 0; color: #2c3e50;'>{i}. {area['name']}</h4>
                <span style='background: {border_color}; color: white; padding: 0.2rem 0.6rem; border-radius: 20px; font-size: 0.8rem;'>Step {i}</span>
            </div>
            <p style='margin: 0.5rem 0; color: #34495e;'>{area['description']}</p>
            <code style='background: white; padding: 0.4rem 0.6rem; border-radius: 4px; color: #d63384; font-size: 0.9rem;'>{area['action']}</code>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='success-box'>
        <h4>🔄 The path is: edit → stage → commit → push</h4>
        <p>Understanding this flow helps you keep changes organized and makes collaboration smoother.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    takeaways = [
        {
            "title": "Think in Analogies",
            "description": "GitHub concepts become easier when you relate them to familiar experiences like lockers, game checkpoints, and group projects.",
            "icon": "🧠"
        },
        {
            "title": "Collaboration is Key", 
            "description": "GitHub is designed for teamwork. Branches and pull requests let multiple people work on the same project safely.",
            "icon": "👥"
        },
        {
            "title": "Practice Makes Perfect",
            "description": "The more you use these concepts, the more natural they'll become. Start with simple projects and build up.", 
            "icon": "💪"
        }
    ]
    
    cols = st.columns(3)
    for i, takeaway in enumerate(takeaways):
        with cols[i]:
            st.markdown(f"""
            <div style='text-align: center; padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>{takeaway['icon']}</div>
                <h4 style='color: #2c3e50; margin-bottom: 1rem;'>{takeaway['title']}</h4>
                <p style='color: #7f8c8d; font-size: 0.9rem;'>{takeaway['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Completion button
    if st.button("✅ Mark Core Concepts as Complete", use_container_width=True):
        st.session_state.completed_pages.add("Core Concepts")
        st.balloons()
        st.success("Great job! You've mastered the core concepts. Ready to create your first repository?")

def first_repository_page():
    """First Repository - Hello World Tutorial"""
    display_header("Your First Repository", "Create your first GitHub repository with the classic 'Hello World' tutorial", "🏗️")
    
    st.markdown("This quick walkthrough shows you how collaboration works without touching the command line.")
    
    # Quick actions overview
    st.markdown("## Quick Actions Overview")
    
    quick_actions = [
        ("Create repo", "Makes a new project home on GitHub", "Everything starts here", "📁"),
        ("Create branch", "Makes a parallel workspace", "Safe experimentation", "🌿"),
        ("Edit and commit", "Saves a checkpoint with a message", "Clear, reviewable history", "💾"),
        ("Open pull request", "Proposes to merge changes", "Enables review and discussion", "📝"),
        ("Merge", "Integrates changes into main", "Delivers the work", "🔗")
    ]
    
    cols = st.columns(5)
    for i, (action, what, why, icon) in enumerate(quick_actions):
        with cols[i]:
            st.markdown(f"""
            <div style='text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px; margin: 0.5rem 0;'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>{icon}</div>
                <h4 style='color: #2c3e50; margin: 0.5rem 0;'>{action}</h4>
                <p style='color: #6c757d; font-size: 0.8rem; margin: 0.2rem 0;'>{what}</p>
                <p style='color: #007bff; font-size: 0.8rem; font-weight: bold;'>{why}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Step-by-step tutorial
    st.markdown("## Step-by-Step Tutorial")
    
    steps = [
        {
            "title": "Create a Repository",
            "description": "Click the '+' icon in the top right and select 'New repository'",
            "details": [
                "Name it 'hello-world'",
                "Write a short description like 'Practicing the GitHub Flow'", 
                "Choose Public or Private (ask your teacher which is right for your class)",
                "Add a README file so the repo explains itself",
                "Click 'Create repository'"
            ],
            "tip": "A README file (written in Markdown) is your chance to tell visitors what the project is about, how to use it, and who contributed."
        },
        {
            "title": "Make a Branch", 
            "description": "Go to the 'Code' tab and create a new branch",
            "details": [
                "Click the branch dropdown (it says 'main' by default)",
                "Type 'readme-edits' and select 'Create branch: readme-edits from main'",
                "You now have a copy of main where you can make changes without touching the main project"
            ],
            "tip": "Branches let you experiment without breaking the main project. Think of it like having a draft version of your document."
        },
        {
            "title": "Commit Changes",
            "description": "Edit a file and save your progress", 
            "details": [
                "Open README.md and click the pencil icon to edit",
                "Add a few lines about yourself or your project",
                "Scroll down and commit your changes with a clear message like 'Add intro to README'"
            ],
            "tip": "Good commit messages are short and descriptive. They help you and your teammates understand what changed."
        },
        {
            "title": "Open and Merge a Pull Request",
            "description": "Propose your changes for review and merge them",
            "details": [
                "Go to the 'Pull requests' tab and click 'New pull request'",
                "Choose 'readme-edits' as the branch to compare with 'main'",
                "Review the differences; if it looks good, click 'Create pull request'",
                "Add a short title and description, then click 'Create pull request' again", 
                "When you are ready, click 'Merge pull request' and 'Confirm merge'",
                "Optionally, delete the branch you merged; this keeps the repo tidy"
            ],
            "tip": "Pull requests are like asking your teacher to review your work before turning it in. They enable discussion and quality control."
        }
    ]
    
    for i, step in enumerate(steps, 1):
        with st.expander(f"Step {i}: {step['title']}", expanded=(i <= 2)):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**What to do:** {step['description']}")
                
                st.markdown("**Detailed steps:**")
                for detail in step['details']:
                    st.markdown(f"• {detail}")
                
                st.markdown(f"""
                <div class='info-box'>
                    <h4>💡 Pro Tip:</h4>
                    <p>{step['tip']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # README explanation
    st.markdown("## What Is a README and Why It Matters")
    st.markdown("A README is the first thing people see. Use it to explain the project in plain language—what it does, how to run or open it, and how to contribute.")
    
    readme_template = """# Project Name

A brief description of what this project does.

## Getting Started

How to get started with this project.

## Contributing

How others can contribute to this project.

## License

What license this project uses."""
    
    st.code(readme_template, language='markdown')
    
    # Merge conflicts primer
    st.markdown("""
    <div class='warning-box'>
        <h3>⚠️ Merge Conflicts: A Quick Primer</h3>
        <p>A merge conflict happens when two branches change the same line in different ways, and Git cannot automatically combine them. GitHub will show you the conflict and let you choose which change to keep (or keep both).</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='background: #f8d7da; border: 1px solid #f5c6cb; padding: 1rem; border-radius: 8px; text-align: center;'>
            <h4>&lt;&lt;&lt;&lt;&lt;&lt;</h4>
            <p>Start of your change</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='background: #fff3cd; border: 1px solid #ffeaa7; padding: 1rem; border-radius: 8px; text-align: center;'>
            <h4>=======</h4>
            <p>Separator - compare both sides</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style='background: #d4edda; border: 1px solid #c3e6cb; padding: 1rem; border-radius: 8px; text-align: center;'>
            <h4>&gt;&gt;&gt;&gt;&gt;&gt;</h4>
            <p>End of the other change</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='warning-box'>
        <h4>🔧 Fix:</h4>
        <p>Resolve the conflict, stage the file, and continue the merge. For this simple exercise, conflicts are unlikely. If they happen, read the on-screen instructions, resolve the differences, and mark the PR as ready to merge.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Completion
    if st.button("✅ Complete First Repository Tutorial", use_container_width=True):
        st.session_state.completed_pages.add("First Repository")
        st.balloons()
        st.success("🎉 Excellent! You've created your first repository. Ready to learn the command line?")

def command_line_page():
    """Command Line - Git commands and workflows"""
    display_header("Command Line Basics", "Learn Git commands and how to sync your local work with GitHub", "⌨️")
    
    st.markdown("Master the essential workflow: edit → stage → commit → push.")
    
    # From local to GitHub flow
    st.markdown("## From Local Folder to GitHub")
    
    command_flow = [
        {
            "step": "Create project",
            "command": "mkdir my-first-repo",
            "description": "Make and enter a folder",
            "what": "Creates a new directory for your project"
        },
        {
            "step": "Start tracking",
            "command": "git init", 
            "description": "Initialize a local repo",
            "what": "Turns the current folder into a Git repository"
        },
        {
            "step": "Create a file",
            "command": "touch readme.md",
            "description": "Add a file",
            "what": "Creates an empty README file for your project"
        },
        {
            "step": "Check status",
            "command": "git status",
            "description": "See untracked changes", 
            "what": "Shows what files have been changed or added"
        },
        {
            "step": "Stage changes",
            "command": "git add readme.md",
            "description": "Put file into staging",
            "what": "Stages the file for commit"
        },
        {
            "step": "Commit",
            "command": "git commit -m \"Add readme\"",
            "description": "Save a checkpoint",
            "what": "Creates a permanent record of your changes"
        },
        {
            "step": "Add remote",
            "command": "git remote add origin <URL>",
            "description": "Link to GitHub repo",
            "what": "Connects your local repo to GitHub"
        },
        {
            "step": "Push",
            "command": "git push -u origin main",
            "description": "Upload to GitHub", 
            "what": "Uploads your commits to GitHub"
        },
        {
            "step": "Pull updates",
            "command": "git pull",
            "description": "Download and merge changes",
            "what": "Downloads and merges changes from GitHub"
        }
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🖥️ Local Setup (Steps 1-5)")
        for i, step in enumerate(command_flow[:5], 1):
            st.markdown(f"""
            <div style='border-left: 4px solid #3498db; padding: 0.8rem; background: #f8f9fa; margin: 0.5rem 0;'>
                <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem;'>
                    <span style='background: #3498db; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;'>{i}</span>
                    <code style='background: #e9ecef; padding: 0.2rem 0.4rem; border-radius: 4px; color: #d63384;'>{step['command']}</code>
                </div>
                <p style='margin: 0.3rem 0 0 0; color: #6c757d; font-size: 0.9rem;'>{step['what']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ☁️ Connect to GitHub (Steps 6-9)")
        for i, step in enumerate(command_flow[5:], 6):
            st.markdown(f"""
            <div style='border-left: 4px solid #9b59b6; padding: 0.8rem; background: #f8f9fa; margin: 0.5rem 0;'>
                <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem;'>
                    <span style='background: #9b59b6; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;'>{i}</span>
                    <code style='background: #e9ecef; padding: 0.2rem 0.4rem; border-radius: 4px; color: #d63384;'>{step['command']}</code>
                </div>
                <p style='margin: 0.3rem 0 0 0; color: #6c757d; font-size: 0.9rem;'>{step['what']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Core cycle visualization
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 10px; text-align: center; margin: 2rem 0;'>
        <h3>🔄 The Core Git Cycle</h3>
        <div style='display: flex; justify-content: center; align-items: center; gap: 1rem; flex-wrap: wrap; margin: 1rem 0;'>
            <div style='background: rgba(255,255,255,0.2); padding: 0.8rem; border-radius: 50px;'>1. Edit files</div>
            <span>→</span>
            <div style='background: rgba(255,255,255,0.2); padding: 0.8rem; border-radius: 50px;'>2. git add</div>
            <span>→</span>
            <div style='background: rgba(255,255,255,0.2); padding: 0.8rem; border-radius: 50px;'>3. git commit</div>
            <span>→</span>
            <div style='background: rgba(255,255,255,0.2); padding: 0.8rem; border-radius: 50px;'>4. git push</div>
        </div>
        <p>Use <code style='background: rgba(255,255,255,0.3); padding: 0.2rem 0.4rem; border-radius: 4px;'>git status</code> often, especially when you are learning. It tells you what changed, what is staged, and what is untracked.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Most used commands
    st.markdown("## Local Commands You Will Use Most")
    
    most_used = [
        ("git status", "Before and after edits", "Shows staged/unstaged/untracked files"),
        ("git add .", "Stage all current changes", "Prepares changes for commit"),
        ("git commit -m \"message\"", "Save work with a note", "Adds a new commit to history"),
        ("git log", "Review history", "Lists commits; press Q to exit"),
        ("git push", "Send commits to GitHub", "Uploads your branch"),
        ("git pull", "Get latest from GitHub", "Downloads and merges updates"),
        ("git branch", "List branches", "Shows current branch and others"),
        ("git checkout -b name", "Create and switch", "New branch ready for work"),
        ("git merge name", "Combine branch", "Integrates changes, may conflict")
    ]
    
    for cmd, when, expect in most_used:
        col1, col2, col3 = st.columns([2, 2, 3])
        with col1:
            st.code(cmd, language='bash')
        with col2:
            st.caption(f"**When:** {when}")
        with col3:
            st.caption(f"**Expect:** {expect}")
    
    # Branching and merging
    st.markdown("## Branching and Merging Locally")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌿 Create a Branch")
        st.code("git checkout -b feature/new-page", language='bash')
        st.markdown("Creates and switches to a new branch. Use the modern `git switch` equivalents if your version supports them.")
    
    with col2:
        st.markdown("### 🔗 Merge Changes")
        st.code("git merge feature/new-page", language='bash')
        st.markdown("Combines changes from another branch. If the same line changed in both branches, you will get a conflict—resolve it by editing the file, staging, and committing the merge.")
    
    # Important notes
    st.markdown("""
    <div class='info-box'>
        <h3>📝 Important Notes</h3>
        <ul>
            <li><strong>Default branch names:</strong> Older guides use "master," while modern defaults use "main." Follow your teacher's policy.</li>
            <li><strong>One focused change per commit:</strong> Good commit messages like "Fix hamburger menu on mobile" make history clear.</li>
            <li><strong>Use -u flag:</strong> The first time you push, use <code>git push -u origin main</code> to set up tracking.</li>
            <li><strong>View history:</strong> <code>git log</code> shows your commit trail; press Q to exit the pager.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✅ Complete Command Line Basics", use_container_width=True):
        st.session_state.completed_pages.add("Command Line")
        st.balloons()
        st.success("🚀 Great work! You're now ready to collaborate with others using GitHub!")

def collaboration_page():
    """Collaboration - Team workflows and pull requests"""
    display_header("Collaboration", "Master branches, pull requests, and code review", "👥")
    
    st.markdown("Learn how teams work together safely and efficiently using GitHub's collaboration features.")
    
    # Simple team workflow
    st.markdown("## Simple Team Workflow")
    st.markdown("Branches keep your main project stable. When you want to add a feature or fix something, create a branch, do the work, and open a pull request.")
    
    team_workflow = [
        ("Any teammate", "Create branch", "Makes a safe workspace"),
        ("Any teammate", "Commit changes", "Saves focused updates with clear messages"),
        ("Any teammate", "Push branch", "Uploads branch to GitHub"),
        ("Any teammate", "Open PR", "Proposes merge and starts review"),
        ("Teammates", "Review", "Comments, requests changes, approves"),
        ("Maintainer or team", "Merge", "Integrates changes into main"),
        ("Maintainer or team", "Delete branch", "Cleans up completed work")
    ]
    
    for i, (who, action, happens) in enumerate(team_workflow, 1):
        st.markdown(f"""
        <div class='step-container'>
            <div style='display: flex; align-items: center; gap: 1rem;'>
                <div style='background: #3498db; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;'>{i}</div>
                <div style='flex: 1;'>
                    <div style='color: #007bff; font-weight: bold;'>{who}</div>
                    <div style='color: #2c3e50; font-weight: bold; margin: 0.2rem 0;'>{action}</div>
                    <div style='color: #6c757d;'>{happens}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # What is a pull request
    st.markdown("## What is a Pull Request?")
    st.markdown("A pull request shows a diff—a side-by-side view of what changed—and invites discussion. Reviewers can leave comments, suggest changes, and approve the PR. When approved, you merge and delete the branch.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Before Opening PR:")
        st.markdown("""
        <ul>
            <li>Make sure your code works</li>
            <li>Test your changes</li>
            <li>Write a clear description</li>
            <li>Link related issues</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 👀 When Reviewing PRs:")
        st.markdown("""
        <ul>
            <li>Test the changes if possible</li>
            <li>Check code quality and style</li>
            <li>Ask questions if something is unclear</li>
            <li>Suggest improvements kindly</li>
        </ul>
        """, unsafe_allow_html=True)
    
    # Best practices
    st.markdown("## Collaboration Best Practices")
    
    practices = [
        {
            "title": "Branch Naming",
            "tip": "Use clear names like feature/about-page or bugfix/typo-contact",
            "why": "Helps everyone understand what the branch is for"
        },
        {
            "title": "Commit Messages", 
            "tip": "Write in present tense: 'Add search bar' not 'Added search bar'",
            "why": "Consistency makes history easier to read"
        },
        {
            "title": "PR Size",
            "tip": "Keep pull requests small and focused",
            "why": "Easier to review and merge quickly"
        },
        {
            "title": "Code Review",
            "tip": "Be kind and specific: 'Consider adding alt text for accessibility'",
            "why": "Positive feedback helps everyone learn"
        }
    ]
    
    cols = st.columns(2)
    for i, practice in enumerate(practices):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
            <div style='background: white; border: 1px solid #e0e0e0; border-radius: 10px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h4 style='color: #2c3e50; margin-bottom: 1rem;'>{practice['title']}</h4>
                <div style='background: #e8f4f8; padding: 0.8rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #3498db;'>
                    <strong style='color: #2c3e50;'>💡 {practice['tip']}</strong>
                </div>
                <p style='color: #6c757d; margin: 0;'>{practice['why']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Code review benefits
    st.markdown("## Why Code Review Matters")
    
    benefits = [
        {
            "title": "Catches Mistakes",
            "description": "Two sets of eyes are better than one. Review helps catch bugs and issues before they reach users.",
            "icon": "🔍"
        },
        {
            "title": "Shares Knowledge", 
            "description": "Review spreads knowledge across the team. Everyone learns from each other's approaches and solutions.",
            "icon": "📚"
        },
        {
            "title": "Maintains Quality",
            "description": "Consistent review helps maintain coding standards and project quality across all contributions.",
            "icon": "⭐"
        }
    ]
    
    cols = st.columns(3)
    for benefit in benefits:
        with cols[benefits.index(benefit)]:
            st.markdown(f"""
            <div style='text-align: center; padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>{benefit['icon']}</div>
                <h4 style='color: #2c3e50; margin-bottom: 1rem;'>{benefit['title']}</h4>
                <p style='color: #7f8c8d; font-size: 0.9rem;'>{benefit['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Kind reviewing
    st.markdown("## How to Review Code Kindly")
    st.markdown("Reviewing is not about being critical; it's about helping each other catch mistakes and learn. Keep comments friendly and specific.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='border-left: 4px solid #28a745; padding: 1rem; background: #d4edda; border-radius: 8px;'>
            <h4 style='color: #155724;'>✅ Good Review Comment:</h4>
            <p style='color: #155724; margin: 0;'>"Consider adding alt text to this image for accessibility. Screen readers will be able to describe the image to users."</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='border-left: 4px solid #dc3545; padding: 1rem; background: #f8d7da; border-radius: 8px;'>
            <h4 style='color: #721c24;'>❌ Avoid This Type of Comment:</h4>
            <p style='color: #721c24; margin: 0;'>"This is wrong. Why would you do it this way?"</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("✅ Complete Collaboration Tutorial", use_container_width=True):
        st.session_state.completed_pages.add("Collaboration")
        st.balloons()
        st.success("🤝 Perfect! You're now ready to work effectively in teams. Next up: best practices!")

def best_practices_page():
    """Best Practices - Common mistakes and professional habits"""
    display_header("Best Practices", "Learn the common mistakes that trip up beginners and how to avoid them", "⭐")
    
    st.markdown("These habits will save you time, stress, and help you work like a pro.")
    
    # Common beginner mistakes
    st.markdown("## Common Beginner Mistakes (and How to Avoid Them)")
    
    mistakes = [
        {
            "mistake": "Not using .gitignore",
            "why": "Clutters repos with temp files and secrets",
            "better": "Create .gitignore for the project type",
            "fix": "Add patterns for logs, caches, keys; commit .gitignore",
            "severity": "high"
        },
        {
            "mistake": "Vague branch names",
            "why": "No one knows what the branch does", 
            "better": "Use type/short-description",
            "fix": "Rename with git branch -m new-name",
            "severity": "medium"
        },
        {
            "mistake": "Changing main directly",
            "why": "Risky, hard to roll back",
            "better": "Work on feature branches, PR to main",
            "fix": "Create a branch, move your changes there",
            "severity": "high"
        },
        {
            "mistake": "Weak commit messages",
            "why": "History is unclear",
            "better": "Write short, descriptive messages", 
            "fix": "git commit --amend to improve last message",
            "severity": "medium"
        },
        {
            "mistake": "Big, unrelated commits",
            "why": "Hard to review and revert",
            "better": "Keep changes small and focused",
            "fix": "Split into multiple commits when possible",
            "severity": "medium"
        },
        {
            "mistake": "Skipping pull requests",
            "why": "Less review, more mistakes",
            "better": "Open PRs even for small changes",
            "fix": "Push branch and open a PR",
            "severity": "low"
        },
        {
            "mistake": "Branch vs fork confusion",
            "why": "Wrong tool for contribution",
            "better": "Use branches for your repo; forks when you do not own it",
            "fix": "Fork on GitHub; PR from your fork to upstream",
            "severity": "medium"
        }
    ]
    
    for mistake in mistakes:
        severity_colors = {
            "high": ("#dc3545", "#f8d7da"),
            "medium": ("#ffc107", "#fff3cd"), 
            "low": ("#6c757d", "#f8f9fa")
        }
        
        border_color, bg_color = severity_colors[mistake["severity"]]
        
        st.markdown(f"""
        <div class='step-container'>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;'>
                <div>
                    <h4 style='color: #dc3545; margin-bottom: 0.5rem;'>❌ Mistake: {mistake['mistake']}</h4>
                    <p style='color: #721c24; background: {bg_color}; padding: 0.8rem; border-radius: 8px; border-left: 4px solid {border_color};'>
                        <strong>Why it hurts:</strong> {mistake['why']}
                    </p>
                </div>
                <div>
                    <h4 style='color: #28a745; margin-bottom: 0.5rem;'>✅ Better Habit: {mistake['better']}</h4>
                    <p style='color: #155724; background: #d4edda; padding: 0.8rem; border-radius: 8px; border-left: 4px solid #28a745;'>
                        <strong>Quick fix:</strong> {mistake['fix']}
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # .gitignore basics
    st.markdown("## .gitignore Basics")
    st.markdown("A `.gitignore` file tells Git which files to ignore. The point is to avoid committing anything sensitive or unneeded.")
    
    gitignore_examples = [
        ("OS and editor files", ".DS_Store, Thumbs.db, *.tmp", "Avoids system clutter"),
        ("Logs and caches", "*.log, .cache/", "Prevents large, changing files"),
        ("Build outputs", "dist/, build/", "Keeps repo lean; these can be regenerated"),
        ("Secrets", "keys.json, *.key", "Protects credentials from exposure"),
        ("Node modules (if used)", "node_modules/", "Large folder; package managers can restore")
    ]
    
    cols = st.columns(2)
    for i, (category, examples, why) in enumerate(gitignore_examples):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
            <div style='border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; background: white; margin: 0.5rem 0;'>
                <h4 style='color: #2c3e50; margin-bottom: 0.5rem;'>{category}</h4>
                <code style='background: #f8f9fa; padding: 0.4rem 0.6rem; border-radius: 4px; color: #d63384; display: block; margin-bottom: 0.5rem;'>{examples}</code>
                <p style='color: #6c757d; margin: 0; font-size: 0.9rem;'>{why}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4>💡 Pro Tip:</h4>
        <p>Start with a small, project-specific list and grow it only when you know why. For many classroom projects, ignoring temporary files, logs, and system files is enough.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Commit hygiene
    st.markdown("## Commit Hygiene")
    st.markdown("Good commit habits will carry you far. Here are the key principles for writing great commit messages:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Best Practices:")
        commit_tips = [
            "Commit frequently, keep each commit focused",
            "Write messages that future you will thank you for",
            "Use present tense: 'Add feature' not 'Added feature'",
            "If you make a mistake in the last commit message, you can amend it",
            "Avoid force-push unless your teacher explicitly approves it",
            "One commit should represent one logical change"
        ]
        
        for tip in commit_tips:
            st.markdown(f"• {tip}")
    
    with col2:
        st.markdown("### Good vs Bad Examples:")
        
        st.markdown("""
        <div style='border-left: 4px solid #28a745; padding: 0.8rem; background: #d4edda; border-radius: 8px; margin-bottom: 1rem;'>
            <h5 style='color: #155724; margin-bottom: 0.5rem;'>✅ Good:</h5>
            <code style='color: #155724; display: block;'>"Add user profile page with bio section"</code>
            <code style='color: #155724; display: block;'>"Fix mobile menu layout on small screens"</code>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='border-left: 4px solid #dc3545; padding: 0.8rem; background: #f8d7da; border-radius: 8px;'>
            <h5 style='color: #721c24; margin-bottom: 0.5rem;'>❌ Bad:</h5>
            <code style='color: #721c24; display: block;'>"Fixed stuff"</code>
            <code style='color: #721c24; display: block;'>"updated the thing"</code>
            <code style='color: #721c24; display: block;'>"wip"</code>
        </div>
        """, unsafe_allow_html=True)
    
    # Safety and ethics
    st.markdown("## Safe and Ethical Use")
    st.markdown("A few responsible-use principles will keep you and your classmates safe:")
    
    safety_tips = [
        {
            "title": "Do not commit secrets",
            "description": "That includes passwords, API keys, or any sensitive data.",
            "action": "If a project needs secret values, keep them out of the repo and use environment variables or configuration files that are ignored by Git."
        },
        {
            "title": "Respect privacy",
            "description": "Do not share personal information in issues, pull requests, or code.",
            "action": "Keep personal data out of repositories and discussions."
        },
        {
            "title": "Follow school policies",
            "description": "Your teacher may require private repositories, specific naming rules, or restrictions on forking.",
            "action": "When in doubt, ask your teacher for guidance."
        }
    ]
    
    for tip in safety_tips:
        st.markdown(f"""
        <div class='step-container'>
            <h4 style='color: #2c3e50; margin-bottom: 0.5rem;'>{tip['title']}</h4>
            <p style='color: #6c757d; margin-bottom: 1rem;'>{tip['description']}</p>
            <div class='info-box'>
                <strong>Action:</strong> {tip['action']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: #f8d7da; border: 1px solid #f5c6cb; border-radius: 8px; padding: 1rem; margin: 1rem 0;'>
        <h4 style='color: #721c24; margin-bottom: 0.5rem;'>🚨 If You Accidentally Commit a Secret:</h4>
        <p style='color: #721c24; margin: 0;'>Talk to your teacher immediately and follow their guidance to remove it safely from history. Never commit API keys, passwords, or other sensitive information.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    takeaways = [
        {
            "title": "Prevention is Key",
            "description": "A little setup work (like .gitignore) prevents big problems later. Good habits save time and stress.",
            "icon": "🛡️"
        },
        {
            "title": "Clear Communication",
            "description": "Good branch names and commit messages make collaboration smoother for everyone involved.",
            "icon": "💬"
        },
        {
            "title": "Stay Organized",
            "description": "Keep changes focused, use branches for experiments, and let pull requests do the heavy lifting.",
            "icon": "🗂️"
        }
    ]
    
    cols = st.columns(3)
    for takeaway in takeaways:
        with cols[takeaways.index(takeaway)]:
            st.markdown(f"""
            <div style='text-align: center; padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>{takeaway['icon']}</div>
                <h4 style='color: #2c3e50; margin-bottom: 1rem;'>{takeaway['title']}</h4>
                <p style='color: #7f8c8d; font-size: 0.9rem;'>{takeaway['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    if st.button("✅ Complete Best Practices", use_container_width=True):
        st.session_state.completed_pages.add("Best Practices")
        st.balloons()
        st.success("🎯 Excellent! You're now equipped with professional habits. Ready to build something real?")

def real_projects_page():
    """Real Projects - Project ideas and applications"""
    display_header("Real Projects", "Apply what you've learned to build something awesome", "🚀")
    
    st.markdown("These project ideas are fun, scope-appropriate, and naturally use GitHub's collaboration features.")
    
    # Project ideas
    st.markdown("## Project Ideas You'll Want to Build")
    
    projects = [
        {
            "title": "Game Assets Repository",
            "description": "Textures, sprites, and level ideas for your game projects",
            "icon": "🎮",
            "skills": ["Asset management", "Version control", "Collaboration"],
            "features": [
                "Organize sprites, textures, and level designs",
                "Track different versions of game assets", 
                "Collaborate with other game developers",
                "Maintain consistent art style across versions"
            ],
            "branch_example": "feature/new-enemy-sprites",
            "commit_example": "Add enemy sprite variations for level 3"
        },
        {
            "title": "School Club Website",
            "description": "A page for officers, events, and contact information",
            "icon": "👥",
            "skills": ["Web development", "Content management", "Design"],
            "features": [
                "Create pages for different club sections",
                "Update event schedules and announcements",
                "Showcase club projects and achievements",
                "Collect contact information from interested students"
            ],
            "branch_example": "feature/officer-profiles",
            "commit_example": "Add bio section for club president"
        },
        {
            "title": "Playlist Tracker",
            "description": "Catalog your favorite tracks with metadata and ratings",
            "icon": "🎵",
            "skills": ["Data organization", "API integration", "Personal projects"],
            "features": [
                "Track your music collection and ratings",
                "Add album art and genre information",
                "Create mood-based playlists",
                "Share recommendations with friends"
            ],
            "branch_example": "feature/album-art-integration",
            "commit_example": "Add Spotify API for album artwork"
        }
    ]
    
    for project in projects:
        with st.expander(f"{project['icon']} {project['title']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**{project['description']}**")
                
                st.markdown("**Skills you'll develop:**")
                for skill in project['skills']:
                    st.markdown(f"• {skill}")
                
                st.markdown("**Project features:**")
                for feature in project['features']:
                    st.markdown(f"• {feature}")
            
            with col2:
                st.markdown("**Example branch name:**")
                st.code(project['branch_example'], language='bash')
                st.markdown("**Example commit message:**")
                st.code(project['commit_example'], language='bash')
    
    # Project benefits
    st.markdown("## Why Build Real Projects?")
    
    project_benefits = [
        ("Real-world Practice", "Build something you actually care about, not just example exercises"),
        ("Portfolio Building", "Your repository history becomes a record of growth you can be proud of"),
        ("Collaboration Skills", "Learn to work with others on projects that matter to your community"),
        ("Problem Solving", "Face real challenges and learn to debug and improve your work")
    ]
    
    cols = st.columns(2)
    for i, (benefit, description) in enumerate(project_benefits):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
            <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 1.5rem; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h4 style='color: #2c3e50; margin-bottom: 1rem;'>{benefit}</h4>
                <p style='color: #6c757d; margin: 0;'>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Building process
    st.markdown("## How to Build Your First Real Project")
    
    building_steps = [
        ("Choose Your Project", "Pick something you're excited about. Passion makes learning easier.", "🎯"),
        ("Start Small", "Begin with the core features. You can always add more later.", "🌱"),
        ("Use Branches", "Practice branch naming and merge workflows with feature branches.", "🌿"),
        ("Document & Share", "Write good commit messages and README files to share your work.", "📝")
    ]
    
    cols = st.columns(4)
    for i, (title, description, icon) in enumerate(building_steps, 1):
        with cols[i-1]:
            st.markdown(f"""
            <div style='text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin: 0.5rem 0;'>
                <div style='font-size: 2.5rem; margin-bottom: 1rem;'>{icon}</div>
                <h4 style='margin-bottom: 1rem;'>{i}. {title}</h4>
                <p style='font-size: 0.9rem; opacity: 0.9;'>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Next steps
    st.markdown("## What Comes Next?")
    
    next_steps = [
        ("GitHub Skills Courses", "Structured practice with hands-on challenges", "https://skills.github.com", "⭐"),
        ("Git Cheat Sheet", "Keep the official Git Cheat Sheet nearby for commands and patterns", "https://education.github.com/git-cheat-sheet-education.pdf", "🔧"),
        ("Multi-Branch Project", "Plan a small website or game with main branch and feature branches", None, "💻"),
        ("Public Portfolio", "Build a public portfolio by curating your best repositories", None, "🌐")
    ]
    
    for title, description, link, icon in next_steps:
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 1.5rem; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 2rem;'>{icon}</div>
                    <div>
                        <h4 style='color: #2c3e50; margin: 0;'>{title}</h4>
                        <p style='color: #6c757d; margin: 0.5rem 0 0 0;'>{description}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if link:
                st.link_button("Visit", link)
    
    # Growth mindset
    st.markdown("## The Key to Steady Progress")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;'>
        <h3 style='margin-bottom: 1rem;'>🎯 The Secret to Success</h3>
        <p style='font-size: 1.2rem; margin-bottom: 1.5rem; line-height: 1.6;'>
            The key to steady progress is <strong>small, frequent practice</strong>. 
            Set a goal like <em>"one repository, one branch, one PR per week,"</em> and 
            keep your messages short and honest.
        </p>
        <div style='background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px;'>
            <p style='margin: 0; font-size: 1.1rem;'>
                <strong>Your Learning Journey:</strong><br>
                Over time, your repository history will become a record of growth you can be proud of. 
                Each commit, each branch, each merged pull request tells the story of how you learned and improved.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✅ Complete Real Projects", use_container_width=True):
        st.session_state.completed_pages.add("Real Projects")
        st.balloons()
        st.success("🎉 Amazing! You're ready to tackle real-world projects. Test your knowledge with our practice quiz!")

def practice_page():
    """Practice - Interactive quizzes and testing"""
    display_header("Practice & Mastery", "Test your knowledge with interactive quizzes", "🎯")
    
    st.markdown("Review explanations for each question to strengthen your understanding of GitHub concepts.")
    
    # Quiz sections
    quiz_sections = {
        "core-concepts": {
            "title": "Core Concepts",
            "description": "Test your understanding of repositories, commits, and branches",
            "questions": [
                {
                    "id": "cc1",
                    "question": "What is a repository, and how is it like a locker or shared folder?",
                    "options": [
                        "A type of computer program",
                        "A single place that holds all your project files and their history",
                        "A website where you post code", 
                        "A backup system for your computer"
                    ],
                    "correct": 1,
                    "explanation": "A repository is the project home that holds files and history, like a shared locker where everyone knows where to find the current files."
                },
                {
                    "id": "cc2", 
                    "question": "Why are commit messages important? Give a good and a bad example.",
                    "options": [
                        "They do not matter much",
                        "They help you and teammates understand what changed; good: 'Add bio section', bad: 'Fixed stuff'",
                        "They are only for show",
                        "They must be exactly 10 characters long"
                    ],
                    "correct": 1,
                    "explanation": "Commit messages should be short and descriptive. 'Add bio section' is good because it tells you what changed, while 'Fixed stuff' is too vague."
                },
                {
                    "id": "cc3",
                    "question": "What does a branch let you do, and when should you delete a branch after merging?",
                    "options": [
                        "Nothing special",
                        "Work in parallel and merge later; delete after merging to keep repo tidy",
                        "Only for experts", 
                        "Create new repositories"
                    ],
                    "correct": 1,
                    "explanation": "Branches let you work in parallel and merge later. You should delete a branch after merging its changes into main to keep the repository tidy."
                }
            ]
        },
        "hello-world": {
            "title": "Hello World",
            "description": "Test your knowledge of the first repository workflow",
            "questions": [
                {
                    "id": "hw1",
                    "question": "Name the steps to create a branch and open a pull request.",
                    "options": [
                        "Just click merge",
                        "Create branch from main, edit a file, commit, open PR comparing your branch to main, then merge",
                        "Type special commands",
                        "Delete everything first"
                    ],
                    "correct": 1,
                    "explanation": "The correct workflow is: create a branch from main, make your changes, commit them, then open a pull request to propose merging your branch into main."
                },
                {
                    "id": "hw2",
                    "question": "What does 'merge' do in simple terms?",
                    "options": [
                        "Deletes your work",
                        "Integrates changes from one branch into another",
                        "Creates a new repository",
                        "Uploads to the internet"
                    ],
                    "correct": 1,
                    "explanation": "Merge integrates changes from one branch into another, combining the work from both branches."
                },
                {
                    "id": "hw3",
                    "question": "What are conflict markers, and how do you resolve a simple conflict?",
                    "options": [
                        "They are decoration",
                        "They show where lines clash; resolve by choosing one version and removing markers",
                        "They mean you did something wrong",
                        "Ignore them and continue"
                    ],
                    "correct": 1,
                    "explanation": "Conflict markers show where lines clash in different ways. You resolve them by choosing which version to keep and removing the conflict markers."
                }
            ]
        },
        "command-line": {
            "title": "Command Line", 
            "description": "Test your understanding of Git commands",
            "questions": [
                {
                    "id": "cl1",
                    "question": "What does `git init` do?",
                    "options": [
                        "Downloads files from the internet",
                        "Starts a new local repository",
                        "Creates a website",
                        "Deletes everything"
                    ],
                    "correct": 1,
                    "explanation": "`git init` starts tracking in the current folder, creating a new local Git repository."
                },
                {
                    "id": "cl2",
                    "question": "When do you use `git add`?",
                    "options": [
                        "When you want to download files",
                        "When you want to upload files to GitHub",
                        "When you want to stage changes for commit",
                        "When you want to delete files"
                    ],
                    "correct": 2,
                    "explanation": "`git add` stages changes, putting files into the staging area to prepare them for commit."
                },
                {
                    "id": "cl3",
                    "question": "What does `git push` do?",
                    "options": [
                        "Uploads commits to the remote repository",
                        "Creates a new branch",
                        "Deletes local files",
                        "Downloads files from GitHub"
                    ],
                    "correct": 0,
                    "explanation": "`git push` uploads your commits to the remote repository (like GitHub)."
                },
                {
                    "id": "cl4",
                    "question": "What does `git pull` do?",
                    "options": [
                        "Deletes your changes",
                        "Downloads and merges changes from the remote",
                        "Creates a new repository",
                        "Uploads your changes"
                    ],
                    "correct": 1,
                    "explanation": "`git pull` downloads and merges new changes from the remote repository to keep your local copy up to date."
                }
            ]
        },
        "collaboration": {
            "title": "Collaboration",
            "description": "Test your knowledge of team workflows",
            "questions": [
                {
                    "id": "col1",
                    "question": "Why open a pull request instead of editing `main` directly?",
                    "options": [
                        "You cannot edit main directly",
                        "PRs enable discussion, review, and safer integration",
                        "It is faster",
                        "It is required by law"
                    ],
                    "correct": 1,
                    "explanation": "Pull requests enable discussion, review, and safer integration. They let teammates discuss changes before merging them."
                },
                {
                    "id": "col2",
                    "question": "How do you name branches to keep work clear?",
                    "options": [
                        "Use random names",
                        "Use clear branch names (feature/, bugfix/) to help everyone understand intent",
                        "Only use main",
                        "Use dates only"
                    ],
                    "correct": 1,
                    "explanation": "Clear branch names like `feature/about-page` or `bugfix/typo-title` help everyone understand what the branch is for."
                },
                {
                    "id": "col3", 
                    "question": "What is the value of code review?",
                    "options": [
                        "It is just a formality",
                        "Review catches mistakes and spreads knowledge across the team",
                        "It takes too much time",
                        "It is only for experts"
                    ],
                    "correct": 1,
                    "explanation": "Code review catches mistakes, shares knowledge across the team, and helps everyone learn from each other."
                }
            ]
        },
        "best-practices": {
            "title": "Best Practices",
            "description": "Test your understanding of common mistakes to avoid",
            "questions": [
                {
                    "id": "bp1",
                    "question": "What should you put in `.gitignore`?",
                    "options": [
                        "Everything",
                        "Nothing important",
                        "Temp files, logs, build outputs, and any secrets",
                        "Only image files"
                    ],
                    "correct": 2,
                    "explanation": "`.gitignore` should contain patterns for temp files, logs, build outputs, and any secrets that should not be committed."
                },
                {
                    "id": "bp2",
                    "question": "How can you improve commit messages?",
                    "options": [
                        "Make them longer",
                        "Use emojis only",
                        "Write short, specific messages that explain 'why'",
                        "Use abbreviations only"
                    ],
                    "correct": 2,
                    "explanation": "Good commit messages are short and specific, explaining the why behind the change, not just the 'what'."
                },
                {
                    "id": "bp3",
                    "question": "When is a fork the right choice instead of a branch?",
                    "options": [
                        "When you own the repository",
                        "When you do not have write access to the original repository",
                        "When you want to work alone",
                        "Never use forks"
                    ],
                    "correct": 1,
                    "explanation": "You should fork when you do not have write access to the original repository. You cannot create branches on repositories you do not own."
                }
            ]
        }
    }
    
    # Section selector
    st.markdown("## Choose a Section to Practice")
    
    # Show completed sections
    for section_id, section_data in quiz_sections.items():
        if section_id in st.session_state.quiz_scores:
            score = st.session_state.quiz_scores[section_id]
            st.success(f"✅ {section_data['title']} Quiz - Score: {score}%")
    
    # Select section to take
    section_options = {f"{data['title']} - {data['description']}": section_id 
                      for section_id, data in quiz_sections.items()}
    
    selected_section = st.selectbox("Select a quiz section:", list(section_options.keys()))
    section_id = section_options[selected_section]
    section_data = quiz_sections[section_id]
    
    # Quiz interface
    if 'current_quiz' not in st.session_state:
        st.session_state.current_quiz = None
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    
    # Start quiz
    if st.button("Start Quiz") or st.session_state.current_quiz == section_id:
        if st.session_state.current_quiz != section_id:
            st.session_state.current_quiz = section_id
            st.session_state.current_question_index = 0
            st.session_state.quiz_answers = {}
        
        questions = section_data['questions']
        current_index = st.session_state.current_question_index
        
        if current_index < len(questions):
            question = questions[current_index]
            
            # Progress
            progress = (current_index + 1) / len(questions)
            st.progress(progress)
            st.caption(f"Question {current_index + 1} of {len(questions)}")
            
            # Question
            st.markdown(f"### {question['question']}")
            
            # Answer options
            selected_answer = st.radio("Select your answer:", 
                                     [f"{i+1}. {option}" for i, option in enumerate(question['options'])],
                                     key=f"q_{question['id']}")
            
            if st.button("Submit Answer"):
                answer_index = int(selected_answer.split('.')[0]) - 1
                st.session_state.quiz_answers[question['id']] = answer_index
                
                # Show result
                if answer_index == question['correct']:
                    st.success("✅ Correct! Well done!")
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {question['options'][question['correct']]}")
                
                # Show explanation
                st.info(f"**Explanation:** {question['explanation']}")
                
                # Next question or results
                if current_index < len(questions) - 1:
                    if st.button("Next Question"):
                        st.session_state.current_question_index += 1
                        st.rerun()
                else:
                    if st.button("View Results"):
                        # Calculate score
                        correct_count = sum(1 for q in questions 
                                          if st.session_state.quiz_answers.get(q['id']) == q['correct'])
                        score = (correct_count / len(questions)) * 100
                        
                        st.session_state.quiz_scores[section_id] = score
                        st.session_state.current_quiz = None
                        st.session_state.current_question_index = 0
                        st.rerun()
        else:
            # Quiz completed - show results
            correct_count = sum(1 for q in questions 
                              if st.session_state.quiz_answers.get(q['id']) == q['correct'])
            score = (correct_count / len(questions)) * 100
            
            st.session_state.quiz_scores[section_id] = score
            
            # Results display
            st.markdown("## Quiz Results")
            
            if score >= 80:
                st.balloons()
                st.success(f"🎉 Excellent work! You scored {score:.0f}% ({correct_count}/{len(questions)})")
            elif score >= 60:
                st.success(f"👍 Good job! You scored {score:.0f}% ({correct_count}/{len(questions)})")
            else:
                st.warning(f"📚 Keep practicing! You scored {score:.0f}% ({correct_count}/{len(questions)})")
            
            # Reset quiz
            if st.button("Take Another Quiz"):
                st.session_state.current_quiz = None
                st.session_state.current_question_index = 0
                st.session_state.quiz_answers = {}
                st.rerun()
    
    # Overall progress
    if st.session_state.quiz_scores:
        st.markdown("## Your Overall Progress")
        
        total_sections = len(quiz_sections)
        completed_sections = len(st.session_state.quiz_scores)
        average_score = sum(st.session_state.quiz_scores.values()) / completed_sections if completed_sections > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average Score", f"{average_score:.0f}%")
        with col2:
            st.metric("Sections Completed", f"{completed_sections}/{total_sections}")
        with col3:
            perfect_scores = sum(1 for score in st.session_state.quiz_scores.values() if score == 100)
            st.metric("Perfect Scores", perfect_scores)
    
    # Mark as complete if all sections passed
    if st.session_state.quiz_scores and len(st.session_state.quiz_scores) == len(quiz_sections):
        avg_score = sum(st.session_state.quiz_scores.values()) / len(quiz_sections)
        if avg_score >= 70:
            if st.button("✅ Complete Practice & Mastery", use_container_width=True):
                st.session_state.completed_pages.add("Practice")
                st.balloons()
                st.success("🎯 Fantastic! You've mastered all the concepts. Ready to reference materials?")

def quick_reference_page():
    """Quick Reference - Command cheat sheets and reference materials"""
    display_header("Quick Reference", "Essential Git commands and concepts at a glance", "📚")
    
    st.markdown("Keep this handy while you practice.")
    
    # Master cheat sheet
    st.markdown("## Git/GitHub Cheat Sheet")
    
    cheat_sheet_data = [
        ("Repository", "Project home for files and history", "Start a new project", "—"),
        ("Commit", "Saved checkpoint with a message", "After making focused changes", "git commit -m \"Add bio\""),
        ("Branch", "Parallel workspace", "Try features or fixes safely", "git checkout -b feature/about-page"),
        ("Pull Request", "Proposal to merge with review", "Collaborate and review", "PR: Add bio section"),
        ("Merge", "Integrate changes", "After review, into main", "Merge PR #3"),
        ("Clone", "Download a repo to your computer", "Work locally on an existing project", "—"),
        ("Fork", "Your own copy of someone else project", "Contribute to projects you do not own", "—"),
        ("Remote", "The online repo (origin)", "Push/pull to stay in sync", "git push -u origin main"),
        ("git init", "Start a new local repo", "Create a new project", "—"),
        ("git status", "See current changes", "Before/after edits", "—"),
        ("git add", "Stage changes", "Prepare to commit", "git add readme.md"),
        ("git commit", "Save staged changes", "Record a focused update", "git commit -m \"Fix typo\""),
        ("git push", "Upload to remote", "Share work, open PR", "git push origin feature/about-page"),
        ("git pull", "Download and merge", "Sync with teammates", "git pull"),
        ("git log", "View history", "Review past commits", "—"),
        (".gitignore", "File listing what Git should ignore", "Keep sensitive/temp files out", "Add *.log and node_modules/")
    ]
    
    # Desktop table view
    st.markdown("### Complete Reference Table")
    
    # Create DataFrame for better display
    df = pd.DataFrame(cheat_sheet_data, 
                     columns=["Term/Command", "What it does", "When to use it", "Example"])
    
    st.dataframe(df, use_container_width=True)
    
    # Common workflows
    st.markdown("## Common Workflows")
    
    workflows = [
        ("Starting a New Project", [
            "git init",
            "git add .",
            "git commit -m \"Initial commit\"",
            "git push origin main"
        ]),
        ("Working on a Feature", [
            "git checkout -b feature/new-feature",
            "git add filename",
            "git commit -m \"Add new feature\"",
            "git push origin feature/new-feature"
        ]),
        ("Updating from Remote", [
            "git pull origin main",
            "git checkout main",
            "git merge feature/new-feature",
            "git push origin main"
        ])
    ]
    
    cols = st.columns(3)
    for i, (workflow_name, steps) in enumerate(workflows):
        with cols[i]:
            st.markdown(f"### {workflow_name}")
            for j, step in enumerate(steps, 1):
                st.markdown(f"{j}. `{step}`")
    
    # Additional resources
    st.markdown("## Additional Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Official GitHub Cheat Sheet
        Official GitHub Education cheat sheet with comprehensive command reference
        """)
        st.link_button("📥 Download PDF", 
                      "https://education.github.com/git-cheat-sheet-education.pdf",
                      use_container_width=True)
    
    with col2:
        st.markdown("""
        ### GitHub Documentation
        Comprehensive documentation for all GitHub features and workflows
        """)
        st.link_button("📖 View Docs", 
                      "https://docs.github.com",
                      use_container_width=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4>💡 Pro Tip</h4>
        <p>Build a habit of writing clear messages and checking <code>git status</code> often; these two habits will carry you far.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Quick Command Lookup")
    
    # Quick search
    search_term = st.text_input("Search for a command or concept:", placeholder="Type to search...")
    
    if search_term:
        search_results = [item for item in cheat_sheet_data 
                         if search_term.lower() in item[0].lower() or 
                            search_term.lower() in item[1].lower() or
                            search_term.lower() in item[2].lower()]
        
        if search_results:
            st.markdown(f"**Search results for '{search_term}':**")
            for term, meaning, when, example in search_results:
                st.markdown(f"- **{term}**: {meaning}")
        else:
            st.info(f"No results found for '{search_term}'")
    
    # Most common commands highlight
    st.markdown("## Most Commonly Used Commands")
    
    common_commands = [
        ("git status", "Check what's changed", "Use before and after every edit"),
        ("git add .", "Stage all changes", "Get ready to commit"),
        ("git commit -m \"message\"", "Save your work", "Create a checkpoint"),
        ("git push", "Upload to GitHub", "Share with others"),
        ("git pull", "Get latest changes", "Stay up to date")
    ]
    
    for cmd, purpose, when in common_commands:
        col1, col2, col3 = st.columns([2, 2, 3])
        with col1:
            st.code(cmd, language='bash')
        with col2:
            st.caption(f"**Purpose:** {purpose}")
        with col3:
            st.caption(f"**When:** {when}")

def resources_page():
    """Resources - External links and learning paths"""
    display_header("Learning Resources", "Continue your GitHub learning journey", "📖")
    
    st.markdown("Practice tools, official courses, and real-world applications to deepen your understanding.")
    
    # Visual learning aids and practice tools
    st.markdown("## Visual Learning Aids and Practice Tools")
    st.markdown("Visualization accelerates understanding, especially for branching and merging. Use the tools below for 10–15 minute practice bursts.")
    
    practice_tools = [
        ("Learn Git Branching", "Interactive levels for branching and merging concepts", "https://learngitbranching.js.org/", "🎮"),
        ("Visualizing Git", "See how commits, branches, and history evolve over time", "https://git-school.github.io/visualizing-git/#rewritten-history", "📊"),
        ("Git-it (Challenges)", "Hands-on Git and GitHub challenges for real practice", "https://github.com/jlord/git-it-electron", "🔧")
    ]
    
    cols = st.columns(3)
    for name, description, link, icon in practice_tools:
        with cols[practice_tools.index((name, description, link, icon))]:
            st.markdown(f"""
            <div style='background: white; border-radius: 15px; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 300px; display: flex; flex-direction: column;'>
                <div style='font-size: 3rem; margin-bottom: 1rem; text-align: center;'>{icon}</div>
                <h3 style='color: #2c3e50; text-align: center; margin-bottom: 1rem;'>{name}</h3>
                <p style='color: #6c757d; text-align: center; flex-grow: 1;'>{description}</p>
                <div style='text-align: center; margin-top: 1rem;'>
                    <a href='{link}' target='_blank' style='background: #3498db; color: white; padding: 0.5rem 1rem; border-radius: 8px; text-decoration: none; font-weight: bold;'>Try it now</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4>💡 Pro Tip:</h4>
        <p>These resources are optional but highly recommended. If your teacher assigns them, treat them like mini-levels in a game: read the goal, try, observe the result, and iterate.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Official resources
    st.markdown("## Official Learning Resources")
    st.markdown("Structured courses and comprehensive documentation to deepen your understanding.")
    
    official_resources = [
        ("GitHub Skills", "Official GitHub beginner course with hands-on exercises", "https://skills.github.com/", "Course"),
        ("Introduction to GitHub", "Structured practice course covering fundamentals", "https://github.com/skills/introduction-to-github", "Course"),
        ("GitHub Docs", "Complete documentation and reference materials", "https://docs.github.com", "Documentation")
    ]
    
    for name, description, link, resource_type in official_resources:
        st.markdown(f"""
        <div style='background: white; border-left: 4px solid #3498db; border-radius: 10px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
            <div style='display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;'>
                <h3 style='color: #2c3e50; margin: 0;'>{name}</h3>
                <span style='background: #3498db; color: white; padding: 0.3rem 0.6rem; border-radius: 20px; font-size: 0.8rem;'>{resource_type}</span>
            </div>
            <p style='color: #6c757d; margin-bottom: 1rem;'>{description}</p>
            <a href='{link}' target='_blank' style='color: #3498db; font-weight: bold; text-decoration: none;'>Get Started →</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Learning path
    st.markdown("## Your Learning Path")
    st.markdown("Follow this structured approach to master GitHub step by step.")
    
    learning_path = [
        ("Set Foundation", "Complete this tutorial and practice with simple repositories", "Week 1-2", "Start Learning"),
        ("Build Skills", "Work through GitHub Skills courses and practice tools", "Week 3-4", "Practice"),
        ("Apply Knowledge", "Apply what you have learned by building something you care about", "Ongoing", "Create Project")
    ]
    
    for i, (title, description, timeframe, action) in enumerate(learning_path, 1):
        st.markdown(f"""
        <div class='step-container'>
            <div style='display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;'>
                <div style='display: flex; align-items: center; gap: 1rem;'>
                    <div style='background: #3498db; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.2rem;'>{i}</div>
                    <div>
                        <h3 style='color: #2c3e50; margin: 0;'>{title}</h3>
                        <p style='color: #3498db; margin: 0; font-size: 0.9rem; font-weight: bold;'>{timeframe}</p>
                    </div>
                </div>
                <button style='background: #3498db; color: white; padding: 0.5rem 1rem; border: none; border-radius: 8px; font-weight: bold;'>{action}</button>
            </div>
            <p style='color: #6c757d; margin: 0; padding-left: 3rem;'>{description}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key references
    st.markdown("## Key References")
    st.markdown("Important articles and guides that support this tutorial.")
    
    references = [
        ("What is Git? Beginner Guide", "GitHub blog explanation of version control fundamentals", "https://github.blog/developer-skills/programming-languages-and-frameworks/what-is-git-our-beginners-guide-to-version-control/"),
        ("Hello World Tutorial", "Official GitHub quickstart guide", "https://docs.github.com/get-started/quickstart/hello-world"),
        ("Git Cheat Sheet", "Comprehensive command reference for students", "https://education.github.com/git-cheat-sheet-education.pdf")
    ]
    
    for title, description, link in references:
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 1.5rem; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h4 style='color: #2c3e50; margin-bottom: 0.5rem;'>{title}</h4>
                <p style='color: #6c757d; margin: 0;'>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.link_button("Read", link)
    
    # Next steps
    st.markdown("## What Comes Next")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 15px; margin: 2rem 0;'>
        <h2 style='margin-bottom: 1rem;'>🚀 Ready for the Next Level?</h2>
        <p style='font-size: 1.1rem; margin-bottom: 1.5rem; line-height: 1.6;'>
            After you are comfortable with repos, commits, branches, pull requests, and `.gitignore`, 
            you can level up by exploring GitHub Skills courses, building multi-branch projects, 
            and creating a public portfolio of your work.
        </p>
        <div style='background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px;'>
            <p style='margin: 0; font-size: 1.1rem;'>
                <strong>Key to steady progress:</strong> Small, frequent practice. Set a goal like 
                "one repository, one branch, one PR per week," and keep your messages short and honest. 
                Over time, your repository history will become a record of growth you can be proud of.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Celebration for completing all content
    if len(st.session_state.completed_pages) >= 8:  # Most of the tutorial
        st.balloons()
        st.success("🎉 Congratulations! You've completed most of the tutorial. You're well on your way to mastering GitHub!")

def main():
    """Main application"""
    initialize_session_state()
    
    # Sidebar navigation
    st.sidebar.markdown("# 📚 GitHub Tutorial")
    st.sidebar.markdown("### Complete Learning Path")
    
    pages = {
        "🏠 Home": "Home",
        "🚀 Getting Started": "Getting Started", 
        "🧠 Core Concepts": "Core Concepts",
        "🏗️ First Repository": "First Repository",
        "⌨️ Command Line": "Command Line",
        "👥 Collaboration": "Collaboration",
        "⭐ Best Practices": "Best Practices",
        "🚀 Real Projects": "Real Projects",
        "🎯 Practice Quiz": "Practice",
        "📚 Quick Reference": "Quick Reference",
        "📖 Resources": "Resources"
    }
    
    # Current page indicator
    st.sidebar.markdown("### Progress")
    completed_count = len(st.session_state.completed_pages)
    total_pages = len(pages)
    progress = (completed_count / total_pages) * 100
    st.sidebar.progress(progress / 100)
    st.sidebar.caption(f"{completed_count}/{total_pages} pages completed ({progress:.0f}%)")
    
    # Navigation
    selected_page = st.sidebar.radio("Navigate to:", list(pages.keys()))
    st.session_state.current_page = pages[selected_page]
    
    # Page content
    if st.session_state.current_page == "Home":
        home_page()
    elif st.session_state.current_page == "Getting Started":
        getting_started_page()
    elif st.session_state.current_page == "Core Concepts":
        core_concepts_page()
    elif st.session_state.current_page == "First Repository":
        first_repository_page()
    elif st.session_state.current_page == "Command Line":
        command_line_page()
    elif st.session_state.current_page == "Collaboration":
        collaboration_page()
    elif st.session_state.current_page == "Best Practices":
        best_practices_page()
    elif st.session_state.current_page == "Real Projects":
        real_projects_page()
    elif st.session_state.current_page == "Practice":
        practice_page()
    elif st.session_state.current_page == "Quick Reference":
        quick_reference_page()
    elif st.session_state.current_page == "Resources":
        resources_page()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Built with ❤️ for 9th grade students**")
    st.sidebar.markdown("Interactive GitHub learning experience")

if __name__ == "__main__":
    main()