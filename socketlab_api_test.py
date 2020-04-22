from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.basicmessage import BasicMessage
from socketlabs.injectionapi.message.emailaddress import EmailAddress

serverId = #######
injectionApiKey = "????????????????"

client = SocketLabsClient(serverId, injectionApiKey);

message = BasicMessage()

message.subject = "Prove of Concept - Socketlab Email API"
message.html_body = "<html>This is a test email sent through a .py file testing the email API. Text me if you get this email. Thanks - Ron</html>"
message.plain_text_body = "This is a test email sent through a .py file testing the email API. Text me if you get this email. Thanks - Ron";

message.from_email_address = EmailAddress("no-reply@pencil_it_in.com")
message.to_email_address.append(EmailAddress("ron_villena@hotmail.com", "Ron Villena"))
message.to_email_address.append(EmailAddress("zlake@gmail.com", "Zachary Lake"))
message.to_email_address.append(EmailAddress("jhalv3@gmail.com", "Jeannie Halvorson"))
message.to_email_address.append(EmailAddress("deepinder93@gmail.com", "Depinder Kaur"))

response = client.send(message)

# Instructions for creating email
# https://cp.socketlabs.com/servers/32586/launch/languageselection/codesample?language=json
