
def send_email(to, subject,*args,**kargs):
    print(f"Sending an email to: {to}")
    print(f"Email subject: {subject}")

    if args:
        print("Additional receipients")
        for recipient in args:
            print(recipient)
    
    if kargs:
        print("Additional details for the email")
        for key in list(kargs):
            print(f"{key}: {kargs[key]}")

send_email('test@test.com', 'Hello world', 'other@test.com','someone@test.com', bbc='bogdan@gmail.com')