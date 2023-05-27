# vertex_palm_streamlit_flask
Vertex PaLM API integration with streamlit and Flask

Step 1: git clone https://github.com/lavinigam-gcp/vertex_palm_streamlit_flask.git

Step 2: run these commands on sheel for gcloud auth

#replace your project-id with PROJECT_ID. Make sure you have billing and Vertex API enabled before doing this. 
gcloud auth application-default login
gcloud auth application-default set-quota-project "PROJECT_ID"

Step 3: cd vertex_palm_streamlit_flask

Step 4: add your project-id in code as well. Do not skip step 2. 
        app.py       ---> PROJECT_ID = ""  #top of the page
        flask_app.py ---> PROJECT_ID = ""  #top of the page

Step 5: To run streamlit: 
        streamlit run app.py

        To run flask webapp: 
        python flask_app.py 

Step 6: Enjoy the API