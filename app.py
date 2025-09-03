from flask import Flask

app = Flask(__name__) 

#Create the idea repositry. THis is where idea will be strored
ideas = {
    1: {
        "id" : 1,
        "idea_name": "ONDC",
        "idea_discription" : "Details about ONDC",
        "idea_author": "Sourav"
    },

    2: {
        "id" : 1,
        "idea_name": "Save soil",
        "idea_discription" : "Details about Saving Soil",
        "idea_author": "Gourav"
    }
}


'''
Create an RESTful endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas")  #a decorator which tell whenver anyone call get refer to below function
def get_all_ideas():
    #logic to fetch all the ideas
    return ideas   #so this is our control as inside it logic is written to fetch the ideas


if __name__ == '__main__':
    app.run(port=8080)
