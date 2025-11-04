"""
Streamlit Interactive Features Implementation
Complete conversion of React interactive features to Streamlit components
"""

import streamlit as st
import time
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json

# Configure Streamlit page
st.set_page_config(
    page_title="GitHub Tutorial - Interactive Features",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for interactive features
def initialize_interactive_features():
    """Initialize all session state variables for interactive features"""
    
    if 'interactive_progress' not in st.session_state:
        st.session_state.interactive_progress = {
            'pages': {},
            'overall_progress': 0,
            'total_pages': 11,
            'current_page': 'home',
            'started_at': datetime.now().isoformat(),
            'last_activity': datetime.now().isoformat(),
            'quiz_scores': {},
            'time_spent': {},
            'sections_completed': set(),
            'current_streak': 0,
            'total_questions_answered': 0,
            'correct_answers': 0
        }
    
    if 'interactive_achievements' not in st.session_state:
        st.session_state.interactive_achievements = {
            'first_steps': {'unlocked': False, 'unlocked_at': None},
            'setup_master': {'unlocked': False, 'unlocked_at': None},
            'concept_explorer': {'unlocked': False, 'unlocked_at': None},
            'repository_creator': {'unlocked': False, 'unlocked_at': None},
            'command_line_pro': {'unlocked': False, 'unlocked_at': None},
            'team_player': {'unlocked': False, 'unlocked_at': None},
            'best_practice': {'unlocked': False, 'unlocked_at': None},
            'quiz_master': {'unlocked': False, 'unlocked_at': None},
            'knowledge_seeker': {'unlocked': False, 'unlocked_at': None},
            'complete_journey': {'unlocked': False, 'unlocked_at': None},
            'dedicated_learner': {'unlocked': False, 'unlocked_at': None},
            'project_builder': {'unlocked': False, 'unlocked_at': None},
            'resource_collector': {'unlocked': False, 'unlocked_at': None}
        }
    
    if 'quiz_state' not in st.session_state:
        st.session_state.quiz_state = {
            'current_section': 'core-concepts',
            'current_question': 0,
            'selected_answers': {},
            'show_results': False,
            'quiz_completed': set(),
            'section_scores': {},
            'show_feedback': False,
            'answer_submitted': False,
            'start_time': None,
            'time_per_question': []
        }
    
    if 'visual_guides' not in st.session_state:
        st.session_state.visual_guides = {
            'completed_demos': set(),
            'current_demo': None,
            'demo_progress': {},
            'show_celebration': False,
            'celebration_message': '',
            'celebration_type': 'success'
        }

# Quiz Data - Exactly matching React implementation
QUIZ_SECTIONS = {
    'core-concepts': {
        'id': 'core-concepts',
        'title': 'Core Concepts',
        'description': 'Test your understanding of repositories, commits, and branches',
        'questions': [
            {
                'id': 'cc1',
                'question': 'What is a repository, and how is it like a locker or shared folder?',
                'options': [
                    'A type of computer program',
                    'A single place that holds all your project files and their history',
                    'A website where you post code',
                    'A backup system for your computer'
                ],
                'correct': 1,
                'explanation': 'A repository is the project home that holds files and history, like a shared locker where everyone knows where to find the current files.',
                'section': 'core-concepts'
            },
            {
                'id': 'cc2',
                'question': 'Why are commit messages important? Give a good and a bad example.',
                'options': [
                    'They do not matter much',
                    'They help you and teammates understand what changed; good: "Add bio section", bad: "Fixed stuff"',
                    'They are only for show',
                    'They must be exactly 10 characters long'
                ],
                'correct': 1,
                'explanation': 'Commit messages should be short and descriptive. "Add bio section" is good because it tells you what changed, while "Fixed stuff" is too vague.',
                'section': 'core-concepts'
            },
            {
                'id': 'cc3',
                'question': 'What does a branch let you do, and when should you delete a branch after merging?',
                'options': [
                    'Nothing special',
                    'Work in parallel and merge later; delete after merging to keep repo tidy',
                    'Only for experts',
                    'Create new repositories'
                ],
                'correct': 1,
                'explanation': 'Branches let you work in parallel and merge later. You should delete a branch after merging its changes into main to keep the repository tidy.',
                'section': 'core-concepts'
            }
        ]
    },
    'hello-world': {
        'id': 'hello-world',
        'title': 'Hello World',
        'description': 'Test your knowledge of the first repository workflow',
        'questions': [
            {
                'id': 'hw1',
                'question': 'Name the steps to create a branch and open a pull request.',
                'options': [
                    'Just click merge',
                    'Create branch from main, edit a file, commit, open PR comparing your branch to main, then merge',
                    'Type special commands',
                    'Delete everything first'
                ],
                'correct': 1,
                'explanation': 'The correct workflow is: create a branch from main, make your changes, commit them, then open a pull request to propose merging your branch into main.',
                'section': 'hello-world'
            },
            {
                'id': 'hw2',
                'question': 'What does "merge" do in simple terms?',
                'options': [
                    'Deletes your work',
                    'Integrates changes from one branch into another',
                    'Creates a new repository',
                    'Uploads to the internet'
                ],
                'correct': 1,
                'explanation': 'Merge integrates changes from one branch into another, combining the work from both branches.',
                'section': 'hello-world'
            },
            {
                'id': 'hw3',
                'question': 'What are conflict markers, and how do you resolve a simple conflict?',
                'options': [
                    'They are decoration',
                    'They show where lines clash; resolve by choosing one version and removing markers',
                    'They mean you did something wrong',
                    'Ignore them and continue'
                ],
                'correct': 1,
                'explanation': 'Conflict markers show where lines clash in different ways. You resolve them by choosing which version to keep and removing the conflict markers.',
                'section': 'hello-world'
            }
        ]
    },
    'command-line': {
        'id': 'command-line',
        'title': 'Command Line',
        'description': 'Test your understanding of Git commands',
        'questions': [
            {
                'id': 'cl1',
                'question': 'What does `git init` do?',
                'options': [
                    'Downloads files from the internet',
                    'Starts a new local repository',
                    'Creates a website',
                    'Deletes everything'
                ],
                'correct': 1,
                'explanation': '`git init` starts tracking in the current folder, creating a new local Git repository.',
                'section': 'command-line'
            },
            {
                'id': 'cl2',
                'question': 'When do you use `git add`?',
                'options': [
                    'When you want to download files',
                    'When you want to upload files to GitHub',
                    'When you want to stage changes for commit',
                    'When you want to delete files'
                ],
                'correct': 2,
                'explanation': '`git add` stages changes, putting files into the staging area to prepare them for commit.',
                'section': 'command-line'
            },
            {
                'id': 'cl3',
                'question': 'What does `git push` do?',
                'options': [
                    'Uploads commits to the remote repository',
                    'Creates a new branch',
                    'Deletes local files',
                    'Downloads files from GitHub'
                ],
                'correct': 0,
                'explanation': '`git push` uploads your commits to the remote repository (like GitHub).',
                'section': 'command-line'
            },
            {
                'id': 'cl4',
                'question': 'What does `git pull` do?',
                'options': [
                    'Deletes your changes',
                    'Downloads and merges changes from the remote',
                    'Creates a new repository',
                    'Uploads your changes'
                ],
                'correct': 1,
                'explanation': '`git pull` downloads and merges new changes from the remote repository to keep your local copy up to date.',
                'section': 'command-line'
            }
        ]
    },
    'collaboration': {
        'id': 'collaboration',
        'title': 'Collaboration',
        'description': 'Test your knowledge of team workflows',
        'questions': [
            {
                'id': 'col1',
                'question': 'Why open a pull request instead of editing `main` directly?',
                'options': [
                    'You cannot edit main directly',
                    'PRs enable discussion, review, and safer integration',
                    'It is faster',
                    'It is required by law'
                ],
                'correct': 1,
                'explanation': 'Pull requests enable discussion, review, and safer integration. They let teammates discuss changes before merging them.',
                'section': 'collaboration'
            },
            {
                'id': 'col2',
                'question': 'How do you name branches to keep work clear?',
                'options': [
                    'Use random names',
                    'Use clear branch names (feature/, bugfix/) to help everyone understand intent',
                    'Only use main',
                    'Use dates only'
                ],
                'correct': 1,
                'explanation': 'Clear branch names like `feature/about-page` or `bugfix/typo-title` help everyone understand what the branch is for.',
                'section': 'collaboration'
            },
            {
                'id': 'col3',
                'question': 'What is the value of code review?',
                'options': [
                    'It is just a formality',
                    'Review catches mistakes and spreads knowledge across the team',
                    'It takes too much time',
                    'It is only for experts'
                ],
                'correct': 1,
                'explanation': 'Code review catches mistakes, shares knowledge across the team, and helps everyone learn from each other.',
                'section': 'collaboration'
            }
        ]
    },
    'best-practices': {
        'id': 'best-practices',
        'title': 'Best Practices',
        'description': 'Test your understanding of common mistakes to avoid',
        'questions': [
            {
                'id': 'bp1',
                'question': 'What should you put in `.gitignore`?',
                'options': [
                    'Everything',
                    'Nothing important',
                    'Temp files, logs, build outputs, and any secrets',
                    'Only image files'
                ],
                'correct': 2,
                'explanation': '`.gitignore` should contain patterns for temp files, logs, build outputs, and any secrets that should not be committed.',
                'section': 'best-practices'
            },
            {
                'id': 'bp2',
                'question': 'How can you improve commit messages?',
                'options': [
                    'Make them longer',
                    'Use emojis only',
                    'Write short, specific messages that explain "why"',
                    'Use abbreviations only'
                ],
                'correct': 2,
                'explanation': 'Good commit messages are short and specific, explaining the why behind the change, not just the "what".',
                'section': 'best-practices'
            },
            {
                'id': 'bp3',
                'question': 'When is a fork the right choice instead of a branch?',
                'options': [
                    'When you own the repository',
                    'When you do not have write access to the original repository',
                    'When you want to work alone',
                    'Never use forks'
                ],
                'correct': 1,
                'explanation': 'You should fork when you do not have write access to the original repository. You cannot create branches on repositories you do not own.',
                'section': 'best-practices'
            }
        ]
    }
}

# Achievement definitions matching React implementation
ACHIEVEMENT_DEFINITIONS = {
    'first_steps': {
        'title': 'First Steps',
        'description': 'Complete your first lesson',
        'icon': '🐾',
        'category': 'completion',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'setup_master': {
        'title': 'Setup Master',
        'description': 'Complete the Getting Started section',
        'icon': '⚙️',
        'category': 'completion',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'concept_explorer': {
        'title': 'Concept Explorer',
        'description': 'Learn all core GitHub concepts',
        'icon': '🧠',
        'category': 'exploration',
        'requirement': {'type': 'pages_completed', 'value': 3}
    },
    'repository_creator': {
        'title': 'Repository Creator',
        'description': 'Create your first repository',
        'icon': '📁',
        'category': 'completion',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'command_line_pro': {
        'title': 'Command Line Pro',
        'description': 'Master the command line basics',
        'icon': '💻',
        'category': 'completion',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'team_player': {
        'title': 'Team Player',
        'description': 'Learn about collaboration',
        'icon': '🤝',
        'category': 'exploration',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'best_practice': {
        'title': 'Best Practice',
        'description': 'Learn GitHub best practices',
        'icon': '✨',
        'category': 'completion',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'quiz_master': {
        'title': 'Quiz Master',
        'description': 'Score 100% on a quiz',
        'icon': '🏆',
        'category': 'mastery',
        'requirement': {'type': 'quiz_score', 'value': 100}
    },
    'knowledge_seeker': {
        'title': 'Knowledge Seeker',
        'description': 'Score 80% or higher on all quizzes',
        'icon': '📚',
        'category': 'mastery',
        'requirement': {'type': 'quiz_score', 'value': 80}
    },
    'complete_journey': {
        'title': 'Complete Journey',
        'description': 'Finish all lessons',
        'icon': '⭐',
        'category': 'completion',
        'requirement': {'type': 'pages_completed', 'value': 9}
    },
    'dedicated_learner': {
        'title': 'Dedicated Learner',
        'description': 'Spend 30 minutes learning',
        'icon': '⏰',
        'category': 'speed',
        'requirement': {'type': 'time_spent', 'value': 30}
    },
    'project_builder': {
        'title': 'Project Builder',
        'description': 'Explore real project ideas',
        'icon': '🔨',
        'category': 'exploration',
        'requirement': {'type': 'pages_completed', 'value': 1}
    },
    'resource_collector': {
        'title': 'Resource Collector',
        'description': 'Explore all resources',
        'icon': '📖',
        'category': 'exploration',
        'requirement': {'type': 'pages_completed', 'value': 1}
    }
}

class InteractiveFeatures:
    """Main class for managing all interactive features"""
    
    def __init__(self):
        initialize_interactive_features()
    
    def render_dashboard(self):
        """Render the main interactive dashboard"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 1rem; margin-bottom: 2rem; color: white; text-align: center;">
            <h1>🐙 GitHub Tutorial - Interactive Features</h1>
            <p style="font-size: 1.2rem; margin: 0;">Master GitHub with hands-on interactive learning!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            progress = st.session_state.interactive_progress
            completed_pages = len([p for p in progress['pages'].values() if p.get('completed', False)])
            st.metric(
                "Overall Progress", 
                f"{progress['overall_progress']}%",
                f"{completed_pages}/{progress['total_pages']} lessons"
            )
        
        with col2:
            unlocked_count = len([a for a in st.session_state.interactive_achievements.values() if a['unlocked']])
            total_achievements = len(st.session_state.interactive_achievements)
            st.metric("🏆 Achievements", f"{unlocked_count}/{total_achievements}")
        
        with col3:
            total_quiz_questions = sum(len(section['questions']) for section in QUIZ_SECTIONS.values())
            st.metric("📝 Quiz Progress", 
                     f"{progress['total_questions_answered']}/{total_quiz_questions} questions")
        
        with col4:
            if progress['total_questions_answered'] > 0:
                accuracy = int((progress['correct_answers'] / progress['total_questions_answered']) * 100)
                st.metric("🎯 Accuracy", f"{accuracy}%")
            else:
                st.metric("🎯 Accuracy", "0%")
    
    def render_interactive_quiz(self):
        """Render the complete interactive quiz system"""
        st.markdown("## 📝 Interactive Quiz System")
        st.markdown("Test your knowledge with 16 questions across 5 sections")
        
        # Quiz section selector
        col1, col2 = st.columns([2, 1])
        
        with col1:
            section_options = [f"{section['title']} ({len(section['questions'])} questions)" 
                             for section in QUIZ_SECTIONS.values()]
            selected_section_display = st.selectbox(
                "Choose a quiz section:",
                section_options,
                key="quiz_section_selector"
            )
            
            # Find selected section
            selected_section_key = None
            for key, section in QUIZ_SECTIONS.items():
                if f"{section['title']} ({len(section['questions'])} questions)" == selected_section_display:
                    selected_section_key = key
                    break
        
        with col2:
            if st.button("🔄 Reset Current Quiz", use_container_width=True):
                self.reset_quiz_session()
        
        if selected_section_key:
            self.render_quiz_section(selected_section_key)
    
    def render_quiz_section(self, section_key: str):
        """Render a specific quiz section"""
        section = QUIZ_SECTIONS[section_key]
        quiz_state = st.session_state.quiz_state
        
        st.markdown(f"### {section['title']} Quiz")
        st.markdown(f"**{section['description']}**")
        
        current_question_idx = quiz_state['current_question']
        total_questions = len(section['questions'])
        
        # Progress indicator
        progress_col1, progress_col2 = st.columns([3, 1])
        with progress_col1:
            progress_bar = st.progress((current_question_idx + 1) / total_questions)
        with progress_col2:
            st.markdown(f"**{current_question_idx + 1}/{total_questions}**")
        
        if current_question_idx < total_questions:
            self.render_quiz_question(section_key, current_question_idx)
        else:
            self.render_quiz_results(section_key)
    
    def render_quiz_question(self, section_key: str, question_idx: int):
        """Render a single quiz question with interactive features"""
        section = QUIZ_SECTIONS[section_key]
        question = section['questions'][question_idx]
        quiz_state = st.session_state.quiz_state
        
        question_id = f"{section_key}_{question_idx}"
        
        st.markdown(f"**{question['question']}**")
        
        # Answer options with custom styling
        selected_option = st.radio(
            "Select your answer:",
            question['options'],
            key=f"answer_{question_id}",
            index=None
        )
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("✅ Submit Answer", disabled=selected_option is None, use_container_width=True):
                if selected_option is not None:
                    self.submit_answer(section_key, question_idx, question['options'].index(selected_option))
        
        with col2:
            if st.button("⏭️ Skip Question", use_container_width=True):
                self.skip_question(section_key)
        
        # Show feedback if answer was submitted
        if quiz_state.get('show_feedback', False) and quiz_state.get('current_question') == question_idx:
            self.render_feedback(question, question_idx)
            
            if st.button("➡️ Next Question", use_container_width=True):
                self.next_question(section_key)
    
    def render_feedback(self, question: Dict, question_idx: int):
        """Render immediate feedback for quiz answers"""
        quiz_state = st.session_state.quiz_state
        selected_answer = quiz_state['selected_answers'].get(f"{st.session_state.quiz_state['current_section']}_{question_idx}")
        
        if selected_answer is not None:
            is_correct = selected_answer == question['correct']
            
            if is_correct:
                st.success("🎉 Correct! Great job!")
            else:
                st.error("❌ Not quite right.")
            
            st.info(f"**Explanation:** {question['explanation']}")
    
    def render_quiz_results(self, section_key: str):
        """Render comprehensive quiz results with achievements"""
        section = QUIZ_SECTIONS[section_key]
        quiz_state = st.session_state.quiz_state
        
        # Calculate results
        correct_answers = 0
        for i, question in enumerate(section['questions']):
            if quiz_state['selected_answers'].get(f"{section_key}_{i}") == question['correct']:
                correct_answers += 1
        
        score_percentage = int((correct_answers / len(section['questions'])) * 100)
        
        # Results display
        st.markdown("### 🎯 Quiz Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Score", f"{score_percentage}%", f"{correct_answers}/{len(section['questions'])} correct")
        
        with col2:
            # Determine performance level
            if score_percentage >= 90:
                performance = "🏆 Excellent!"
                color = "green"
            elif score_percentage >= 80:
                performance = "👍 Great Job!"
                color = "blue"
            elif score_percentage >= 70:
                performance = "💪 Good Effort!"
                color = "orange"
            else:
                performance = "📚 Keep Learning!"
                color = "red"
            
            st.metric("Performance", performance)
        
        with col3:
            time_taken = len(quiz_state.get('time_per_question', []))
            st.metric("Time Spent", f"{time_taken} min" if time_taken > 0 else "Quick!")
        
        # Detailed results
        st.markdown("### 📊 Detailed Results")
        
        for i, question in enumerate(section['questions']):
            user_answer = quiz_state['selected_answers'].get(f"{section_key}_{i}")
            is_correct = user_answer == question['correct']
            
            if is_correct:
                st.success(f"✅ **Q{i+1}:** {question['question']}")
            else:
                st.error(f"❌ **Q{i+1}:** {question['question']}")
                if user_answer is not None:
                    st.markdown(f"   Your answer: {question['options'][user_answer]}")
                st.markdown(f"   Correct answer: {question['options'][question['correct']]}")
        
        # Save quiz score and check achievements
        self.save_quiz_score(section_key, score_percentage, correct_answers, len(section['questions']))
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Retake Quiz", use_container_width=True):
                self.reset_quiz_section(section_key)
        
        with col2:
            if st.button("📝 Different Section", use_container_width=True):
                self.reset_quiz_session()
                st.rerun()
        
        with col3:
            if st.button("✅ Mark Section Complete", use_container_width=True):
                self.mark_section_complete(section_key)
    
    def render_achievement_system(self):
        """Render the complete achievement system with badges and celebrations"""
        st.markdown("## 🏆 Achievement System")
        
        achievements = st.session_state.interactive_achievements
        
        # Achievement categories
        categories = {
            'completion': '✅ Completion',
            'mastery': '🎯 Mastery', 
            'exploration': '🔍 Exploration',
            'speed': '⚡ Speed'
        }
        
        for category_key, category_name in categories.items():
            st.markdown(f"### {category_name}")
            
            # Filter achievements by category
            category_achievements = {
                key: achievement for key, achievement in ACHIEVEMENT_DEFINITIONS.items()
                if achievement['category'] == category_key
            }
            
            # Render achievements in a grid
            cols = st.columns(3)
            col_idx = 0
            
            for achievement_id, achievement_def in category_achievements.items():
                with cols[col_idx % 3]:
                    user_achievement = achievements.get(achievement_id, {'unlocked': False, 'unlocked_at': None})
                    
                    if user_achievement['unlocked']:
                        # Unlocked achievement with celebration styling
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                                    padding: 1rem; border-radius: 0.5rem; color: white; text-align: center;
                                    border: 2px solid #FFD700; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{achievement_def['icon']}</div>
                            <h4 style="margin: 0; color: white;">{achievement_def['title']}</h4>
                            <p style="margin: 0.5rem 0; font-size: 0.9rem; color: #f0f0f0;">{achievement_def['description']}</p>
                            <small style="color: #FFD700;">🏅 Unlocked!</small>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        # Locked achievement
                        st.markdown(f"""
                        <div style="background: #f5f5f5; padding: 1rem; border-radius: 0.5rem; 
                                    text-align: center; border: 2px dashed #ccc;">
                            <div style="font-size: 2rem; margin-bottom: 0.5rem; opacity: 0.5;">🔒</div>
                            <h4 style="margin: 0; color: #666;">{achievement_def['title']}</h4>
                            <p style="margin: 0.5rem 0; font-size: 0.9rem; color: #888;">{achievement_def['description']}</p>
                            <small style="color: #999;">Locked</small>
                        </div>
                        """, unsafe_allow_html=True)
                
                col_idx += 1
        
        # Achievement statistics
        st.markdown("### 📊 Achievement Statistics")
        
        total_achievements = len(achievements)
        unlocked_achievements = len([a for a in achievements.values() if a['unlocked']])
        completion_percentage = int((unlocked_achievements / total_achievements) * 100)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Achievements", total_achievements)
        with col2:
            st.metric("Unlocked", unlocked_achievements)
        with col3:
            st.metric("Completion", f"{completion_percentage}%")
        with col4:
            if unlocked_achievements > 0:
                recent_achievement = next(
                    (a for a in achievements.values() if a['unlocked'] and a['unlocked_at']), 
                    None
                )
                if recent_achievement:
                    st.metric("Latest Unlock", recent_achievement['unlocked_at'][:10])
                else:
                    st.metric("Latest Unlock", "N/A")
            else:
                st.metric("Latest Unlock", "N/A")
    
    def render_visual_guides(self):
        """Render interactive step-by-step visual guides and demonstrations"""
        st.markdown("## 🎬 Visual Step-by-Step Guides")
        st.markdown("Interactive demonstrations to help you learn GitHub workflows")
        
        # Guide categories
        guides = {
            'repository_creation': {
                'title': 'Creating Your First Repository',
                'description': 'Learn how to create and set up a new repository',
                'steps': [
                    {'title': 'Sign in to GitHub', 'content': 'Go to github.com and sign in to your account', 'icon': '🔐'},
                    {'title': 'Click New Repository', 'content': 'Click the green "New" button or the "+" icon in the top right', 'icon': '➕'},
                    {'title': 'Name Your Repository', 'content': 'Enter a descriptive name like "my-first-repo"', 'icon': '📝'},
                    {'title': 'Add Description', 'content': 'Write a brief description of your project', 'icon': '📄'},
                    {'title': 'Choose Visibility', 'content': 'Select Public (others can see) or Private', 'icon': '👁️'},
                    {'title': 'Initialize Repository', 'content': 'Check "Add a README file" to start with documentation', 'icon': '📖'},
                    {'title': 'Create Repository', 'content': 'Click "Create repository" to finish setup', 'icon': '🎉'}
                ]
            },
            'git_workflow': {
                'title': 'Basic Git Workflow',
                'description': 'Learn the essential Git commands for version control',
                'steps': [
                    {'title': 'Open Terminal', 'content': 'Open your command line interface (Terminal, Command Prompt, or Git Bash)', 'icon': '💻'},
                    {'title': 'Navigate to Project', 'content': 'Use `cd` command to navigate to your project folder', 'icon': '📁'},
                    {'title': 'Initialize Git', 'content': 'Run `git init` to start tracking your project', 'icon': '🚀'},
                    {'title': 'Check Status', 'content': 'Use `git status` to see what files have changed', 'icon': '📊'},
                    {'title': 'Stage Changes', 'content': 'Run `git add .` to stage all your changes', 'icon': '✅'},
                    {'title': 'Commit Changes', 'content': 'Use `git commit -m "Your message"` to save changes', 'icon': '💾'},
                    {'title': 'Push to GitHub', 'content': 'Use `git push` to upload your changes to GitHub', 'icon': '☁️'}
                ]
            },
            'branch_workflow': {
                'title': 'Branch and Pull Request Workflow',
                'description': 'Learn how to work with branches and create pull requests',
                'steps': [
                    {'title': 'Create New Branch', 'content': 'Use `git checkout -b feature/new-feature` to create a new branch', 'icon': '🌿'},
                    {'title': 'Make Changes', 'content': 'Edit your files to implement the new feature', 'icon': '✏️'},
                    {'title': 'Stage and Commit', 'content': 'Stage and commit your changes with `git add .` and `git commit`', 'icon': '💾'},
                    {'title': 'Push Branch', 'content': 'Use `git push origin feature/new-feature` to push your branch', 'icon': '☁️'},
                    {'title': 'Open Pull Request', 'content': 'Go to GitHub and click "Pull requests" → "New pull request"', 'icon': '🔄'},
                    {'title': 'Review Process', 'content': 'Wait for team members to review your changes', 'icon': '👀'},
                    {'title': 'Merge and Delete', 'content': 'Once approved, merge the PR and delete the feature branch', 'icon': '✅'}
                ]
            }
        }
        
        # Guide selector
        guide_options = [f"{guide['title']} - {guide['description']}" for guide in guides.values()]
        selected_guide = st.selectbox("Choose a visual guide:", guide_options)
        
        # Find selected guide
        selected_guide_key = None
        for key, guide in guides.items():
            if f"{guide['title']} - {guide['description']}" == selected_guide:
                selected_guide_key = key
                break
        
        if selected_guide_key:
            self.render_guide_steps(guides[selected_guide_key])
    
    def render_guide_steps(self, guide: Dict):
        """Render individual steps of a visual guide"""
        steps = guide['steps']
        
        # Progress tracking
        if 'current_step' not in st.session_state:
            st.session_state.current_step = 0
        
        current_step = st.session_state.current_step
        
        # Step navigation
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("⬅️ Previous", disabled=current_step == 0, use_container_width=True):
                st.session_state.current_step = max(0, current_step - 1)
                st.rerun()
        
        with col2:
            st.markdown(f"**Step {current_step + 1} of {len(steps)}**")
            progress_bar = st.progress((current_step + 1) / len(steps))
        
        with col3:
            if st.button("Next ➡️", disabled=current_step == len(steps) - 1, use_container_width=True):
                st.session_state.current_step = min(len(steps) - 1, current_step + 1)
                st.rerun()
        
        # Current step display
        step = steps[current_step]
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 1rem; margin: 1rem 0; color: white; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{step['icon']}</div>
            <h2 style="margin: 0; color: white;">{step['title']}</h2>
            <p style="font-size: 1.2rem; margin: 1rem 0 0 0; color: #f0f0f0;">{step['content']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Step completion
        if st.button(f"✅ Mark Step {current_step + 1} Complete", use_container_width=True):
            if guide['title'] not in st.session_state.visual_guides['completed_demos']:
                completed_demos = st.session_state.visual_guides['completed_demos']
                completed_demos.add(guide['title'])
                st.session_state.visual_guides['completed_demos'] = completed_demos
                
                # Show celebration
                self.show_celebration(f"Step {current_step + 1} completed!", "success")
                st.rerun()
        
        # Interactive elements for certain steps
        if "git init" in step['content']:
            st.markdown("#### 💻 Try it yourself:")
            st.code("git init", language="bash")
            st.info("Open your terminal and run this command in your project folder!")
        
        elif "git status" in step['content']:
            st.markdown("#### 💻 Try it yourself:")
            st.code("git status", language="bash")
            st.info("This command shows you which files have changed!")
        
        elif "git add" in step['content']:
            st.markdown("#### 💻 Try it yourself:")
            st.code("git add .", language="bash")
            st.info("This stages all your changes for commit!")
        
        elif "git commit" in step['content']:
            st.markdown("#### 💻 Try it yourself:")
            st.code('git commit -m "Add new feature"', language="bash")
            st.info("Replace 'Add new feature' with your own message!")
        
        elif "git push" in step['content']:
            st.markdown("#### 💻 Try it yourself:")
            st.code("git push origin main", language="bash")
            st.info("This uploads your changes to GitHub!")
        
        # Guide completion
        if current_step == len(steps) - 1:
            if st.button("🎉 Complete Guide", use_container_width=True):
                completed_demos = st.session_state.visual_guides['completed_demos']
                completed_demos.add(guide['title'])
                st.session_state.visual_guides['completed_demos'] = completed_demos
                self.show_celebration(f"'{guide['title']}' guide completed!", "guide_complete")
    
    def render_session_management(self):
        """Render session state management interface"""
        st.markdown("## 📊 Session Management")
        st.markdown("Track your learning progress and session data")
        
        # Progress data
        progress = st.session_state.interactive_progress
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 Learning Progress")
            
            # Overall progress
            st.metric("Overall Progress", f"{progress['overall_progress']}%")
            st.progress(progress['overall_progress'] / 100)
            
            # Pages visited
            st.markdown("**Pages Visited:**")
            for page, data in progress['pages'].items():
                status = "✅" if data.get('completed', False) else "👁️" if data.get('last_visited') else "⭕"
                st.markdown(f"{status} {page.replace('-', ' ').title()}")
            
            # Quiz scores
            if progress['quiz_scores']:
                st.markdown("### 📝 Quiz Scores")
                for section, score_data in progress['quiz_scores'].items():
                    st.metric(
                        f"{section.replace('-', ' ').title()}", 
                        f"{score_data['percentage']}%",
                        f"{score_data['correct']}/{score_data['total']} correct"
                    )
        
        with col2:
            st.markdown("### ⏱️ Time Tracking")
            
            if progress['time_spent']:
                total_time = sum(progress['time_spent'].values())
                st.metric("Total Time Spent", f"{total_time} minutes")
            
            st.markdown("### 🎯 Learning Stats")
            st.metric("Questions Answered", progress['total_questions_answered'])
            st.metric("Correct Answers", progress['correct_answers'])
            
            if progress['total_questions_answered'] > 0:
                accuracy = int((progress['correct_answers'] / progress['total_questions_answered']) * 100)
                st.metric("Overall Accuracy", f"{accuracy}%")
            
            # Session reset options
            st.markdown("### 🔧 Session Controls")
            
            if st.button("🔄 Reset Quiz Progress", use_container_width=True):
                self.reset_quiz_session()
                st.success("Quiz progress reset!")
            
            if st.button("🏆 Reset Achievements", use_container_width=True):
                self.reset_achievements()
                st.success("Achievements reset!")
            
            if st.button("🗑️ Clear All Progress", use_container_width=True):
                self.clear_all_progress()
                st.success("All progress cleared!")
    
    def render_celebration_animation(self):
        """Render achievement celebration animations"""
        visual_guides = st.session_state.visual_guides
        
        if visual_guides.get('show_celebration', False):
            message = visual_guides.get('celebration_message', '')
            celebration_type = visual_guides.get('celebration_type', 'success')
            
            if celebration_type == "success":
                st.balloons()
                st.success(f"🎉 {message}")
            elif celebration_type == "guide_complete":
                st.snow()
                st.success(f"🏆 {message}")
            elif celebration_type == "achievement":
                st.balloons()
                st.success(f"🏅 {message}")
            
            # Auto-hide celebration after a few seconds
            time.sleep(3)
            visual_guides['show_celebration'] = False
    
    # Helper methods for state management
    def submit_answer(self, section_key: str, question_idx: int, answer_index: int):
        """Submit a quiz answer and show feedback"""
        quiz_state = st.session_state.quiz_state
        quiz_state['selected_answers'][f"{section_key}_{question_idx}"] = answer_index
        quiz_state['show_feedback'] = True
        quiz_state['answer_submitted'] = True
        
        # Track stats
        progress = st.session_state.interactive_progress
        progress['total_questions_answered'] += 1
        
        # Check if answer is correct
        section = QUIZ_SECTIONS[section_key]
        question = section['questions'][question_idx]
        if answer_index == question['correct']:
            progress['correct_answers'] += 1
    
    def skip_question(self, section_key: str):
        """Skip a quiz question"""
        self.next_question(section_key)
    
    def next_question(self, section_key: str):
        """Move to next question or show results"""
        quiz_state = st.session_state.quiz_state
        section = QUIZ_SECTIONS[section_key]
        
        if quiz_state['current_question'] < len(section['questions']) - 1:
            quiz_state['current_question'] += 1
            quiz_state['show_feedback'] = False
        else:
            # Quiz completed
            quiz_state['show_results'] = True
    
    def save_quiz_score(self, section_key: str, score_percentage: int, correct: int, total: int):
        """Save quiz score and check for achievements"""
        progress = st.session_state.interactive_progress
        progress['quiz_scores'][section_key] = {
            'percentage': score_percentage,
            'correct': correct,
            'total': total,
            'completed_at': datetime.now().isoformat()
        }
        
        # Check quiz achievements
        self.check_quiz_achievements()
    
    def mark_section_complete(self, section_key: str):
        """Mark a section as complete and show celebration"""
        progress = st.session_state.interactive_progress
        completed_sections = progress.get('sections_completed', set())
        completed_sections.add(section_key)
        progress['sections_completed'] = completed_sections
        
        self.show_celebration(f"'{QUIZ_SECTIONS[section_key]['title']}' section completed!", "success")
        st.rerun()
    
    def check_quiz_achievements(self):
        """Check for quiz-related achievements"""
        achievements = st.session_state.interactive_achievements
        progress = st.session_state.interactive_progress
        
        # Quiz Master - 100% on any quiz
        if not achievements['quiz_master']['unlocked']:
            for section_data in progress['quiz_scores'].values():
                if section_data['percentage'] == 100:
                    self.unlock_achievement('quiz_master')
                    break
        
        # Knowledge Seeker - 80%+ average across all quizzes
        if not achievements['knowledge_seeker']['unlocked'] and progress['quiz_scores']:
            avg_score = sum(data['percentage'] for data in progress['quiz_scores'].values()) / len(progress['quiz_scores'])
            if avg_score >= 80:
                self.unlock_achievement('knowledge_seeker')
    
    def unlock_achievement(self, achievement_id: str):
        """Unlock an achievement and show celebration"""
        achievements = st.session_state.interactive_achievements
        if not achievements[achievement_id]['unlocked']:
            achievements[achievement_id]['unlocked'] = True
            achievements[achievement_id]['unlocked_at'] = datetime.now().isoformat()
            
            achievement_def = ACHIEVEMENT_DEFINITIONS[achievement_id]
            self.show_celebration(
                f"Achievement Unlocked: {achievement_def['title']} - {achievement_def['description']}", 
                "achievement"
            )
    
    def show_celebration(self, message: str, celebration_type: str = "success"):
        """Show celebration animation"""
        visual_guides = st.session_state.visual_guides
        visual_guides['show_celebration'] = True
        visual_guides['celebration_message'] = message
        visual_guides['celebration_type'] = celebration_type
    
    def reset_quiz_session(self):
        """Reset quiz session state"""
        st.session_state.quiz_state = {
            'current_section': 'core-concepts',
            'current_question': 0,
            'selected_answers': {},
            'show_results': False,
            'quiz_completed': set(),
            'section_scores': {},
            'show_feedback': False,
            'answer_submitted': False,
            'start_time': None,
            'time_per_question': []
        }
    
    def reset_quiz_section(self, section_key: str):
        """Reset a specific quiz section"""
        st.session_state.quiz_state['current_question'] = 0
        # Clear answers for this section only
        keys_to_remove = [key for key in st.session_state.quiz_state['selected_answers'].keys() 
                         if key.startswith(section_key)]
        for key in keys_to_remove:
            del st.session_state.quiz_state['selected_answers'][key]
        st.session_state.quiz_state['show_feedback'] = False
        st.session_state.quiz_state['show_results'] = False
    
    def reset_achievements(self):
        """Reset all achievements"""
        for achievement_id in st.session_state.interactive_achievements:
            st.session_state.interactive_achievements[achievement_id] = {
                'unlocked': False, 
                'unlocked_at': None
            }
    
    def clear_all_progress(self):
        """Clear all progress data"""
        st.session_state.interactive_progress = {
            'pages': {},
            'overall_progress': 0,
            'total_pages': 11,
            'current_page': 'home',
            'started_at': datetime.now().isoformat(),
            'last_activity': datetime.now().isoformat(),
            'quiz_scores': {},
            'time_spent': {},
            'sections_completed': set(),
            'current_streak': 0,
            'total_questions_answered': 0,
            'correct_answers': 0
        }
        self.reset_achievements()
        self.reset_quiz_session()
        st.session_state.visual_guides = {
            'completed_demos': set(),
            'current_demo': None,
            'demo_progress': {},
            'show_celebration': False,
            'celebration_message': '',
            'celebration_type': 'success'
        }

# Main application
def main():
    """Main function to render all interactive features"""
    
    # Initialize interactive features
    features = InteractiveFeatures()
    
    # Render main dashboard
    features.render_dashboard()
    
    # Create tabs for different features
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Interactive Quiz",
        "🏆 Achievements", 
        "🎬 Visual Guides",
        "📊 Session Management",
        "🎉 Celebrations"
    ])
    
    with tab1:
        features.render_interactive_quiz()
    
    with tab2:
        features.render_achievement_system()
    
    with tab3:
        features.render_visual_guides()
    
    with tab4:
        features.render_session_management()
    
    with tab5:
        features.render_celebration_animation()
    
    # Render celebration animations at the end
    features.render_celebration_animation()

if __name__ == "__main__":
    main()