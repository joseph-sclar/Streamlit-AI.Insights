import os
#os.chdir("/Users/oanottage/Desktop/Personal_Projects/LangChainStreamLit/")

#import configparser
#config = configparser.ConfigParser()
#config.read('secrets/config.ini')


os.environ["OPENAI_API_KEY"] = "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"
openai_api_key = os.getenv('OPENAI_API_KEY')
#openai_api_key = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import openai
import streamlit as st
from streamlit import cache_resource
import time


from langchain.document_loaders import PyPDFLoader

st.set_page_config(page_title="AI Insights", page_icon="🤖", initial_sidebar_state="auto")

pdf_file = 0

@cache_resource
def upload_pdf_file(uploaded_file, openai_api_key):

    if uploaded_file is not None:
        with open(os.path.join("pdf_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"{uploaded_file.name} is saved successfully!")
        time.sleep(2)
        st.empty()

        # load the document
        st.markdown("")
        mesLoading = st.markdown("Loading your book (this may take a few seconds)...")
        loader = PyPDFLoader(f"pdf_files/{uploaded_file.name}")
        data = loader.load()
        time.sleep(3)
        mesLoading.empty()


        # show some stats
        mesLoaded = st.success("Your book has loaded successfully!")
        time.sleep(3)    
        mesLoaded.empty()



        # split the document into smaller chunks
        if len(data[0].page_content) >= 4000:
            mesChunkWarn = st.warning(f"There are {len(data[0].page_content)} characters in your document.\
                Your document is too long. Let's split it into smaller chunks")

            # split the document into smaller chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(data)
            time.sleep(2)
            mesChunkWarn.empty()

            mesChunkSuccess = st.success(f"Now you have {len(texts)} documents")
            time.sleep(2)
            mesChunkSuccess.empty()

            mesUnimake = st.success("Let's create a universe for you and your book!")
            time.sleep(3)
            mesUnimake.empty()


            

            # create a vectorstore
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            docsearch = Chroma.from_documents(texts, embeddings)
            qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch)
            

            mesUniverse = st.success("Your universe is created successfully!")
            time.sleep(2)
            mesUniverse.empty()

            return qa



        else:
            st.markdown("")
            mesNoChunkSuccess = st.success(f"There are {len(data[0].page_content)} characters in your document. No need for the extra stuff.")
            time.sleep(2)
            mesNoChunkSuccess.empty()
            
            mesUnimake = st.success("Let's create a universe for you and your book!")
            time.sleep(3)
            mesUnimake.empty()
            texts = data

            # create a vectorstore        
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            docsearch = Chroma.from_documents(texts, embeddings)
            qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch)
            mesUniverse = st.success("Your universe is created successfully!")
            time.sleep(2)
            mesUniverse.empty()

            return qa

    return None



def app():    
    st.markdown("# AI - Insights")


    st.markdown("Upload any PDF file and ask questions about it")


    
    ######### UPLOAD PDF FILE #########
    st.markdown("### Upload your PDF file")
    uploaded_file = st.file_uploader(label="Upload your PDF file", type=["pdf"], accept_multiple_files=False, key="pdf_uploader", help="Upload your book here. Only PDF files are accepted.")


    qa = upload_pdf_file(uploaded_file, openai_api_key)
    # if the pdf file is uploaded successfully
    if qa is not None:
        if uploaded_file is not None:
            st.markdown("-----------------------------")
            # show a chat box to communicate with the book
            st.markdown("### Time to talk to your book!")
            
            with st.form("query"):
                query = st.text_input(label="", placeholder="Ask a question!", value="", max_chars=100, key="question", help="Ask a question to your book.")
                submit_button = st.form_submit_button(label="Submit")
            
            if submit_button:
                if query.strip() != "":
                    st.markdown(f"### Q: {query}")
                    st.write(qa.run(query))
                
                else:
                    mesOpenAI = st.warning("⚠️ Please insert a valid question")
                    time.sleep(3)
                    mesOpenAI.empty()

    

if __name__ == '__main__':
    app()



