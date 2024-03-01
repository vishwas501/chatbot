from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

# Global variable to track if it's the first interaction
first_interaction = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/chat', methods=['POST'])
def chat():
    global first_interaction  # Access the global variable

    user_input = request.form['user_input']
    username = request.form.get('username', 'User')

    # Check if it's the first interaction
    if first_interaction == True:
        bot_response = f"<img src='/static/bot.png' alt='Maya Photo' style='width: 50px; height: 50px; border-radius: 50%;'>" \
                       f"Maya: Hello! I'm Maya, your virtual assistant. What's your name?"
        first_interaction = False  # Update the flag
    else:
        bot_response = get_bot_response(user_input, username)

    return bot_response


def get_bot_response(user_input, username):
    user_input = user_input.lower()
    
    # Construct user message with photo, name, and input
    user_message = f"<img src='/static/userphoto.png' alt='User Photo' style='width: 50px; height: 50px; border-radius: 50%;'>"
    user_message += f"<strong>{username}:</strong> {user_input}<br><br>"
    
    bot_message = ""  # Initialize bot response

    # Bot responses
    if "hi" in user_input or "hello" in user_input:
        bot_message += f"<img src='/static/bot.png' alt='Maya Photo' style='width: 50px; height: 50px; border-radius: 50%;'>"
        bot_message += "Maya: Hello! Nice to meet you. What's your name?"
    elif username == 'User' and user_input:
        username = user_input.strip()  # Set username based on user input
        bot_message += f"<img src='/static/maya_photo.png' alt='Maya Photo' style='width: 50px; height: 50px; border-radius: 50%;'>"
        bot_message += f"Maya: Nice to meet you, {username}! How can I assist you today?"
    elif "admission" in user_input:
        bot_message += "Maya: Here's the admission information:<br><br>"
        bot_message += "Admission to B.A/B.Sc/B.Com/B.C.A 1st will be on merit basis.<br>"
        bot_message += "Regular admission to B.A./B.Sc./B.Com/B.C.A. 1st/3rd/5th Semester and On-Going Post-Graduate Classes will start from 27.07.2024.<br>"
        bot_message += "Admission to M.Sc. 1st Semester Physics/Chemistry will be on the basis of OCET Conducted by Panjab University, Chandigarh.<br>"
        bot_message += "No OCET is needed for Admission to M.Sc Mathematics/ M.A. History / Punjabi/ English / Hindi/ Political Science and PGDCA.<br><br>"
        bot_message += "For admission form, click <a href='https://spnmukerian.files.wordpress.com/2020/07/camscanner-07-28-2020-12.34.28.pdf' target='_blank'>here</a>.<br>"
        bot_message += "For online registration, click <a href='https://www.example.com/online_registration'>here</a>.<br>"
        bot_message += "For more details, refer <a href='https://www.example.com/admission_details'>here</a>."
    elif "apply" in user_input or "how to apply?" in user_input or "how to apply" in user_input:
        bot_message += "Maya: Students can apply to the college in two ways:<br><br>"
        bot_message += "1. Online Application: Students can apply online through the college's official website. You can find the online application form <a href='https://www.example.com/apply_online'>here</a>.<br>"
        bot_message += "2. Visit College: Alternatively, students can visit the college office in person and submit their application.<br>"
        bot_message += "Address: SPN College, Railway Road, Mukerian, Punjab 144211, India"
    elif "history" in user_input or "college history" in user_input or "college records" in user_input:
        bot_message += "Maya: The college derives its name from SWAMI PREMANAND, a saint and philosopher of the modern times.<br>"
        bot_message += "He was a great force in pioneering the religious sentiments in the second and third quarter of the past century.<br>"
        bot_message += "The essential spirit of Swamiji’s message lays emphasis upon the need for abolishing ignorance and dogmatic beliefs, which had for centuries crippled the human mind.<br>"
        bot_message += "It was thought appropriate by the people of the area to raise an educational institution in the memory of this enlightened son of God who met with a fatal accident on 23rd April, 1965 at Mukerian."
        bot_message += "You can find more about the college's history on the <a href='https://spncollegemukerian.com/college-history/'style='color: purple;' target='_blank'>college history page</a>."
    elif "about college" in user_input or "college" in user_input or "about us" in user_input:
        bot_message += "Maya: Swami Premanand Mahavidyalaya is a multifaculty postgraduate institution affiliated with Panjab University. It offers a variety of programs, including science, commerce, and arts. The college was founded in 1972 and has since grown to include over 1500 students."
        bot_message += "For more information, you can refer to <a href='https://spncollegemukerian.com/'target='_blank'>College Website</a>."
    elif "contact" in user_input or "contact us" in user_input:
        bot_message += "Maya: You can contact us via the following methods:<br>"
        bot_message += "<strong>Email:</strong> principalspn.mex@gmail.com<br>"
        bot_message += "<strong>Phone:</strong> 01883-244070<br>"
        bot_message += "<strong>Address:</strong> SPN College, Railway Road, Mukerian, Punjab 144211, India"
    elif "scholarships" in user_input:
        bot_message += "Maya: We offer various scholarships based on academic achievement, financial need, leadership qualities, and other criteria. You can find detailed information about available scholarships on our website's financial aid page."
    elif "course" in user_input:
        bot_message += "Maya: We offer various courses and degree programs, including undergraduate and postgraduate options."
    elif "housing" in user_input:
        bot_message += "Maya: We offer on-campus housing options for both domestic and international students. International students can apply for housing through our international student services office. Our on-campus housing includes dormitories, apartments, and family housing options."
    elif "campus tour" in user_input:
        bot_message += "Maya: You can schedule a campus tour through our website's admissions page. We offer both group tours and individual tours led by student guides. You can select a date and time that works for you and register for the tour online."
    elif "thank you" in user_input or "thanks" in user_input:
        bot_message += "Maya: You're welcome! If you have any more questions, feel free to ask."
    else:
        bot_message += "Maya: I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"
    
    return user_message + bot_message

if __name__ == '__main__':
    app.run(debug=True)
