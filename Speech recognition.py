import random
import speech_recognition as sr
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox

spoken_points = 0
written_points = 0
spoken_text = ""

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Speak something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text.lower()  # Convert recognized text to lowercase
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

def get_prompt(level):
    beginner_prompts = [
        "Tell us about your favorite food",
        "Describe your pet if you have one",
        "Talk about a movie you recently watched",
        "What is your favorite color and why",
        "Share about a memorable childhood event",
        "Discuss a recent trip or vacation",
        "Explain a hobby or interest you have",
        "Talk about your dream job",
        "Describe a typical day in your life",
        "What are your thoughts on social media",
        "Discuss a favorite book or author",
        "What do you enjoy doing in your free time",
        "Describe a family tradition",
        "Share about a favorite TV show or series",
        "Talk about a historical event that interests you"
    ]

    intermediate_prompts = [
        "Explain the importance of recycling",
        "Discuss the impact of social media on society",
        "Share your views on climate change",
        "What are your thoughts on artificial intelligence",
        "Discuss the benefits of regular exercise",
        "Explain the process of learning a new language",
        "Talk about a recent technological advancement",
        "Discuss the impact of music on people's lives",
        "Explain the concept of time management",
        "Share your views on modern education systems",
        "Discuss the pros and cons of working from home",
        "What are your thoughts on renewable energy",
        "Share about a volunteering experience",
        "Discuss the significance of cultural diversity",
        "Explain the effects of global warming"
    ]

    advanced_prompts = [
        "Discuss the future of artificial intelligence",
        "Explain the concept of time dilation in physics",
        "Share your views on space exploration",
        "What are your thoughts on quantum computing",
        "Discuss the ethical implications of genetic engineering",
        "Explain the economic impact of globalization",
        "Share your views on virtual reality technology",
        "Discuss the impact of artificial intelligence on employment",
        "What do you think about the future of healthcare",
        "Explain the theory of relativity",
        "Discuss the impact of nanotechnology on society",
        "What are your thoughts on brain-computer interfaces",
        "Explain the concept of dark matter in astrophysics",
        "Discuss the role of robotics in various industries",
        "Share your views on bioethics and biotechnology"
    ]

    if level == "beginner":
        return random.choice(beginner_prompts)
    elif level == "intermediate":
        return random.choice(intermediate_prompts)
    elif level == "advanced":
        return random.choice(advanced_prompts)
    else:
        return "Invalid level selected."

# Add more prompts to the lists above for each level

def start_session():
    global spoken_points, written_points, spoken_text
    
    level = level_dropdown.currentText().lower()

    if level == 'exit':
        output_text.setText("Exiting the program.")
        return

    if level in ["beginner", "intermediate", "advanced"]:
        prompt = get_prompt(level)
        prompt_display.setText(f"Prompt: {prompt}")  # Display the prompt
        
        input("Press Enter when ready to read aloud.")
        print("Read the prompt aloud:")
        print(prompt)
        input("Press Enter when done reading.")
        
        spoken_text = recognize_speech()
        print(f"Captured spoken text: {spoken_text}")

        if spoken_text.lower() == 'exit':
            print("Exiting the program.")
            return

        if spoken_text.lower() == prompt.lower():
            print("Great job! Your spoken sentence matches the prompt.")
            spoken_points += 1
        else:
            print("Your spoken sentence doesn't match the prompt. Try again or work on refining your speech.")

        written_text = ""
        while written_text != prompt:
            print("\nNow, write about the prompt:")
            written_text = input().strip()

            if written_text.lower() == 'exit':
                print("Exiting the program.")
                return

            if written_text == prompt:
                print("Great job! Your written sentence matches the prompt.")
                written_points += 1
            else:
                print("Your written sentence doesn't match the prompt. Try again or work on refining your writing.")

        print(f"Total Spoken Points: {spoken_points}")
        print(f"Total Written Points: {written_points}")

    else:
        output_text.setText("Invalid level selected. Please choose beginner, intermediate, or advanced.")

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Improve Writing and Speaking Skills")

central_widget = QWidget()
layout = QVBoxLayout(central_widget)

level_dropdown = QComboBox()
level_dropdown.addItems(["Select Level", "beginner", "intermediate", "advanced", "exit"])
layout.addWidget(level_dropdown)

start_button = QPushButton("Start Session")
start_button.clicked.connect(start_session)
layout.addWidget(start_button)

prompt_display = QLabel("Prompt will be displayed here")
layout.addWidget(prompt_display)

output_text = QLabel("")
layout.addWidget(output_text)

window.setCentralWidget(central_widget)
window.show()
app.exec()