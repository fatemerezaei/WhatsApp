require('dotenv').config();

const authToken = process.env.TWILIO_AUTH_TOKEN;
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const my_client = require('twilio')(accountSid, authToken);

my_client.messages.create({
  from: 'whatsapp:twilio number',
  body: 'Hello World From Twilio!',
  to: 'whatsapp: my_number'
}).then(message => console.log(`Message: ${message.sid}`));