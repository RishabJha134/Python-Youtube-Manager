import pymongo
from bson import ObjectId

# please enter you username and password.
client = pymongo.MongoClient("mongodb+srv://username:password@cluster0.3h2q7py.mongodb.net/",tlsAllowInvalidCertificates=True)



db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)
print(type(video_collection))

# tlsAllowInvalidCertificates=True :- it is not a good way to handle a ssl certificates.




def Add_video(name,time):
    video_collection.insert_one({"name":name, "time":time})

def list_All_videos():
    for video in video_collection.find():
       
         print(f"Id:{video['_id']}, Name: {video['name']}, Time:{video['time']}")


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def update_video(video_id,name,time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name":name, "time":time}}
        )



def main():

    while True:

        print("youtube manager")
        print("1. list all videos")
        print("2. add a videos")
        print("3. delete a videos")
        print("4. update a videos")
        print("5. exit the app")

        choice = input("enter a choice:")

        if(choice == "1"):
            list_All_videos()
        elif(choice == "2"):
            name = input("enter the video")
            time = input("enter the time")
            Add_video(name,time)
        elif(choice == "3"):
            video_id = input("enter the video id")
            delete_video(video_id)
        elif(choice == "4"):
            video_id = input("enter the video id")
            name = input("enter the video")
            time = input("enter the time")
            update_video(video_id,name,time)
        elif(choice == "5"):
            break
        else:
            print("invalid choice")



if __name__ == "__main__":
    main()




# find method iterable return karta hai:-
# example:- for video in video_collection.find():
# it returns the all items present in the video collection.
# bson format :- object id(_id):- it is in mongo db
# terminal me always value string ke format me hi di jaati hai.