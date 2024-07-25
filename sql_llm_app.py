from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[
    """

        you are a expert in converting English question to sql query!
        The sql database has the name student and has the following columns -Name,class,section\n\n for 
        example ,\n Example 1- How many entries of records are present?,
        the sql command will be something like this select count(*) from student ;
        \n Example 2 - tell me all the students studying in Ai class?,
        the sql command will be something like the select * from student where class ="Ai";
        also the sql code should not have ''' in beginnig or end and sql word in the output

        """
]




st.set_page_config(page_title="i can retrieve any sql query")
st .header("Gemini app to retrieve sql data")

question=st.text_input("Input: ",key="input")
submit=st.button("ask")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("the response is ")
    for row in data:
        print(row)
        st.header(row)