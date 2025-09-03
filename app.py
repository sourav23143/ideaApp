from flask import Flask, request
#request use to track request body

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

'''
Create a RESTful endpoint for creating a new idea
'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    #logic to create a new idea


    #whenverr we created something like this there is a chance that there might be some error in it so we use try- except 
    try:

        #first read the request body 
        request_body = request.get_json()


        #check if the idea id passed is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "idea with same id already present",400
    

        #Insert the passed idea in the ideas dictonary
        ideas[request_body["id"]] = request_body

        #return the response saying idea got saved
        return "idea created and saved sucessfully",201
    except KeyError:
        return "id is missing",400
    except:
        return "Some internal server error", 500
    

if __name__ == '__main__':
    app.run(port=5000 )
