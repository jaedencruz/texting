# secret = 9Yggs4zZ45IwjFfTq47lwsEgGm15047e
#
# SID = SKda7a043c944fe4c8e35e62e9e6019c72

from twilio.rest import Client

account_sid = 'AC35995c6a5ea67c65e6eae6ff5683c33a'
auth_token = '63758374bdf2abd36c270788a55f53e4'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18669021138',
  body='he gon act like he dont know my bop, like, but i soon be the one thats on top, like, bro I used to get all them rocks, bag em, I used to put em on that block.',
  to='+13472603506'
)

print(message.sid)

print(message.sid)

