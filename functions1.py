def main():
    #Empty dictionary to collect users
    responses={}
    
    #set flag condition to end or continue loop
    polling=True

    #while loop to fill responses
    while polling:
        name=input("Enter name: ")
        address1=input("House number and street: ")
        city=input("City: ")
        state=input("State: ")
        Zip=input("Zip code: ")
        responses[name]=address1
        responses[name]=city
        responses[name]=state
        responses[name]=Zip
        rep=input("Any more users y/n?")
        if rep=='n' or rep=='N':
            polling=False
    for info in responses.items():
        print("\nName:\t"+name+"\nAddress \t"+address1+"\ncity:\t"+city+",\nstate:\t "+state+"\nzip:\t "+Zip)
main()
