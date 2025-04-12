import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ap import extract_text_from_class, generate_sop

class SOPGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("SOP/Mail Generator - Tuhin Bidyanta")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #F1EFEC;")
        
        layout = QVBoxLayout()
        
        self.url_label = QLabel("Enter Webpage URL:")
        self.url_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.url_label.setStyleSheet("color: #030303;")
        layout.addWidget(self.url_label)
        
        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("padding: 5px; border: 2px solid #123458; border-radius: 5px; background-color: #D4C9BE;")
        layout.addWidget(self.url_input)
        
        self.prompt_label = QLabel("Enter Additional Prompt:")
        self.prompt_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.prompt_label.setStyleSheet("color: #030303;")
        layout.addWidget(self.prompt_label)
        
        self.prompt_input = QLineEdit()
        self.prompt_input.setStyleSheet("padding: 5px; border: 2px solid #123458; border-radius: 5px; background-color: #D4C9BE;")
        layout.addWidget(self.prompt_input)
        
        self.option_label = QLabel("Select Output Type:")
        self.option_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.option_label.setStyleSheet("color: #030303;")
        layout.addWidget(self.option_label)
        
        self.option_dropdown = QComboBox()
        self.option_dropdown.addItems(["SOP", "Gmail", "Research Proposal", "Cover Letter"])
        self.option_dropdown.setStyleSheet("padding: 5px; border: 2px solid #123458; border-radius: 5px; background-color: #D4C9BE;")
        layout.addWidget(self.option_dropdown)
        
        self.generate_button = QPushButton("Generate")
        self.generate_button.setStyleSheet("background-color: #123458; color: white; padding: 10px; border: none; border-radius: 5px; font-weight: bold;")
        self.generate_button.clicked.connect(self.generate_content)
        layout.addWidget(self.generate_button)
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("padding: 10px; border: 2px solid #123458; border-radius: 5px; background-color: #D4C9BE; color: #030303;")
        layout.addWidget(self.output_text)
        
        self.setLayout(layout)
    
    def generate_content(self):
        url = self.url_input.text()
        additional_prompt = self.prompt_input.text()
        option = self.option_dropdown.currentText()
        topics = extract_text_from_class(url)
        
        if not topics:
            self.output_text.setText("No topics found.")
            return
        
        prompt_type = "statement of purpose" if option == "SOP" else "professional email using Respected sir/mam" if option == "Gmail" else "research proposal" if option == "Research Proposal" else "cover letter"
        
        response_text = generate_sop(topics, additional_prompt, prompt_type)
        self.output_text.setText(response_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SOPGeneratorApp()
    window.show()
    sys.exit(app.exec())
