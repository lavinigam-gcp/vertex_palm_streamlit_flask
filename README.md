# vertex_palm_streamlit_flask
Vertex PaLM API integration with streamlit and Flask

Step 1: 
>git clone https://github.com/lavinigam-gcp/vertex_palm_streamlit_flask.git

Step 2: 
>pip install -r requirements.txt

Step 3: run these commands on shell for gcloud auth

#replace your project-id with PROJECT_ID. Make sure you have billing and Vertex API enabled before doing this. 

>gcloud auth application-default login

>gcloud auth application-default set-quota-project "PROJECT_ID"

Step 4: 
>cd vertex_palm_streamlit_flask

Step 5: add your project-id in code as well. Do not skip step 3. 

>app.py       ---> PROJECT_ID = ""  #top of the page

>flask_app.py ---> PROJECT_ID = ""  #top of the page


Step 6(a): To run streamlit: 

>streamlit run app.py

Step 6(b): To run flask webapp: 

>python flask_app.py 

Step 7: Enjoy the API
