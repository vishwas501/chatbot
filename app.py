from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

# Global variable to track if the username has been set
username_set = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/chat', methods=['POST'])
def chat():
    global username_set

    user_input = request.form['user_input']
    username = request.form.get('username', 'User')
    
    # Set username only if it's still the default and there is valid input
    
    bot_response = get_bot_response(user_input, username)

    # Construct bot message with photo, name,
    bot_message = f"<img src='/static/bot.png' alt='Bot Photo' style='width: 50px; height: 50px; border-radius: 50%;'>"
    bot_message += f"<strong>Maya:</strong> {bot_response}<br><br>"
    
    # Construct user message with photo, name, and input
    user_message = f"<img src='/static/userphoto.png' alt='User Photo' style='width: 50px; height: 50px; border-radius: 50%;'>"
    user_message += f"<strong>You:</strong> {user_input}<br><br>"
    
    return bot_message 

def get_bot_response(user_input, username):
    user_input = user_input.lower()
    
    bot_message = ""  # Initialize bot response

    # Bot responses
    if "hello" in user_input or "hii" in user_input:
        bot_message += "Hello! Nice to meet you."
    elif "admission" in user_input:
        bot_message += "Here's the admission information:<br><br>"
        bot_message += "Admission to B.A/B.Sc/B.Com/B.C.A 1st will be on merit basis.<br>"
        bot_message += "Regular admission to B.A./B.Sc./B.Com/B.C.A. 1st/3rd/5th Semester and On-Going Post-Graduate Classes will start from 27.07.2024.<br>"
        bot_message += "Admission to M.Sc. 1st Semester Physics/Chemistry will be on the basis of OCET Conducted by Panjab University, Chandigarh.<br>"
        bot_message += "No OCET is needed for Admission to M.Sc Mathematics/ M.A. History / Punjabi/ English / Hindi/ Political Science and PGDCA.<br><br>"
        bot_message += "For admission form, click <a href='https://spnmukerian.files.wordpress.com/2020/07/camscanner-07-28-2020-12.34.28.pdf' target='_blank'>here</a>.<br>"
        bot_message += "For online registration, click <a href='https://www.example.com/online_registration'>here</a>.<br>"
        bot_message += "For more details, refer <a href='https://www.example.com/admission_details'>here</a>."
    elif "fees" in user_input or "fee" in user_input or "fees structure" in user_input or "fee structure" in user_input:  
      bot_message += "Sure! Here are the available courses for which you can inquire about fees:<br><br>"
      bot_message += "1. B.A<br>"
      bot_message += "2. B.Sc<br>"
      bot_message += "3. B.Com<br>"
      bot_message += "4. B.C.A<br>"
      bot_message += "5. M.Sc in Physics/Chemistry<br>"
      bot_message += "6. M.A in History/Punjabi/English<br>"
      bot_message += "<br>Please type the number corresponding to the course you want to inquire about."
    elif user_input.isdigit():
     selection = int(user_input)
     if selection == 1:
        bot_message += "Here is the fee structure for B.A:<br><br>"
        bot_message += "1st Semester: $XXXX<br>"
        bot_message += "2nd Semester: $XXXX<br>"
        bot_message += "3rd Semester: $XXXX<br>"
        bot_message += "4th Semester: $XXXX<br>"
        bot_message += "5th Semester: $XXXX<br>"
        bot_message += "6th Semester: $XXXX<br>"
     elif selection ==2:
        bot_message += "Here is the fee structure for B.S.c:<br><br>"
        bot_message += "1st Semester: &#8377;14000<br>"
        bot_message += "2nd Semester: &#8377;14000<br>"
        bot_message += "3rd Semester: &#8377;15000<br>"
        bot_message += "4th Semester: &#8377;15000<br>"
        bot_message += "5th Semester: &#8377;16000<br>"
        bot_message += "6th Semester: &#8377;16000<br>" 
     elif selection ==3:
        bot_message += "Here is the fee structure for B.com:<br><br>"
        bot_message += "1st Semester: &#8377;10,000<br>"
        bot_message += "2nd Semester: &#8377;10,000<br>"
        bot_message += "3rd Semester: &#8377;12,000<br>"
        bot_message += "4th Semester: &#8377;12,000<br>"
        bot_message += "5th Semester: &#8377;12,500<br>"
        bot_message += "6th Semester: &#8377;12,500<br>" 
     elif selection ==4:
        bot_message += "Here is the fee structure for B.C.A:<br><br>"
        bot_message += "<hr>1st Semester: &#8377;25,000<br>"
        bot_message += "<hr>2nd Semester: &#8377;25,0000<br>"
        bot_message += "<hr>3rd Semester: &#8377;26,000<br>"
        bot_message += "<hr>4th Semester: &#8377;26,000<br>"
        bot_message += "<hr>5th Semester: &#8377;26,500<br>"
        bot_message += "<hr>6th Semester: &#8377;26,500<br><hr>"        
     elif selection ==5:
        bot_message += "Here is the fee structure for M.S.C:<br><br>"
        bot_message += "<hr>1st Semester: $XXXX<br>"
        bot_message += "<hr>2nd Semester: $XXXX<br>"
        bot_message += "<hr>3rd Semester: $XXXX<br>"
        bot_message += "<hr>4th Semester: $XXXX<br>"
        bot_message += "<hr>5th Semester: $XXXX<br>"
        bot_message += "<hr>6th Semester: $XXXX<br><hr>" 
    else:
        bot_message += "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"
    
    return bot_message

if __name__ == '__main__':
    app.run(debug=True)
