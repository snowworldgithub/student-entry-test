import streamlit as st
import time
import random
from styles import load_css
from pdf_generator import create_pdf_report, get_pdf_download_link
from test_sections import show_section_questions
from utils import initialize_session_state

# Must be the first Streamlit command
st.set_page_config(
    page_title="Ahmed's Educational System - Admission Test",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
initialize_session_state()

def show_registration_form():
    st.header("📝 Student Registration")
    
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Student Name", key="name_input")
        student_age = st.number_input("Student Age", min_value=3, max_value=6, value=3, key="age_input")
    
    with col2:
        applying_class = st.selectbox("Applying for Class", ["Playgroup", "Nursery", "KG"], key="class_input")
        student_gender = st.selectbox("Gender", ["Male", "Female"], key="gender_input")

    if st.button("Register & Start Test ▶️", key="register_button", type="primary"):
        if student_name.strip() == "":
            st.error("Please enter student name!")
            return
            
        student_id = f"student_{len(st.session_state.students) + 1}"
        st.session_state.students[student_id] = {
            'name': student_name,
            'age': student_age,
            'class': applying_class,
            'gender': student_gender,
            'test_status': 'pending',
            'scores': {},
            'current_section': 0
        }
        
        st.session_state.current_student = student_id
        st.success(f"✅ {student_name} registered successfully!")
        st.info("Starting test...")
        time.sleep(1)
        st.rerun()

def conduct_test(student_id):
    student = st.session_state.students[student_id]
    sections = ['English', 'Urdu', 'Math', 'General Knowledge', 'Islamiat']
    
    st.markdown(f"""
        <div class='section-header'>
            <h2>Test in Progress</h2>
            <p>Student: {student['name']} | Class: {student['class']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    progress = st.progress(student['current_section'] / len(sections))
    
    if student['current_section'] >= len(sections):
        student['test_status'] = 'completed'
        show_results(student_id)
        return
    
    current_section = sections[student['current_section']]
    st.subheader(f"📚 Section: {current_section}")
    
    score, submitted = show_section_questions(current_section, student_id)
    
    col1, col2 = st.columns([1,2])
    with col1:
        if st.button("Next Section ➡️", key=f"next_{student_id}_{current_section}"):
            student['scores'][current_section] = score
            student['current_section'] += 1
            st.rerun()

def show_results(student_id):
    student = st.session_state.students[student_id]
    st.header(f"Test Results - {student['name']}")
    
    # Add timestamp to make keys unique
    timestamp = int(time.time())
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Student Information")
        st.write(f"Name: {student['name']}")
        st.write(f"Age: {student['age']}")
        st.write(f"Class Applied: {student['class']}")
    
    with col2:
        st.subheader("Test Scores")
        total_score = sum(student['scores'].values())
        total_possible = len(student['scores']) * 2
        percentage = (total_score / total_possible) * 100
        
        for section, score in student['scores'].items():
            st.write(f"{section}: {score}/2")
        st.write(f"Overall: {percentage:.2f}%")
    
    # Add performance evaluation
    st.subheader("Performance Evaluation")
    if percentage >= 80:
        st.success("🌟 Excellent Performance! Highly Recommended for Admission")
    elif percentage >= 60:
        st.info("✨ Good Performance! Recommended for Admission")
    else:
        st.warning("⚠️ Needs Improvement! Parent Consultation Recommended")
    
    # Add unique keys using timestamp and random number
    download_key = f"download_{student_id}_{timestamp}"
    new_test_key = f"new_test_{student_id}_{timestamp}"
    
    col3, col4 = st.columns(2)
    with col3:
        if st.button("📥 Download Report", key=download_key):
            pdf = create_pdf_report(student, percentage)
            st.markdown(
                get_pdf_download_link(pdf, f"report_{student['name']}_{timestamp}.pdf"), 
                unsafe_allow_html=True
            )
    
    with col4:
        if st.button("🔄 Start New Test", key=new_test_key):
            st.session_state.current_student = None
            st.rerun()

    # Add recommendations section
    st.subheader("Recommendations")
    weak_sections = [section for section, score in student['scores'].items() if score < 1]
    if weak_sections:
        st.write("Areas needing improvement:")
        for section in weak_sections:
            st.write(f"- {section}")
        st.write("\nSuggested actions:")
        st.write("1. Regular practice in weak areas")
        st.write("2. Parent-teacher consultation recommended")
        st.write("3. Consider additional support in specific subjects")
    else:
        st.success("Student has performed well in all sections! Ready for admission.")

def main():
    load_css(st.session_state.theme)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        theme = st.selectbox(
            "Select Theme",
            ['Light', 'Dark'],
            index=0 if st.session_state.theme == 'light' else 1,
            key='theme_selector'
        )
        if theme.lower() != st.session_state.theme:
            st.session_state.theme = theme.lower()
            st.rerun()

    st.markdown("""
        <div class='main-header'>
            <div class='school-name'>Ahmed's Educational System</div>
            <div class='school-address'>Gulbahar Petal Gali</div>
        </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.header("Student Management")
        action = st.radio("Select Action", ["Add New Student", "View Existing Students"])
        
        if action == "View Existing Students":
            if st.session_state.students:
                st.subheader("Registered Students")
                for student_id, student in st.session_state.students.items():
                    if student['test_status'] == 'pending':
                        if st.button(f"Continue Test: {student['name']}", 
                                   key=f"continue_{student_id}"):
                            st.session_state.current_student = student_id
                            st.rerun()
                    elif student['test_status'] == 'completed':
                        if st.button(f"View Results: {student['name']}", 
                                   key=f"view_{student_id}"):
                            show_results(student_id)
            else:
                st.info("No students registered yet")

    st.markdown("<hr>", unsafe_allow_html=True)
    
    if action == "Add New Student":
        show_registration_form()
    elif st.session_state.current_student:
        conduct_test(st.session_state.current_student)
    else:
        st.markdown("""
            <div style='text-align: center; padding: 2rem;'>
                <h2>Welcome to Student Admission Test System</h2>
                <p>Please register a new student or select an existing student to continue.</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 