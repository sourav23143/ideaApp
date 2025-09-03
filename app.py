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
        "id" : 2,
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
    #I need to read the query param
    idea_author = request.args.get('idea_author') #request.args.get('idea_author'): this is used to read the query param

    if idea_author:
        #filter the idea created by this author
        idea_res ={}
        for key, value in ideas.items():
            if value["idea_author"] == idea_author :
                idea_res[key]  = value #then put that in idea_res


        return idea_res
    


    #logic to fetch all the ideas and support query params
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
    

'''End point to fetch idea based on id'''
@app.get("/ideaapp/api/v1/ideas/<idea_id>")   #any thing that is path param must be inside < > angular bracket
def get_idea_id(idea_id):                         #since it is path param so we also able to make it part of method
    #any thing inside idea_id is treated as string
    #but the idea_id is integer so we have to convert it into int
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "Idea id passed is not present",400

    except :
        return "Some internal error happened",500



'''
Endpoint for update the idea
'''
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] =request.get_json()  #here we are checking request body and what ever be request body we will update that in ideas[int(idea_id)]
            return ideas[int(idea_id)],200
        else:
            return "Idea id passed is not present",400

    except :
        return "Some internal error happened",500


'''
Endpoint to delete an idea
'''
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))   #delete the entry from server
            return "Idea got successfully removed"
           
        else:
            return "Idea id passed is not present",400

    except :
        return "Some internal error happened",500



if __name__ == '__main__':
    app.run(port=5000 )
