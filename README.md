
# AI.Insights
### AI.Insights is a Streamlit app that allows users to ask questions about a PDF document and receive answers from a chatbot powered by Langchain and OpenAI.

### Usage
To use AI.Insights, follow these steps:

- Install the required packages by running pip install -r requirements.txt in the terminal.
- Run the app by executing python main.py in the terminal.
- Upload a PDF file using the file uploader in the sidebar.
- Enter your question in the input box provided and click the "Ask" button.
T- he chatbot will generate an answer based on the content of the PDF document.

### How it works
AI.Insights uses Streamlit, an open-source Python library that allows users to create interactive web applications using only Python code. The app takes a PDF file as input and converts it into a text format using the PyPDF2 package.

The app then uses the Langchain API to extract information from the text by performing named entity recognition, entity linking, and text classification. This information is used to generate an answer to the user's question.

The chatbot uses OpenAI's GPT-3 model to generate a response based on the question and the information extracted from the PDF. The response is displayed in the app, allowing the user to interact with the chatbot.

### Contributing
If you would like to contribute to AI.Insights, please submit a pull request. We welcome contributions from developers of all skill levels.

### Credits
AI.Insights was created by Joseph Szklar. The app uses the following libraries and APIs:

Streamlit
PyPDF2
Langchain
OpenAI
